from datasets import load_dataset, concatenate_datasets, DatasetDict
import numpy as np
import json
import os
from tqdm import tqdm
from vllm import LLM, SamplingParams
from transformers import AutoTokenizer
import re
from blocksworld_reward_model import BlocksWorldModel

def validate_bw_response_format(response: str):
    """Validate the blocksworld response format"""
    # Remove leading/trailing whitespace
    response = response.strip()

    # Rule 1: Must start with <think> and end with </plan>
    if not response.startswith("<think>") or not response.endswith("</answer>"):
        print('Response does not start with <think> or end with </answer>')
        return False

    # Rule 2: Must contain exactly one of each tag.
    if response.count("<think>") != 1 or response.count("</think>") != 1:
        print('Response does not contain exactly one of each think tag')
        return False
    if response.count("<answer>") != 1 or response.count("</answer>") != 1:
        print('Response does not contain exactly one of each answer tag')
        return False

    # Find indices for each tag.
    think_open = response.find("<think>")
    think_close = response.find("</think>")
    plan_open = response.find("<answer>")
    plan_close = response.find("</answer>")

    # Rule 4: The order should be: <think> ... </think> then <answer> ... </answer>
    if think_open != 0:  # Should start with <think>
        print('Response does not start with <think>')
        return False
    if think_close == -1 or plan_open == -1 or plan_close == -1:
        print('Response does not contain <answer> and </answer>, or </think>')
        return False
    if think_close > plan_open:
        print('Response has closing think tag after opening answer tag')
        return False  # The closing think tag must come before the opening plan tag

    # Rule 3: Check non-empty content between tags.
    think_content = response[len("<think>"):think_close].strip()
    plan_content = response[plan_open + len("<answer>"):plan_close].strip()

    if not think_content or not plan_content:
        return False

    return True

