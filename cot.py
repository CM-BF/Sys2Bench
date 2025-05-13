import os
import re
import json
import torch
import argparse
import numpy as np
from tqdm import tqdm
from vllm import LLM, SamplingParams
from transformers import AutoTokenizer
from datasets import load_dataset, concatenate_datasets


def chat_template_countdown(**kwargs):
    target = kwargs["answer"]
    numbers = kwargs["question"]
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. You first thinks about the reasoning process in the mind and then provides the user with the answer.\n"
        },
        {
            "role": "user",
            "content": f"Using the numbers {numbers}, create an equation that equals {target}. You can use basic arithmetic operations (+, -, *, /) and each number can only be used once. Show your work in <think> </think> tags. And return the final answer in <answer> </answer> tags, for example <answer> (1 + 2) / 3 </answer>."
        },
        {
            "role": "assistant",
            "content": "Let me solve this step by step.\n<think>"
        }
    ]
    return messages

def is_correct_countdown(completion, **kwargs):
    nums = kwargs['question']
    target = kwargs['answer']
    answer_match = re.findall(r'<answer>\s*(.*?)\s*</answer>', completion, re.DOTALL)
    if len(answer_match) > 0:
        extracted_answer = answer_match[-1].strip()
        numbers_in_eq = [int(n) for n in re.findall(r'\d+', extracted_answer)]
        # Each number should be used exactly once
        if sorted(numbers_in_eq) == sorted(nums):
            # Define a regex pattern that only allows numbers, operators, parentheses, and whitespace
            if re.match(r'^[\d+\-*/().\s]+$', extracted_answer):
                # Evaluate the equation with restricted globals and locals
                result = eval(extracted_answer, {"__builtins__": None}, {})
                # Account for floating point precision
                if abs(result - target) < 1e-5:
                    return 1
    return 0


def chat_template_gsm8k(**kwargs):
    question = kwargs['question']
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. You first thinks about the reasoning process in the mind and then provides the user with the answer.\n"
        },
        {
            "role": "user",
            "content": f"Solve the following math problem\n{question}\n\n Show your work in <think> </think> tags. And return the final answer in <answer> </answer> tags, for example <answer> 500 </answer>."
        },
        {
            "role": "assistant",
            "content": "Let me solve this step by step.\n<think>"
        }
    ]
    return messages

def is_correct_gsm8k(completion, **kwargs):
    answer = kwargs['answer']
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
            'content': f"Solve the following math problem and choose an answer from the given options\n{question}\n{options}\n\n Show your work in <think> </think> tags. And return the final answer in <answer> </answer> tags, for example <answer> C </answer>."
        },
        {
            "role": "assistant",
            "content": "Let me solve this step by step.\n<think>"
        }
    ]
    return messages

def is_correct_aqua(completion, **kwargs):
    answer = kwargs['answer']
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
        'max_prompt_length': 512,
        'max_completion_length': 512,
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
        'max_prompt_length': 1600,
        'max_completion_length': 512,
        'chat_template' : chat_template_gsm8k,
        'is_correct' : is_correct_gsm8k
    },
    'countdown' : {
        'data_files' : [
            'datasets/countdown/trivial',
            'datasets/countdown/easy',
            'datasets/countdown/medium',
            'datasets/countdown/hard',
            'datasets/countdown/ood',
        ],
        'max_prompt_length': 1000,
        'max_completion_length': 512,
        'chat_template' : chat_template_countdown,
        'is_correct' : is_correct_countdown
    }
}


model_dict = {
    'qwen15' : 'Qwen/Qwen2.5-1.5B-Instruct',
    'qwen' : 'Qwen/Qwen2.5-3B-Instruct',
    'llama3' : 'meta-llama/Llama-3.2-3B-Instruct'
}


def main(args):

    # Load tokenizer & model
    tokenizer = AutoTokenizer.from_pretrained(
        model_dict[args.model],
        trust_remote_code=True,
    )
    model = LLM(
        model=model_dict[args.model],
        trust_remote_code=True,
        tensor_parallel_size=torch.cuda.device_count(),
        dtype='bfloat16',
        gpu_memory_utilization=0.9,
        max_model_len=dataset_dict[args.dataset]['max_prompt_length']+dataset_dict[args.dataset]['max_completion_length'],
        seed=1234,
        task='generate'
    )
    sampling_params = SamplingParams(
        n=1,
        temperature=0,
        max_tokens=dataset_dict[args.dataset]['max_completion_length'],
        min_tokens=1,
        truncate_prompt_tokens=dataset_dict[args.dataset]['max_prompt_length'],
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
        dataset_dict[args.dataset]['is_correct'](request_output.outputs[-1].text, **dataset[request_idx]) 
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
    print(json.dumps(results, indent=4))


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--model')
    parser.add_argument('--dataset')
    args = parser.parse_args()

    main(args)