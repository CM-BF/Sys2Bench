from datasets import load_dataset, concatenate_datasets, DatasetDict
import numpy as np
import json
import os
from tqdm import tqdm
from vllm import LLM, SamplingParams
import torch
from transformers import AutoTokenizer
from math_utils import process_docs, process_result_v1, list_fewshot_samples
import re
from math import comb

def is_formatted(response: str):
    """Validate the response format"""
    response = response.strip()

    # Rule 1: Must start with <think> and end with </answer>
    if not response.startswith("<think>") or not response.endswith("</answer>"):
        return False, "Response does not start with <think> or end with </answer>"

    # Rule 2: Must contain exactly one of each tag.
    if response.count("<think>") != 1 or response.count("</think>") != 1:
        return False, 'Response does not contain exactly one of each think tag'
    if response.count("<answer>") != 1 or response.count("</answer>") != 1:
        return False, 'Response does not contain exactly one of each answer tag'

    # Find indices for each tag.
    think_open = response.find("<think>")
    think_close = response.find("</think>")
    plan_open = response.find("<answer>")
    plan_close = response.find("</answer>")

    # Rule 3: The order should be: <think> ... </think> then <answer> ... </answer>
    if think_open != 0:  # Should start with <think>
        return False, 'Response does not start with <think>'
    if think_close == -1 or plan_open == -1 or plan_close == -1:
        return False, 'Response does not contain <answer> and </answer>, or </think>'
    if think_close > plan_open:
        return False, 'Response has closing think tag after opening answer tag'

    # Rule 4: Check non-empty content between tags.
    think_content = response[len("<think>"):think_close].strip()
    plan_content = response[plan_open + len("<answer>"):plan_close].strip()
    if not think_content or not plan_content:
        return False, 'Empty content between tags'

    # Rule 5: Check <answer> immedietly follows </think>
    if not (response[think_close+len("</think>"):plan_open].strip() == ''):
        return False, 'There is content between </think> and <answer>'

    return True, 'Correctly Formatted'

def generate_prompt(tokenizer, example, use_icl = False):
    """Generate prompt for the arithmetic model"""

    example_1 = list_fewshot_samples()[0]
    example_2 = list_fewshot_samples()[1]
    question = example["problem"]
    sft = example["solution"]
    answer = example["answer"].strip()
    cot_prefix = "Solve the following math problem\n<question>\n\nShow your work in <think> </think> tags. And return the final answer in \\boxed{}, wrapped in <answer> </answer> tags, for example <answer>\\boxed{500}</answer>.\n"
    cot_prefix = cot_prefix.replace('<question>', example_1["problem"])
    cot_prefix += example_1["solution"] + "\n\n"

    cot_prefix1 = "Solve the following math problem\n<question>\n\nShow your work in <think> </think> tags. And return the final answer in \\boxed{}, wrapped in <answer> </answer> tags, for example <answer>\\boxed{500}</answer>.\n"
    cot_prefix1 = cot_prefix.replace('<question>', example_2["problem"])
    cot_prefix1 += example_2["solution"] + "\n\n"

    instruction = "Solve the following math problem\n<question>\n\nShow your work in <think> </think> tags. And return the final answer in \\boxed{}, wrapped in <answer> </answer> tags, for example <answer>\\boxed{500}</answer>."
    instruction = instruction.replace('<question>', question)
    
    instruction = cot_prefix + cot_prefix1 + instruction
    
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. You first thinks about the reasoning process in the mind and then provides the user with the answer.\n"
        },
        {
            "role": "user",
            "content": instruction
        },
        {
            "role": "assistant",
            "content": "Let me solve this step by step.\n<think>"
        }
    ]

    return {
        "prompt": tokenizer.apply_chat_template(messages, tokenize=False, continue_final_message=True),
        "sft" : sft,
        "answer": answer,
        "task" : example["problem"],
        "level" : example["level"],
        "id" : example["level_id"],
    }

