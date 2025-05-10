import os
import re
import torch
import argparse
import numpy as np
from tqdm import tqdm
from pprint import pprint
from vllm import LLM, SamplingParams
from transformers import AutoTokenizer
from datasets import load_dataset, concatenate_datasets


def chat_template_gsm8k(**kwargs):
    question = kwargs['question']
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. You first thinks about the reasoning process in the mind and then provides the user with the answer.\n"
        },
        {
            'role': 'user',
            'content': f"Q: Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?\n<think>Natalia sold 48 clips in April and half as many clips in May, so she sold 48 / 2 = 24 clips in May.\nAltogether, she sold 48 + 24 = 72 clips.\nThe answer is 72.</think><answer> 72 </answer>\n\nQ: Weng earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?\n<think>Since Weng earns $12 an hour for babysitting, she earns $12 / 60 = $0.2 per minute.\n Working 50 minutes, she earned $0.2 x 50 = $10.\nThe answer is 10.</think><answer> 10 </answer>\n\nSimilar to the previous examples, solve the following math problem\nQ: {question}\n\n Show your work in <think> </think> tags. And return the final answer in <answer> </answer> tags."
        },
        {
            "role": "assistant",
            "content": "Let me solve this step by step.\n<think>"
        }
    ]
    return messages

def is_correct_gsm8k(completion, answer):
    answer = float(answer)
    answer_match = re.findall(r'<answer>\s*(.*?)\s*</answer>', completion, re.DOTALL)
    if len(answer_match) > 0:
        extracted_answer = answer_match[-1].strip()
        extracted_answer = extracted_answer.replace(",", "")
        extracted_answer = re.search(r'-?\d+(?:\.\d+)?', extracted_answer)
        if extracted_answer is not None:
            extracted_answer = float(extracted_answer.group(0))
            return 1 * (abs(answer - extracted_answer) < 1e-5)
    return 0


def chat_template_aqua(**kwargs):
    question = kwargs['question']
    options = "  ".join(kwargs['options'])
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. You first thinks about the reasoning process in the mind and then provides the user with the answer.\n"
        },
        {
            'role': 'user',
            'content': f"Q: A class of 35 students has an average height of 180 cm. Seven students whose average height is 120 cm, left the class and seven others whose average height is 140 cm, joined. Calculate the new average height of the students of the class (in cm) is?\nA)204.6 cm  B)404.6 cm  C)224.6 cm  D)184.0 cm  E)256.6 cm\n<think> The total height of students before seven students left is 180 * 35 = 6300 cm.The total height of students who joined is 140 * 7  = 980 cm. The new total height of students after seven students joined is 6300 - 840 + 980 = 6440 cm. The new average height is 6440 / 35 = 184 cm. The answer is D.</think><answer> D </answer>\n\nQ: How much is 70% of 40 is greater than 4/5 of 25?\nA)22  B)67  C)88  D)12  E)8\n<think> 70% of 40 is 40 * 0.7 = 28. 4/5 of 25 is 25 * 4/5 = 20. 70% of 40 is greater than 4/5 of 25 by 28 - 20 = 8. The answer is E.</think><answer> E </answer>\n\nSimilar to the previous examples, solve the following math question and choose an answer from the given options\nQ: {question}\n{options}\n\n Show your work in <think> </think> tags. And return the final answer in <answer> </answer> tags."
        },
        {
            "role": "assistant",
            "content": "Let me solve this step by step.\n<think>"
        }
    ]
    return messages

def is_correct_aqua(completion, answer):
    answer_match = re.findall(r'<answer>\s*(.*?)\s*</answer>', completion, re.DOTALL)
    if len(answer_match) > 0:
        if answer_match[-1].strip() == answer:
            return 1
    return 0


dataset_dict = {
    'aqua' : {
        'data_files' : [
            'datasets/aqua/trivial',
            'datasets/aqua/easy',
            'datasets/aqua/medium',
            'datasets/aqua/hard',
        ],
        'chat_template' : chat_template_aqua,
        'is_correct' : is_correct_aqua
    },
    'gsm8k' : {
        'data_files' : [
            'datasets/gsm8k/trivial',
            'datasets/gsm8k/easy',
            'datasets/gsm8k/medium',
            'datasets/gsm8k/hard'
        ],
        'chat_template' : chat_template_gsm8k,
        'is_correct' : is_correct_gsm8k
    }
}


def main(args):

    # Load tokenizer & model
    tokenizer = AutoTokenizer.from_pretrained(
        args.model,
        trust_remote_code=True,
    )
    model = LLM(
        model=args.model,
        trust_remote_code=True,
        tensor_parallel_size=torch.cuda.device_count(),
        dtype='bfloat16',
        gpu_memory_utilization=0.9,
        max_model_len=4096,
        seed=1234,
        task='generate'
    )
    sampling_params = SamplingParams(
        temperature=0,
        max_tokens=512,
        min_tokens=1,
        seed=1234
    )
    
    # Prepare dataset
    dataset = []
    for task_idx, data_dir in enumerate(dataset_dict[args.dataset]['data_files']):
        data = load_dataset('json', data_dir=data_dir, split='test')
        data = data.add_column("task", [task_idx] * len(data))
        dataset.append(data)
    dataset = concatenate_datasets(dataset)

    # Apply Chat Template
    prompts = [
        tokenizer.apply_chat_template(
            dataset_dict[args.dataset]['chat_template'](**example), 
            tokenize=False, 
            continue_final_message=True
        )
        for example in dataset
    ]

    # Generate Completions
    outputs = model.generate(prompts, sampling_params)

    # Check Correctness
    is_correct = np.array([
        dataset_dict[args.dataset]['is_correct'](request_output.outputs[-1].text, dataset['answer'][request_idx]) 
        for request_idx, request_output in tqdm(enumerate(outputs), desc='Checking Correctness')
    ])
    dataset = dataset.add_column('is_correct', is_correct.tolist())

    # Process Metrics
    results = dict()
    results['overall'] = {
        'accuracy': is_correct.mean().item(),
        'support': len(dataset)
    }
    for task_idx, data_dir in enumerate(dataset_dict[args.dataset]['data_files']):
        task_outputs = dataset.filter(lambda example: example['task']==task_idx)
        task_is_correct = np.array(task_outputs['is_correct'])
        results[os.path.basename(os.path.normpath(data_dir))] = {
            'accuracy': task_is_correct.mean().item(),
            'support': len(task_is_correct)
        }
    pprint(results, indent=4, width=2)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--model')
    parser.add_argument('--dataset')
    args = parser.parse_args()

    main(args)