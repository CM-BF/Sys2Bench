from huggingface_hub import login
from transformers import AutoTokenizer, AutoModelForCausalLM
from datasets import load_dataset
from blocksworld_reward_model import BlocksWorldModel
import re
from trl import GRPOConfig, GRPOTrainer, get_peft_config, ModelConfig, PPOConfig
from peft import LoraConfig, get_peft_model
import os



data_files = ['data/blocksworld/train_set-2.json', 'data/blocksworld/train_set-4.json', 'data/blocksworld/train_set-6.json']

def prepare_dataset(data_files=data_files):
    dataset = load_dataset('json', data_files=data_files)
    # print(dataset)
    dataset = dataset['train'].shuffle(seed=1234).select(range(2500))
    return dataset

def generate_r1_prompt(tokenizer, init, goal, plan = ""):
    r1_prefix = [{
        "role": "system",
        "content": "You are a helpful assistant. You first thinks about the reasoning process in the mind and then provides the user with the answer."
      },
      { 
        "role": "user",
        "content": f"I am playing with a set of blocks where I need to arrange the blocks into stacks. Here are the actions I can do\n\nPick up a block\nUnstack a block from on top of another block\nPut down a block\nStack a block on top of another block\n\nI have the following restrictions on my actions:\nI can only pick up or unstack one block at a time.\nI can only pick up or unstack a block if my hand is empty.\nI can only pick up a block if the block is on the table and the block is clear. A block is clear if the block has no other blocks on top of it and if the block is not picked up.\nI can only unstack a block from on top of another block if the block I am unstacking was really on top of the other block.\nI can only unstack a block from on top of another block if the block I am unstacking is clear.\nOnce I pick up or unstack a block, I am holding the block.\nI can only put down a block that I am holding.\nI can only stack a block on top of another block if I am holding the block being stacked.\nI can only stack a block on top of another block if the block onto which I am stacking the block is clear.\nOnce I put down or stack a block, my hand becomes empty.\nHere is the format of the actions: \n\n <pick up the [block_name] block> \n <unstack the [block_name] block from on top of [another_block_name] block> \n <put down the [block_name] block> \n <stack the [block_name] block on top of the [another_block_name] block> \n\n Here is the initial state of the blocks: \n{init}\n\nHere is the goal state of the blocks:\n{goal}. Show your work in the <think> </think> tags. Return the final answer in the <plan> </plan> tags, for example: <plan>\npick up the blue block\nstack the blue block on top of the yellow block\npick up the orange block\nstack the orange block on top of the red block</plan>."
      },
      {
        "role": "assistant",
        "content": "Let me solve this step by step.\n<think>"
      }
    ]
    return {"prompt": tokenizer.apply_chat_template(r1_prefix, tokenize=False, continue_final_message=True), "plan": plan, "init": init, "goal": goal}

def reward_fn_wrapper(completions, plan, init, goal, **kwargs):
    rewards = []
    for completion, plan_i, init_i, goal_i in zip(completions, plan, init, goal):
        try:
            print('#########################')
            completion = "<think>" + completion
            
            matches = re.findall(r"<plan>(.*?)</plan>", completion, flags=re.DOTALL | re.IGNORECASE)
            if matches is None or len(matches) != 1:
                print("No match found")
                rewards.append(0.0)
                continue
            non_empty = [match.strip() for match in matches if match.strip()] # Ideally, we should have only one match
            extracted_plan = non_empty[0]
            instance_example = BlocksWorldModel(init_i, goal_i, extracted_plan)
            reward = instance_example.simulate_plan_with_reward()
            rewards.append(reward)
            print(reward)
            print(init_i)
            print(goal_i)
            print('-----')
            print(completion)
            print('-----')
        except Exception as e:
            print(e)
            rewards.append(0.0)
            
    return rewards
                            
"""
Pick up D from B
Unstack D from B
Stack D on A
Pick up C
Stack C on B
Pick up B
Stack B on C


We start from the initial state: A on C, D on B, C on table, B on table. We want D on A and C on B.
"""

def main():
    hf_token = os.environ.get("hf_token")
    login(token=hf_token, add_to_git_credential=True) # ADD YOUR TOKEN HERE
    
    # Model config
    # model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-3B-Instruct", torch_dtype="bfloat16")
    model_config = ModelConfig(
        model_name_or_path="Qwen/Qwen2.5-3B-Instruct",
        torch_dtype="bfloat16",
        attn_implementation="flash_attention_2",
        # use_peft=True,
        # load_in_4bit=True,
        lora_task_type="CAUSAL_LM",
        lora_r=32,
        lora_alpha=64,
        lora_dropout=0.1,
        lora_target_modules=["q_proj", "v_proj"],
    )
    # lora_config = LoraConfig(
    #     r=32,
    #     lora_alpha=64,
    #     target_modules=["q_proj", "v_proj"],
    #     lora_dropout=0.1,
    #     task_type="CAUSAL_LM",
    # )
    # model = get_peft_model(model, lora_config)
    # model.print_trainable_parameters()
    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-3B-Instruct")
    
    # Format the dataset
    dataset = prepare_dataset()
    dataset = dataset.map(lambda example: generate_r1_prompt(tokenizer, example["init"], example["goal"], example["plan"]))
    train_test_split = dataset.train_test_split(test_size=0.1)
    train_dataset = train_test_split["train"]
    test_dataset = train_test_split["test"]
    
    # Hyperparameters
    
    training_args = GRPOConfig(
        output_dir="qwen-bw-r1-aha-moment",
        learning_rate=1e-5,
        lr_scheduler_type="cosine",
        logging_steps=10,
        max_steps=250,
        per_device_train_batch_size=1,
        gradient_accumulation_steps=16,
        # gradient_checkpointing=True,
        # gradient_checkpointing_kwargs={"use_reentrant": False},
        bf16=True,
        # GRPO specific parameters
        max_prompt_length=256,
        max_completion_length=1024, # max length of the generated output for our solution
        num_generations=4,
        beta=0.001,
        # Vllm
        use_vllm=True,
        vllm_gpu_memory_utilization=0.2,
        # Reporting
        report_to=["tensorboard"],
        push_to_hub=True,
        save_strategy="steps",
        save_steps=10,   
    )
    trainer = GRPOTrainer(
        model=model_config.model_name_or_path,
        reward_funcs=[reward_fn_wrapper],
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=test_dataset,
        peft_config=get_peft_config(model_config),
    )
    
    trainer.train()
    trainer.save_model(training_args.output_dir)
    trainer.push_to_hub(dataset_name='bw-test')

if __name__ == "__main__":
    main()