def generate_prompt(tokenizer, init, goal, plan="", example_index=0, icl_examples_set=None, example=None):
    """Generate prompt for the blocksworld model"""
    if icl_examples_set is None:
        icl_example = ""
    else:
        # icl_example = generate_icl(icl_examples_set, provide_think_icl=True, num_icl=1, idx=example_index)
        pass
    
    icl_example = "I am playing with a set of blocks where I need to arrange the blocks into stacks. Here are the actions I can do\n\nPick up a block\nUnstack a block from on top of another block\nPut down a block\nStack a block on top of another block\n\nI have the following restrictions on my actions:\nI can only pick up or unstack one block at a time.\nI can only pick up or unstack a block if my hand is empty.\nI can only pick up a block if the block is on the table and the block is clear. A block is clear if the block has no other blocks on top of it and if the block is not picked up.\nI can only unstack a block from on top of another block if the block I am unstacking was really on top of the other block.\nI can only unstack a block from on top of another block if the block I am unstacking is clear.\nOnce I pick up or unstack a block, I am holding the block.\nI can only put down a block that I am holding.\nI can only stack a block on top of another block if I am holding the block being stacked.\nI can only stack a block on top of another block if the block onto which I am stacking the block is clear.\nOnce I put down or stack a block, my hand becomes empty.\n\n[STATEMENT]\nAs initial conditions I have that, the red block is clear, the yellow block is clear, the hand is empty, the red block is on top of the blue block, the yellow block is on top of the orange block, the blue block is on the table and the orange block is on the table.\nMy goal is to have that the orange block is on top of the red block.\n\nMy plan is as follows:\n\n[PLAN]\nunstack the yellow block from on top of the orange block\nput down the yellow block\npick up the orange block\nstack the orange block on top of the red block\n[PLAN END]\n\n[STATEMENT]\nAs initial conditions I have that, the orange block is clear, the yellow block is clear, the hand is empty, the blue block is on top of the red block, the orange block is on top of the blue block, the red block is on the table and the yellow block is on the table.\nMy goal is to have that the blue block is on top of the red block and the yellow block is on top of the orange block.\n\nMy plan is as follows:\n\n[PLAN]\npick up the yellow block\nstack the yellow block on top of the orange block\n[PLAN END]\n\n[STATEMENT]\nAs initial conditions I have that, the red block is clear, the blue block is clear, the orange block is clear, the hand is empty, the blue block is on top of the yellow block, the red block is on the table, the orange block is on the table and the yellow block is on the table.\nMy goal is to have that the blue block is on top of the orange block and the yellow block is on top of the red block.\n\nMy plan is as follows:\n\n[PLAN]\nunstack the blue block from on top of the yellow block\nstack the blue block on top of the orange block\npick up the yellow block\nstack the yellow block on top of the red block\n[PLAN END]\n\n[STATEMENT]\nAs initial conditions I have that, the red block is clear, the blue block is clear, the yellow block is clear, the hand is empty, the yellow block is on top of the orange block, the red block is on the table, the blue block is on the table and the orange block is on the table.\nMy goal is to have that the orange block is on top of the blue block and the yellow block is on top of the red block.\n\nMy plan is as follows:\n\n[PLAN]\nunstack the yellow block from on top of the orange block\nstack the yellow block on top of the red block\npick up the orange block\nstack the orange block on top of the blue block\n[PLAN END]\n\n[STATEMENT]\n"

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. You first thinks about the reasoning process in the mind and then provides the user with the answer.\n"
        },
        {
            "role": "user",
            "content": f"I am playing with a set of blocks where I need to arrange the blocks into stacks. Here are the actions I can do\n\nPick up a block\nUnstack a block from on top of another block\nPut down a block\nStack a block on top of another block\n\nI have the following restrictions on my actions:\nI can only pick up or unstack one block at a time.\nI can only pick up or unstack a block if my hand is empty.\nI can only pick up a block if the block is on the table and the block is clear. A block is clear if the block has no other blocks on top of it and if the block is not picked up.\nI can only unstack a block from on top of another block if the block I am unstacking was really on top of the other block.\nI can only unstack a block from on top of another block if the block I am unstacking is clear.\nOnce I pick up or unstack a block, I am holding the block.\nI can only put down a block that I am holding.\nI can only stack a block on top of another block if I am holding the block being stacked.\nI can only stack a block on top of another block if the block onto which I am stacking the block is clear.\nOnce I put down or stack a block, my hand becomes empty.\nHere is the format of the actions: \n\npick up the [block_name] block # for example: pick up the blue block\nunstack the [block_name] block from on top of the [another_block_name] block # for example: unstack the orange block from on top of the black block\nput down the [block_name] block # for example put down the red block\nstack the [block_name] block on top of the [another_block_name] block # for example: stack the yellow block on top of the red block \n\n{icl_example}\n\n[Problem]\nHere is the initial state of the blocks: {init}\n\nHere is the goal state of the blocks: {goal}. Show your work in <think> </think> tags. After that, provide the final answer in <answer> </answer> tags, for example <answer>\nunstack the cyan block from on top of the emerald block\nput down the cyan block</answer>\n"
        },
        {
            "role": "assistant",
            "content": "Let me solve this step by step.\n<think>"
        }
    ]

    return {
        "prompt": tokenizer.apply_chat_template(messages, tokenize=False, continue_final_message=True),
        "plan": plan,
        "init": init,
        "goal": goal,
        "id": example['level_id'],
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

def blocksworld_reward_fn(completions, plan, init, goal, **kwargs):
    """Reward function for blocksworld task"""
    rewards = []
    for completion, plan_i, init_i, goal_i in zip(completions, plan, init, goal):
        reward_format = 0.0
        try:
            print('#########################')
            completion = "<think>" + completion
            print(completion)

            if not validate_bw_response_format(completion):
                print('Response Format Error')
                rewards.append(0.0)  # Penalty to avoid format errors
                continue
            else:
                reward_format = 1.0

            # Extract the plan
            matches = re.findall(r"<answer>(.*?)</answer>", completion, flags=re.DOTALL | re.IGNORECASE)
            if matches is None or len(matches) != 1:
                print("No plan found")
                rewards.append(0.0)
                continue

            # Process plan
            non_empty = [match.strip() for match in matches if
                         match.strip()]  # Ideally, we should have only one match
            extracted_plan = non_empty[0]

            # Calculate reward
            instance_example = BlocksWorldModel(init_i, goal_i, extracted_plan)
            reward = instance_example.simulate_plan_with_reward(true_plan=plan_i) + reward_format
            rewards.append(reward)
            print('-----')
            print(reward)
            print(init_i)
            print(goal_i)
            print('-----')
            print('#########################')
        except Exception as e:
            print(e)
            rewards.append(0.0)

    return rewards

def calculate_rating(example, model, sampling_params):
        outputs = model.generate(example['prompt'], sampling_params)
        outputs = [
            completion_output.text
            for request_output in outputs
            for completion_output in request_output.outputs
        ]
        breakpoint()

        ratings = blocksworld_reward_fn(outputs, example['plan'], example['init'], example['goal'])
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

        with open('bw/correctness.log', 'a') as f:
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

    root = "blocksworld"
    parts = []
    levels = [1, 2, 3, 4, 6]
    for n in levels:
        fname = f"train_set-{n}-all.json"
        path = os.path.join(root, fname)
        ds = load_dataset("json", data_files={"train": path})["train"]
        ds = ds.map(lambda ex, id=n: {**ex, "level_id": id})
        parts.append(ds)

    if not parts:
        raise FileNotFoundError(f"No train_set files found in {root}")
    data = concatenate_datasets(parts)
    breakpoint()

    # data = DatasetDict({
    #     "train": concatenate_datasets(splits["train"]),
    #     "test":  concatenate_datasets(splits["test"])
    # })

    tokenizer = AutoTokenizer.from_pretrained(
        base_model,
        trust_remote_code=True,
    )

    model = LLM(
        model=base_model,
        dtype= "bfloat16",
        gpu_memory_utilization=0.5,
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


    for example in tqdm(data, total=len(data)):
        # prompt = generate_prompt(
        #     tokenizer,
        #     example,
        #     use_icl=False
        # )
        prompt = generate_prompt(
            tokenizer,
            example['init'],
            example['goal'],
            plan=example['plan'],
            example_index=0,
            icl_examples_set=None,
            example=example
        )
        breakpoint()
        rating = calculate_rating(prompt, model, sampling_params)
        # breakpoint()
        full_ratings.append(rating)

    # Save the aggregated ratings to a file
    with open('bw/summary.json', 'w') as f:
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

    for i, example in tqdm(enumerate(data), total=len(data)):
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

    output_dir = "bw/splits"
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
