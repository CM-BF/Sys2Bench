import os
import re
import numpy as np
from datasets import load_dataset
from vllm import LLM, SamplingParams
from transformers import AutoTokenizer


def preprocess_aqua(dataset):
    dataset = dataset.rename_columns({
        'rationale' : 'solution',
        'correct' : 'answer'
    })
    return dataset


def chat_template_aqua(**kwargs):
    question = kwargs['question']
    options = "  ".join(kwargs['options'])
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. You first thinks about the reasoning process in the mind and then provides the user with the answer.\n"
        },
        {
            "role": "user",
            "content": f"Solve the following math problem and choose an answer from the given options\n{question}\n{options}\n\n Show your work in <think> </think> tags. And return the final answer in <answer> </answer> tags, for example <answer> C </answer>."
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


def split_into_tasks(dataset, num_splits):
    quantiles = [
        np.quantile(dataset['difficulty'], i/num_splits) 
        for i in range(1, num_splits)
    ] + [np.max(dataset['difficulty'])]

    tasks = dict((f'task{i}', []) for i in range(1, num_splits+1))
    for example_idx in range(len(dataset)):
        for task_idx, quantile in enumerate(quantiles):
            if dataset['difficulty'][example_idx] <= quantile:
                tasks[f'task{task_idx+1}'].append(example_idx)
                break

    for task in tasks:
        tasks[task] = dataset.select(tasks[task])
    
    return tasks


def main(config):

    tokenizer = AutoTokenizer.from_pretrained(
        config['model_params']['model'], 
        trust_remote_code=config['model_params']['trust_remote_code']
    )
    model = LLM(
        **config['model_params'], 
        seed=config['seed'],
        task='generate'
    )
    sampling_params = SamplingParams(
        **config['sampling_params'], 
        seed=config['seed']
    )

    for split in ['test', 'train']:
        print('\n\n*****')
        print(split)
        print('*****')

        dataset = load_dataset(config['dataset'], split=config[split]['split'])

        if config[split]['size'] != -1:
            dataset = dataset.shuffle(seed=config['seed'])
            dataset = dataset.select(range(config[split]['size']))

        dataset = config['dataset_preprocess_func'](dataset)
        assert set(['question', 'solution', 'answer']).issubset(dataset.column_names), 'Every dataset needs to have question, solution, answer columns'

        prompts = [
            tokenizer.apply_chat_template(
                config['chat_template_func'](**example), 
                tokenize=False, 
                continue_final_message=True
            )
            for example in dataset
        ]
        outputs = model.generate(prompts, sampling_params)
        outputs = [
            [completion_output.text for completion_output in request_output.outputs]
            for request_output in outputs
        ]

        is_correct = [
            [
                config['correctness_func'](completion_output, dataset['answer'][request_idx]) 
                for completion_output in request_output
            ]
            for request_idx, request_output in enumerate(outputs)
        ]
        difficulty = [sampling_params.n-sum(item) for item in is_correct]
        dataset = dataset.add_column('difficulty', difficulty)

        for task_name, dataset in split_into_tasks(dataset, config['num_splits']).items():
            dataset.to_json(os.path.join(config['save_path'], task_name, split+'.jsonl'))

    
if __name__ == '__main__':

    config = {

        'dataset' : 'deepmind/aqua_rat',
        
        'save_path' : 'datasets/aqua',

        'seed' : 42,

        'train' : {
            'split' : 'train', # split on hf
            'size' : 5000
        },
        'test' : {
            'split' : 'test', # split on hf
            'size' : -1
        },

        'dataset_preprocess_func' : preprocess_aqua,

        'chat_template_func' : chat_template_aqua,

        'model_params' : {
            'model' : 'Qwen/Qwen2.5-3B',
            'trust_remote_code' : True,
            'tensor_parallel_size' : 2,  # num gpus
            'dtype' : 'bfloat16',
            'gpu_memory_utilization' : 0.9,
            'max_model_len' : 1024,
        },

        'sampling_params' : {
            'n' : 20,  # max difficulty level
            'temperature' : 0.8,
            'max_tokens' : 512,
            'min_tokens' : 1
        },

        'correctness_func' : is_correct_aqua,

        'num_splits' : 4,

    }
    main(config)