def save_array_to_json(data, filename):
    """
    Saves the entire iterable of JSON-serializable items as one pretty-printed JSON array.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(
            list(data),  # make sure it's a list if data is a generator
            f,
            ensure_ascii=False,  # keep non-ASCII characters intact
            indent=4,  # pretty-print with 4-space indents
        )

def calculate_rating(example, model, sampling_params):
        outputs = model.generate(example['prompt'], sampling_params)
        outputs = [
            completion_output.text
            for request_output in outputs
            for completion_output in request_output.outputs
        ]
        
        def ans_extract(output):
            answer_match = re.findall(r'<answer>\s*(.*?)\s*</answer>', output, re.DOTALL)
            if len(answer_match) > 0:
                return answer_match[-1].strip()
            return None

        # breakpoint()
        
        ratings = []

        for output in outputs:
            rating = process_result_v1(
                example["answer"],
                output,
                answer_parser=ans_extract,
            )
            ratings.append(rating)
        correct_flags = [r > 0.5 for r in ratings]   

        first_correct    = correct_flags[0]
        num_correct_20   = sum(correct_flags[:20])
        acc_first20      = num_correct_20 / 20
        any_correct_20   = (num_correct_20 >= 1)

        n = len(correct_flags)
        pass_at_k = {}
        for k in [1,2,4,8,16,32,64,128,256]:
            if k <= n:
                pass_at_k[k] = sum(correct_flags[:k]) >= 1

        with open('math/correctness.log', 'a') as f:
            f.write(f"Example ID: {example['id']}\n")
            f.write(f"Ratings: {ratings}\n")
                    

        return {
            "first_correct":    first_correct,
            "accuracy20":       acc_first20,
            "any20":            any_correct_20,
            "pass@k":           pass_at_k,
        }
             


def main():
    base_model = "Qwen/Qwen2.5-1.5B"
    print("Loading codeforces dataset (main config)...")
    # data = datasets.load_dataset("open-r1/codeforces", split="train")
    # data = datasets.load_dataset('json', data_dir='math', split='train')

    root = "math"
    splits = {"train": [], "test": []}

    for level_dir in sorted(os.listdir(root)):
        if not level_dir.startswith("level_"):
            continue
        level_num = int(level_dir.split("_", 1)[1])

        for split in ("train", "test"):
            path = os.path.join(root, level_dir, f"{split}.json")
            ds = load_dataset("json", data_files={split: path})[split]
            ds = ds
            ds = ds.map(lambda example: {
                "level": level_dir,
                "level_id": level_num 
            })
            splits[split].append(ds)

    data = DatasetDict({
        "train": concatenate_datasets(splits["train"]),
        "test":  concatenate_datasets(splits["test"])
    })
    
    data["train"] = process_docs(data["train"])
    data["test"] = process_docs(data["test"])

    tokenizer = AutoTokenizer.from_pretrained(
        base_model,
        trust_remote_code=True,
    )

    model = LLM(
        model=base_model,
        dtype= "bfloat16",
        gpu_memory_utilization=0.2,
        max_model_len=3200,
        task='generate'
    )
    

    sampling_params = SamplingParams(
        n=256,
        temperature=0.7,
        max_tokens=1600,
        min_tokens=1,
        stop=["</answer>"],
        include_stop_str_in_output=True
    )

    full_ratings = []


    for example in tqdm(data['train'], total=len(data['train'])):
        prompt = generate_prompt(
            tokenizer,
            example,
            use_icl=False
        )
        rating = calculate_rating(prompt, model, sampling_params)
        # breakpoint()
        full_ratings.append(rating)

    # Save the aggregated ratings to a file
    with open('math/summary.json', 'w') as f:
        avg_acc = sum([r["accuracy20"] for r in full_ratings]) / len(full_ratings)
        avg_first = sum([r["first_correct"] for r in full_ratings]) / len(full_ratings)
        avg_any = sum([r["any20"] for r in full_ratings]) / len(full_ratings)
        avg_pass = {}
        for k in [1,2,4,8,16,32,64,128,256]:
            avg_pass[k] = sum([r["pass@k"][k] for r in full_ratings]) / len(full_ratings)
        json.dump({
            "accuracy20": avg_acc,
            "first_correct": avg_first,
            "any20": avg_any,
            "pass@k": avg_pass
        }, f, indent=4)


    ratings = [full_rating["accuracy20"] for full_rating in full_ratings]
    ratings = np.array(ratings)
    q1 = np.quantile(ratings, 1 / 5)
    q2 = np.quantile(ratings, 2 / 5)
    q3 = np.quantile(ratings, 3 / 5)
    q4 = np.quantile(ratings, 4 / 5)

    level_1 = []
    level_2 = []
    level_3 = []
    level_4 = []
    level_5 = []

    print("Splitting dataset...")

    for i, example in tqdm(enumerate(data['train']), total=len(data['train'])):
        # breakpoint()
        rating = full_ratings[i]
        example = example.copy()
        example["accuracy20"] = rating["accuracy20"]
        example["first_correct"] = rating["first_correct"]
        example["any20"] = rating["any20"]
        example["pass@k"] = rating["pass@k"]
        if rating["accuracy20"] >= q4:
            level_1.append(example)
        elif rating["accuracy20"] >= q3:
            level_2.append(example)
        elif rating["accuracy20"] >= q2:
            level_3.append(example)
        elif rating["accuracy20"] >= q1:
            level_4.append(example)
        else:
            level_5.append(example)



    print(
        f"Split sizes: Trivial={len(level_1)} Easy={len(level_2)}, Medium={len(level_3)}, Hard={len(level_4)}, Extra={len(level_5)}"
    )

    output_dir = "math/splits"
    os.makedirs(output_dir, exist_ok=True)

    print(f"Saving splits to '{output_dir}' directory...")
    save_array_to_json(level_1, os.path.join(output_dir, "level_1.json"))
    save_array_to_json(level_2, os.path.join(output_dir, "level_2.json"))
    save_array_to_json(level_3, os.path.join(output_dir, "level_3.json"))
    save_array_to_json(level_4, os.path.join(output_dir, "level_4.json"))
    save_array_to_json(level_5, os.path.join(output_dir, "level_5.json"))

    print("Splitting complete.")


if __name__ == "__main__":
    main()
