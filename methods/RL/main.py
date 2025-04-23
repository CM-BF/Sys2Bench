import os
import sys
from typing import Union

sys.path.append(os.environ['ROOT_PATH'])
import re
import time
import json
from datetime import datetime
from pathlib import Path
from tqdm import tqdm
from collections import Counter
import hydra
from hydra.core.hydra_config import HydraConfig
import torch
from omegaconf import DictConfig, OmegaConf
from datasets import load_dataset, concatenate_datasets, Dataset
from huggingface_hub import login
from transformers import AutoTokenizer, AutoModelForCausalLM
from trl import GRPOConfig, GRPOTrainer, PPOConfig, PPOTrainer, get_peft_config, ModelConfig
import datasets

# Task-specific imports
from blocksworld_reward_model import BlocksWorldModel
from utils import generate_icl, sc_output_extractor
from reasoners.benchmark import BWEvaluator
from reasoners.lm import HFModel
import numpy as np
# For countdown task
import random
from countdown_reward_model import CountdownRewardModel
import math
from functools import partial
# For Arithmetic Tasks
from gsm8k_reward_model import GSM8KRewardModel
import logging
from accelerate import Accelerator
from vllm import LLM, SamplingParams

log = logging.getLogger(__name__)
OmegaConf.register_new_resolver("d2s", lambda digit, sub: str(digit).replace(".", "_"))


accelerator = Accelerator()
def log_on_main(text):
    if accelerator.is_main_process:
        log.info(text)


def cosine_schedule(t, T, num_tasks):
    total = num_tasks * (num_tasks + 1) / 2.0
    early = {i: (num_tasks - i)/ total for i in range(num_tasks)}
    late = {i: (i + 1) / total for i in range(num_tasks)}
    alpha = 0.5 * (1 + math.cos(math.pi * t / T))
    probs = {i: alpha * early[i] + (1 - alpha) * late[i] for i in range(num_tasks)}
    # Enforce symmetric floor equal to the minimum probability in early/late.
    p_min = 2 / (num_tasks * (num_tasks + 1))
    for i in range(num_tasks):
        probs[i] = max(probs[i], p_min)
    norm = sum(probs.values())
    return {i: probs[i] / norm for i in probs}


class CosineTaskSampler(torch.utils.data.Sampler):
    def __init__(self, dataset, num_tasks, total_iterations, batch_size, seed=0):
        """
        Args:
          dataset: a HF dataset; each sample is assumed to be a dict including "task" (an integer 0 to num_tasks-1)
          num_tasks: total number of task categories (e.g. 4)
          total_iterations: total training iterations (T)
          current_iter_fn: callable that returns current iteration (t)
        """
        self.dataset = dataset
        self.batch_size = batch_size
        self.max_dataset_len = len(self.dataset)
        self.num_tasks = num_tasks
        self.total_iterations = total_iterations
        self.indices_by_task = {i: [] for i in range(num_tasks)}
        for idx, sample in enumerate(self.dataset):
            task = sample.get("task", 0)
            self.indices_by_task[task].append(idx)
            
        # for idx in range(4):
        #     print(f"Task {idx}: {len(self.indices_by_task[idx])}")
        # quit()
    
    def __iter__(self):
        
        for i in range(self.total_iterations):
            probs_dict = cosine_schedule(i, self.total_iterations, self.num_tasks)
            
            probs = np.array([probs_dict[j] for j in range(self.num_tasks)])
            print(f'For iter {i}, probs = {probs}')
            # Sample a task for each slot in the batch using the probabilities.
            chosen_tasks = np.random.choice(np.arange(self.num_tasks), size=self.batch_size, p=probs, replace=True)
            batch_indices = []
            
            for task in chosen_tasks:
                indices = self.indices_by_task[task]
                
                if len(indices) == 0:
                    idx = random.randrange(len(self.dataset))
                else:
                    idx = random.choice(indices)
                batch_indices.append(int(idx))
            print(f"Iteration {i}: Batch indices: {batch_indices}: Task Difficulties: {chosen_tasks}")
            yield from batch_indices
        
        # indices_by_task = {i: [] for i in range(self.num_tasks)}
        # for idx, sample in enumerate(self.dataset):
        #     task = sample.get("task", 0)
        #     indices_by_task[task].append(idx)
        
        # t = self.current_iter_fn()
        # probs = cosine_schedule(t, self.total_iterations, self.num_tasks)
        # print(f'For iter {t}, probs = {probs}')
        # sampled_indices = []
        # for task, indices in indices_by_task.items():
        #     if not indices:
        #         continue
        #     # Determine sample count; here we simply use a proportion of available indices.
        #     count = max(1, int(len(indices) * probs[task]))
        #     # count = min(count, len(indices))
        #     count = min(int(self.max_dataset_len * probs[task]), count)
        #     sampled_indices.extend(random.sample(indices, count))
        # random.shuffle(sampled_indices)
        # print('Sampled indices:', len(sampled_indices), len(self.dataset))
        # if t%2 == 0 and t > 0:
        #     print('Sampled indices:', len(sampled_indices))
        #     quit()
        # return iter(sampled_indices)

    def __len__(self):
        return self.total_iterations * self.batch_size


class CosineGRPOTrainer(GRPOTrainer):
    def __init__(self, num_tasks=4, total_iterations=1200, *args, **kwargs):
        self.num_tasks = num_tasks
        self.total_iterations = total_iterations
        super().__init__(*args, **kwargs)
    
    def _get_train_sampler(self):
        batch_size = int(self.args.per_device_train_batch_size * self.args.gradient_accumulation_steps)
        return CosineTaskSampler(self.train_dataset,
                                 num_tasks = self.num_tasks, 
                                 total_iterations = self.total_iterations, 
                                #  current_iter_fn= lambda: self.state.global_step,
                                 batch_size = batch_size)
    
    def training_step(self, *args, **kwargs):
        return super().training_step(*args, **kwargs)


class TaskSampler(torch.utils.data.Sampler):
    def __init__(self, dataset, num_tasks, total_iterations, data_schedule, batch_size, scheduler_params, seed=0):
        """
        Args:
          dataset: a HF dataset; each sample is assumed to be a dict including "task" (an integer 0 to num_tasks-1)
          num_tasks: total number of task categories (e.g. 4)
          total_iterations: total training iterations (T)
          current_iter_fn: callable that returns current iteration (t)
        """
        self.dataset = dataset
        self.batch_size = batch_size
        self.max_dataset_len = len(self.dataset)
        self.num_tasks = num_tasks
        self.total_iterations = total_iterations
        self.indices_by_task = {task_idx: (np.array(self.dataset['task']) == task_idx).nonzero()[0].tolist() for task_idx in range(num_tasks)}
        schedule_funcs = {
            'balanced': self._balanced_schedule,
            'cosine': self._cosine_schedule,
            'gaussian': partial(self._gaussian_schedule, **scheduler_params),
            'classic': self._step_schedule
        }
        log_on_main(f"Data Schedule: {data_schedule}")
        self.schedule_func = schedule_funcs[data_schedule]
    
    # Classical Curriculum Learning
    @staticmethod    
    def _step_schedule(t, T, num_tasks):
        active_task = min(int(t * num_tasks / T), num_tasks - 1)
        return dict(enumerate(np.eye(num_tasks)[active_task].tolist()))

    def __iter__(self):

        for i in range(self.total_iterations):
            probs_dict = self.schedule_func(i, self.total_iterations, self.num_tasks)

            probs = np.array([probs_dict[j] for j in range(self.num_tasks)])
            # Sample a task for each slot in the batch using the probabilities.
            chosen_tasks = np.random.choice(np.arange(self.num_tasks), size=self.batch_size, p=probs, replace=True)
            batch_indices = []

            for task in chosen_tasks:
                indices = self.indices_by_task[task]

                if len(indices) == 0:
                    idx = random.randrange(len(self.dataset))
                else:
                    idx = random.choice(indices)
                batch_indices.append(int(idx))
            log_on_main(f"Iteration {i}: Probs = {probs} Batch indices = {batch_indices} Task Difficulties = {chosen_tasks}")
            yield from batch_indices

    def __len__(self):
        return self.total_iterations * self.batch_size

    @staticmethod
    def _balanced_schedule(t, T, num_tasks):
        return {i: 1. / num_tasks for i in range(num_tasks)}

    @staticmethod
    def _cosine_schedule(t, T, num_tasks):
        total = num_tasks * (num_tasks + 1) / 2.0
        early = {i: (num_tasks - i) / total for i in range(num_tasks)}
        late = {i: (i + 1) / total for i in range(num_tasks)}
        alpha = 0.5 * (1 + math.cos(math.pi * t / T))
        probs = {i: alpha * early[i] + (1 - alpha) * late[i] for i in range(num_tasks)}
        # Enforce symmetric floor equal to the minimum probability in early/late.
        p_min = 2 / (num_tasks * (num_tasks + 1))
        for i in range(num_tasks):
            probs[i] = max(probs[i], p_min)
        norm = sum(probs.values())
        return {i: probs[i] / norm for i in probs}

    @staticmethod
    def _gaussian_schedule(t, T, num_tasks, mu_exp, sigma, min_prob: Union[bool, float]=False):
        '''
        Gaussian schedule for task sampling.
        mu_exp: exponent for the mean, typically 1.0. Move faster at the beginning: < 1.0. Move slower at the beginning: > 1.0
        sigma: standard deviation of the Gaussian distribution
        min_prob: minimum probability for each task
        '''
        # Move mean from 0 to (num_tasks-1) as time progresses, Use sqrt(t / T) to boost the the speed at the beginning
        mu = (t / T) ** mu_exp * (num_tasks - 1)
        p_min = (2 / (num_tasks * (num_tasks + 1))) if (min_prob is True) else (min_prob if isinstance(min_prob, float) else None)
        if p_min is None: raise ValueError("min_prob should be either a boolean or a float")
        if num_tasks * p_min > 1: raise ValueError("num_tasks * p_min must not exceed 1")
        
        # Compute normalized Gaussian probabilities.
        base = [math.exp(-((i - mu) ** 2) / (2 * sigma ** 2)) for i in range(num_tasks)]
        total = sum(base)
        q = [b / total for b in base]
        
        # Mix with uniform floor to guarantee each probability is at least p_min.
        return {i: p_min + (1 - num_tasks * p_min) * q_i for i, q_i in enumerate(q)}

        # Calculate unnormalized probabilities using Gaussian PDF
        # unnormalized_probs = {}
        # for i in range(num_tasks):
        #     # Calculate PDF of Gaussian for task i
        #     exponent = -((i - mu) ** 2) / (2 * sigma ** 2)
        #     unnormalized_probs[i] = math.exp(exponent)
        #     unnormalized_probs[i] = max(unnormalized_probs[i], p_min)

        # total = sum(unnormalized_probs.values())
        # return {i: prob / total for i, prob in unnormalized_probs.items()}


class CurriculumGRPOTrainer(GRPOTrainer):
    def __init__(self, num_tasks=4, total_iterations=1200, data_schedule='balanced', scheduler_params: dict=None, *args, **kwargs):
        self.num_tasks = num_tasks
        self.total_iterations = total_iterations
        self.data_schedule = data_schedule
        self.scheduler_params=scheduler_params
        super().__init__(*args, **kwargs)

    def _get_train_sampler(self):
        batch_size = int(self.args.per_device_train_batch_size * self.args.gradient_accumulation_steps)
        return TaskSampler(self.train_dataset,
                           num_tasks=self.num_tasks,
                           total_iterations=self.total_iterations,
                           data_schedule=self.data_schedule,
                           scheduler_params=self.scheduler_params,
                           batch_size=batch_size)

    def training_step(self, *args, **kwargs):
        return super().training_step(*args, **kwargs)

# class Cosine

class BaseTrainer:
    """Base class for training and inference with Hydra configuration"""

    def __init__(self, cfg: DictConfig):
        self.cfg = cfg
        # Setting up paths
        self.output_dir = Path(HydraConfig.get().run.dir)  # Hydra changes working directory

        # Save the config for reproducibility
        with open(self.output_dir / "config_dump.yaml", "w") as f:
            f.write(OmegaConf.to_yaml(cfg))

        root_path = Path(os.environ['ROOT_PATH'])
        os.chdir(root_path)
        print(f"Working directory: {root_path}")
        print(f"Output directory: {self.output_dir}")

        # Setup HuggingFace authentication
        # Setup HuggingFace authentication
        hf_token = self.cfg.experiment.hf_token
        # Check if already logged in using huggingface_hub API
        from huggingface_hub import HfApi
        try:
            # Try to get user info which will fail if not logged in
            api = HfApi()
            user_info = api.whoami()
            print(f"Already logged in to Hugging Face as {user_info['name']}")
        except Exception as e:
            print("Logging in to Hugging Face")
            login(token=hf_token, add_to_git_credential=True)

        self.last_log_time = None

    def train(self):
        """Train a model"""
        raise NotImplementedError("Train method must be implemented by subclasses")

    def inference(self):
        """Run inference"""
        raise NotImplementedError("Inference method must be implemented by subclasses")

    def _get_model_config(self):
        """Create model configuration"""
        lora_config = self.cfg.lora

        model_config = ModelConfig(
            model_name_or_path=self.cfg.model.name,
            torch_dtype=self.cfg.model.torch_dtype,
            attn_implementation=self.cfg.model.attn_implementation,
            lora_task_type=lora_config.task_type,
            lora_r=lora_config.r,
            lora_alpha=lora_config.alpha,
            lora_dropout=lora_config.dropout,
            lora_target_modules=list(lora_config.target_modules),
        )

        return model_config

    def _get_checkpoint_path(self, checkpoint, model_name=None):
        """Generate the path to the checkpoint based on configuration"""
        # Get the base output directory for models from config
        base_output_dir = self.cfg.output.root_path

        # Use the model name from output config
        model_name = self.cfg.output.run_name if model_name is None else model_name

        # If the checkpoint is a number, use the checkpoint-{num} format
        if isinstance(checkpoint, int):
            checkpoint_path = os.path.join(base_output_dir, "outputs", model_name,
                                           f"checkpoint-{checkpoint}")
        else:
            # Otherwise use the provided checkpoint path directly
            checkpoint_path = checkpoint

        # Ensure the checkpoint exists
        if not os.path.exists(checkpoint_path):
            import warnings

            checkpoint_path = f'{self.cfg.model.family}/{model_name}'
            warnings.warn(f"Checkpoint not found at {checkpoint_path}. Will attempt to use the model in huggingface: {checkpoint_path}.")

        return checkpoint_path

    def _get_common_training_args(self):
        """Get common training arguments for both GRPO and PPO"""
        training_cfg = self.cfg.algorithm.training
        output_dir = self.output_dir

        common_args = {
            "learning_rate": training_cfg.learning_rate,
            "lr_scheduler_type": training_cfg.lr_scheduler_type,
            "logging_steps": training_cfg.logging_steps,
            "max_steps": training_cfg.max_steps * len(self.cfg.task.data_files) if training_cfg.curriculum else training_cfg.max_steps,
            "per_device_train_batch_size": training_cfg.per_device_train_batch_size,
            "gradient_accumulation_steps": training_cfg.gradient_accumulation_steps,
            "gradient_checkpointing": training_cfg.gradient_checkpointing,
            "bf16": training_cfg.bf16,
            "report_to": list(training_cfg.report_to),
            "push_to_hub": training_cfg.push_to_hub,
            "save_strategy": training_cfg.save_strategy,
            "save_steps": training_cfg.save_steps,
            "tf32": training_cfg.tf32,
            "output_dir": str(output_dir),
            "run_name": self.cfg.output.run_name,
            "hub_model_id": self.cfg.output.run_name,
            "seed": self.cfg.experiment.dataset_seed,
            "logging_dir": str(output_dir),
            "eval_strategy": "no",
            "accelerator_config": {'split_batches': True}
        }

        return common_args, output_dir

    def _setup_grpo_training(self):
        """Setup training configuration for GRPO"""
        training_cfg = self.cfg.algorithm.training
        common_args, _ = self._get_common_training_args()

        # Add GRPO specific parameters
        grpo_args = {
            # GRPO specific parameters
            "max_prompt_length": self.cfg.task.training.max_prompt_length,
            "max_completion_length": self.cfg.task.training.max_completion_length,
            "num_generations": training_cfg.num_generations,
            "beta": training_cfg.beta,
            # Vllm
            "use_vllm": training_cfg.use_vllm,
            "vllm_gpu_memory_utilization": training_cfg.vllm_gpu_memory_utilization,
        }

        # Combine common and GRPO specific args
        training_args = GRPOConfig(**common_args, **grpo_args)

        return training_args

    def _setup_ppo_training(self):
        """Setup training configuration for PPO"""
        training_cfg = self.cfg.algorithm.training
        common_args, _ = self._get_common_training_args()

        # Add PPO specific parameters
        ppo_args = {
            # PPO specific parameters
            "num_ppo_epochs": training_cfg.num_ppo_epochs,
            "kl_coef": training_cfg.kl_coef,
            "cliprange": training_cfg.cliprange,
            "vf_coef": training_cfg.vf_coef,
            "cliprange_value": training_cfg.cliprange_value,
            "gamma": training_cfg.gamma,
            "lam": training_cfg.lam,
            "whiten_rewards": training_cfg.whiten_rewards,
        }

        # Combine common and PPO specific args
        training_args = PPOConfig(**common_args, **ppo_args)

        return training_args


class BlocksWorldTrainer(BaseTrainer):
    """Class for training and inference on blocksworld models"""

    def _prepare_dataset(self):
        """Prepare dataset for training"""
        # If a dataset size limit is specified, sample equally from each file
        all_samples = []
        data_files = self.cfg.task.data_files
        data_schedule = self.cfg.algorithm.training.curriculum_schedule
        for task_idx, file in enumerate(data_files):
            file_dataset = load_dataset('json', data_files=file)['train']
            file_dataset = file_dataset.shuffle(seed=self.cfg.experiment.dataset_seed)
            
            # if self.cfg.experiment.dataset_size > 0 and data_schedule == 'fixed':
            #     num_files = len(data_files)
            #     samples_per_file = self.cfg.experiment.dataset_size // num_files
            #     num_samples = min(len(file_dataset), samples_per_file)
            #     file_dataset = file_dataset.select(range(num_samples))
            
            # Annotate with difficulty
            task_annotations = [task_idx] * len(file_dataset)
            file_dataset = file_dataset.add_column("task", task_annotations)
            
            all_samples.extend(file_dataset)
        dataset = Dataset.from_list(all_samples)

        # if self.cfg.experiment.dataset_size > 0:
        #     data_files = self.cfg.task.data_files
        #     num_files = len(data_files)
        #     samples_per_file = self.cfg.experiment.dataset_size // num_files

        #     all_samples = []
        #     for file in data_files:
        #         # Load and shuffle the dataset for this file
        #         file_dataset = load_dataset('json', data_files=file)['train']
        #         file_dataset = file_dataset.shuffle(seed=self.cfg.experiment.dataset_seed)
        #         # Select up to samples_per_file from this file (or all if fewer available)
        #         num_samples = min(len(file_dataset), samples_per_file)
        #         file_samples = file_dataset.select(range(num_samples))
        #         all_samples.extend(file_samples)
            
        #     # Convert the collected samples into a HuggingFace Dataset and shuffle the final list
        #     dataset = Dataset.from_list(all_samples)
        #     # dataset = Dataset.from_list(all_samples)
        #     # dataset = Dataset.from_list(all_samples)
        # else:
        #     # Load the entire dataset and shuffle if no size limit is provided
        #     dataset = load_dataset('json', data_files=self.cfg.task.data_files)['train']
        #     dataset = dataset.shuffle(seed=self.cfg.experiment.dataset_seed)
        
        # Final shuffle for randomness
        dataset = dataset.shuffle(seed=self.cfg.experiment.dataset_seed)
        print(f"Dataset prepared with {len(dataset)} samples")
        return dataset

    def _generate_prompt(self, tokenizer, init, goal, plan="", example_index=0, icl_examples_set=None):
        """Generate prompt for the blocksworld model"""
        if icl_examples_set is None:
            icl_example = ""
        else:
            icl_example = generate_icl(icl_examples_set, provide_think_icl=True, num_icl=1, idx=example_index)

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
            "goal": goal
        }

    def _validate_bw_response_format(self, response: str):
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

    def _blocksworld_reward_fn(self, completions, plan, init, goal, **kwargs):
        """Reward function for blocksworld task"""
        rewards = []
        for completion, plan_i, init_i, goal_i in zip(completions, plan, init, goal):
            reward_format = 0.0
            try:
                print('#########################')
                completion = "<think>" + completion
                print(completion)

                if not self._validate_bw_response_format(completion):
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

    def train(self):
        """Train a model using the specified algorithm with configurations from Hydra"""
        # Extract config values
        model_name = self.cfg.model.name
        use_icl_examples = self.cfg.task.use_icl_examples
        output_model_name = self.cfg.output.run_name
        algorithm = self.cfg.algorithm.name

        # Prepare ICL examples if needed
        icl_examples = None
        if use_icl_examples:
            with open(self.cfg.task.icl_examples_file) as f:
                icl_examples = json.load(f)

        # Load tokenizer and model
        model_config = self._get_model_config()
        tokenizer = AutoTokenizer.from_pretrained(
            model_config.model_name_or_path,
            trust_remote_code=model_config.trust_remote_code
        )
        model = AutoModelForCausalLM.from_pretrained(
            model_config.model_name_or_path,
            torch_dtype=model_config.torch_dtype,
            trust_remote_code=model_config.trust_remote_code,
            attn_implementation=model_config.attn_implementation
        )
        peft_config = get_peft_config(model_config)

        # Prepare dataset
        dataset = self._prepare_dataset()
        dataset = dataset.map(
            lambda example, idx: self._generate_prompt(
                tokenizer,
                example["init"],
                example["goal"],
                example["plan"],
                idx,
                icl_examples
            ),
            with_indices=True
        )

        # Split dataset
        train_test_split = dataset.train_test_split(test_size=self.cfg.experiment.test_size)
        train_dataset = train_test_split["train"]
        test_dataset = train_test_split["test"]

        # Setup training arguments based on algorithm
        if 'grpo' in algorithm:
            training_args = self._setup_grpo_training()
            trainer = CurriculumGRPOTrainer(
                model=model,
                reward_funcs=self._blocksworld_reward_fn,
                args=training_args,
                train_dataset=train_dataset,
                eval_dataset=test_dataset,
                processing_class=tokenizer,
                peft_config=peft_config,
                num_tasks=len(self.cfg.task.data_files),
                total_iterations=training_args.max_steps,
                data_schedule=self.cfg.algorithm.training.curriculum_schedule,
                scheduler_params=self.cfg.algorithm.training.scheduler_params,
            )

        elif algorithm == "ppo":
            training_args = self._setup_ppo_training()
            trainer = PPOTrainer(
                model=model_config.model_name_or_path,
                ref_model=model_config.model_name_or_path,  # Same model as reference
                tokenizer=tokenizer,
                args=training_args,
                reward_fn=self._blocksworld_reward_fn,
                train_dataset=train_dataset,
                eval_dataset=test_dataset,
                peft_config=get_peft_config(model_config),
            )

        else:
            raise ValueError(f"Unsupported algorithm: {algorithm}")

        # Train model
        trainer.train()
        trainer.save_model(training_args.output_dir)

        if self.cfg.algorithm.training.push_to_hub:
            trainer.push_to_hub(dataset_name='blocksworld-dataset')

    def _train_ppo(self, trainer, dataset, tokenizer):
        """Custom training loop for PPO"""
        print("Starting PPO training loop for BlocksWorld task")

        # Use smaller subset during PPO training due to computational constraints
        if len(dataset) > 100:
            train_dataset = dataset.select(range(100))
        else:
            train_dataset = dataset

        for epoch in range(self.cfg.algorithm.training.max_steps):
            print(f"PPO Epoch {epoch}/{self.cfg.algorithm.training.max_steps}")

            # Sample batch of prompts
            # Sample batch of prompts - use the per_device_train_batch_size as batch size
            batch_indices = random.sample(range(len(train_dataset)),
                                          min(self.cfg.algorithm.training.per_device_train_batch_size,
                                              len(train_dataset)))
            batch = [train_dataset[i] for i in batch_indices]

            # Prepare inputs
            query_tensors = []
            for item in batch:
                input_ids = tokenizer(item["prompt"], return_tensors="pt").input_ids
                if hasattr(trainer, "accelerator"):
                    input_ids = input_ids.to(trainer.accelerator.device)
                query_tensors.append(input_ids)

            # Generate model responses
            response_tensors = []
            for query in query_tensors:
                response = trainer.generate(
                    query,
                    max_new_tokens=self.cfg.task.training.max_completion_length,
                    do_sample=True,
                    temperature=0.7
                )
                response_tensors.append(response)

            # Compute rewards
            rewards = []
            for i, (response, item) in enumerate(zip(response_tensors, batch)):
                # Decode the response
                response_text = tokenizer.decode(response[0], skip_special_tokens=True)

                # Extract the completion part (after "<think>")
                if "<think>" in response_text:
                    completion = response_text.split("<think>")[1]
                else:
                    completion = response_text

                # Compute reward using the blocksworld reward function
                reward = self._blocksworld_reward_fn(
                    [completion],
                    [item["plan"]],
                    [item["init"]],
                    [item["goal"]]
                )[0]

                rewards.append(reward)
                print(f"Sample {i}, Reward: {reward}")

            # Convert rewards to tensors
            reward_tensors = [torch.tensor(reward) for reward in rewards]

            # Perform PPO update
            stats = trainer.step(query_tensors, response_tensors, reward_tensors)

            # Log training progress
            if epoch % self.cfg.algorithm.training.logging_steps == 0:
                print(f"Epoch {epoch}: {stats}")

                # Save checkpoint
                if epoch % self.cfg.algorithm.training.save_steps == 0:
                    trainer.save_pretrained(f"{trainer.args.output_dir}/checkpoint-{epoch}")

    def inference(self):
        """Run inference using the trained model"""
        # Extract config values
        model_checkpoint = self.cfg.task.inference.checkpoint
        steps = self.cfg.task.inference.steps
        temperature = self.cfg.task.inference.temperature
        sc_num = self.cfg.task.inference.sc_num
        use_icl = self.cfg.task.inference.use_icl
        prompt_path = self.cfg.task.inference.prompt_path
        resume = self.cfg.task.inference.resume

        # Generate checkpoint path
        model_dir = self._get_checkpoint_path(model_checkpoint)

        # Setup data path
        data_path = self.cfg.task.inference.data_path.format(steps=steps)

        # Setup log directory
        model_name = model_dir.split('/')[-1]
        log_dir = f'logs/Blocksworld/RL/step_{steps}/{datetime.now().strftime("%m%d%Y-%H%M%S")}_{model_name}_t_{temperature}_sc_{sc_num}'

        # Load prompt
        with open(prompt_path) as f:
            prompt = json.load(f)

        # Prepare ICL examples if needed
        icl = ""
        if use_icl:
            with open(self.cfg.task.icl_examples_file) as f:
                icl_examples = json.load(f)
            icl = generate_icl(icl_examples, provide_think_icl=True, num_icl=self.cfg.task.inference.icl_num)
        print(f"ICL examples: {icl}")

        # Load model
        base_model = HFModel(
            model_pth=model_dir,
            tokenizer_pth=model_dir,
            max_new_tokens=self.cfg.task.inference.max_new_tokens
        )

        # Create reasoner
        reasoner = RLReasoner(
            base_model,
            temperature=temperature,
            sc_num=sc_num,
            icl_example=icl
        )

        # Setup evaluator
        evaluator = BWEvaluator(
            config_file=self.cfg.task.inference.config_file,
            domain_file=self.cfg.task.inference.domain_file,
            data_path=data_path,
            init_prompt=prompt,
            disable_log=False,
            output_extractor=sc_output_extractor,
            sample_prompt_type="rap"  # rap prompt includes cot
        )

        # Run evaluation
        accuracy = evaluator.evaluate(
            reasoner,
            shuffle_prompt=True,
            num_shot=self.cfg.task.inference.num_shot,
            resume=resume,
            log_dir=log_dir
        )

        print(f'Accuracy: {accuracy}')

        # Save results to output directory
        results = {
            "accuracy": accuracy,
            "model_checkpoint": model_checkpoint,
            "steps": steps,
            "temperature": temperature,
            "sc_num": sc_num,
            "use_icl": use_icl,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        with open(self.output_dir / "inference_results.json", "w") as f:
            json.dump(results, f, indent=2)

        return accuracy


class CountdownTrainer(BaseTrainer):
    """Class for training and inference on countdown models"""

    def _prepare_dataset(self, data_files):
        """Prepare dataset for training"""
        if self.cfg.task.force_redownload:
            all_data = [load_dataset(data_path, download_mode='FORCE_REDOWNLOAD') for data_path in data_files]
        else:
            all_data = [load_dataset(data_path) for data_path in data_files]
        train_data = [data['train'] for data in all_data]
        test_data = [data['test'] for data in all_data]
        # Annotate with difficulty
        add_task_difficulty = lambda task_idx, dataset: dataset.add_column("task", [task_idx] * len(dataset))
        train_data = [add_task_difficulty(i, data) for i, data in enumerate(train_data)]
        test_data = [add_task_difficulty(i, data) for i, data in enumerate(test_data)]

        train_dataset = concatenate_datasets(train_data)
        test_dataset = concatenate_datasets(test_data)
        train_dataset = train_dataset.shuffle(seed=self.cfg.experiment.dataset_seed)
        test_dataset = test_dataset.shuffle(seed=self.cfg.experiment.dataset_seed)

        # Limit dataset size if specified
        if self.cfg.task.train_size > 0:
            train_dataset = train_dataset.select(range(self.cfg.task.train_size))
            test_dataset = test_dataset.select(range(self.cfg.task.test_size))

        print(f"Dataset prepared with {len(train_dataset)} training samples and {len(test_dataset)} test samples")
        return train_dataset, test_dataset

    def _construct_reasoning_trace(self, reasoning_steps):
        """Construct reasoning trace from reasoning steps"""
        reasoning_trace = []
        n_r = len(reasoning_steps) - 1
        for i, step in enumerate(reasoning_steps):
            if 0 < i < n_r:
                reasoning_trace.append(f"Step {i}: {step}")
        reasoning_trace.append(f"Final Result: {reasoning_steps[-1]}")
        return reasoning_trace

    def _generate_prompt(self, tokenizer, example):
        """Generate prompt for the countdown model"""
        # Extract target and numbers from the example
        data = example.get("reward_model", {}).get("ground_truth", {})
        target = data.get("target")
        numbers = data.get("numbers")
        # expression = data.get("expression") # e.g., (((76 - 80) - 28) + 43), (((65 * 12) + 60) / 28)
        reasoning_steps = example.get("reasoning_steps")
        reasoning_trace = self._construct_reasoning_trace(reasoning_steps)

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

        return {
            "prompt": tokenizer.apply_chat_template(messages, tokenize=False, continue_final_message=True),
            "target": target,
            "numbers": numbers,
            "reasoning_trace": reasoning_trace,
        }

    def _validate_countdown_response_format(self, response: str):
        """Validate the countdown response format"""
        # Remove leading/trailing whitespace
        response = response.strip()

        # Must contain <think> and </think> tags
        if "<think>" not in response or "</think>" not in response:
            print('Response does not contain think tags')
            return False

        # Must contain <answer> and </answer> tags
        if "<answer>" not in response or "</answer>" not in response:
            print('Response does not contain answer tags')
            return False

        # Check that tags are in correct order
        think_open = response.find("<think>")
        think_close = response.find("</think>")
        answer_open = response.find("<answer>")
        answer_close = response.find("</answer>")

        if think_close < think_open or answer_close < answer_open:
            return False

        if answer_open < think_close:
            return False

        return True

    def _countdown_reward_fn(self, completions, target, numbers, **kwargs):
        """Reward function for countdown task"""
        rewards = []
        for completion, target_i, numbers_i in zip(completions, target, numbers):
            try:
                print('#########################')
                completion = "<think>" + completion
                print(completion)

                if not self._validate_countdown_response_format(completion):
                    print('Response Format Error')
                    rewards.append(0.0)  # Penalty to avoid format errors
                    continue

                # Use the CountdownRewardModel class
                reward_model = CountdownRewardModel(target_i, numbers_i)
                reward = reward_model.compute_score(completion)
                rewards.append(reward)
                print('-----')
                print(reward)
                print(target_i)
                print(numbers_i)
                print('-----')
                print('#########################')
            except Exception as e:
                print(e)
                rewards.append(0.0)

        return rewards

    def train(self):
        """Train a model using the specified algorithm with configurations from Hydra"""
        # Extract config values
        model_name = self.cfg.model.name
        output_model_name = self.cfg.output.run_name
        algorithm = self.cfg.algorithm.name

        # Load tokenizer and model
        model_config = self._get_model_config()
        tokenizer = AutoTokenizer.from_pretrained(
            model_config.model_name_or_path,
            trust_remote_code=model_config.trust_remote_code
        )
        model = AutoModelForCausalLM.from_pretrained(
            model_config.model_name_or_path,
            torch_dtype=model_config.torch_dtype,
            trust_remote_code=model_config.trust_remote_code,
            attn_implementation=model_config.attn_implementation
        )
        peft_config = get_peft_config(model_config)

        # Prepare dataset
        train_dataset, test_dataset = self._prepare_dataset(self.cfg.task.data_files)
        train_dataset = train_dataset.map(lambda example: self._generate_prompt(tokenizer, example))
        test_dataset = test_dataset.map(lambda example: self._generate_prompt(tokenizer, example))

        # Split dataset
        # train_test_split = dataset.train_test_split(test_size=self.cfg.task.test_size)
        # train_dataset = train_test_split["train"]
        # test_dataset = train_test_split["test"]

        # Setup training arguments based on algorithm
        if "grpo" in algorithm:
            training_args = self._setup_grpo_training()
            trainer = CurriculumGRPOTrainer(
                model=model,
                reward_funcs=self._countdown_reward_fn,
                args=training_args,
                train_dataset=train_dataset,
                eval_dataset=test_dataset,
                processing_class=tokenizer,
                peft_config=peft_config,
                num_tasks=len(self.cfg.task.data_files),
                total_iterations=training_args.max_steps,
                data_schedule=self.cfg.algorithm.training.curriculum_schedule,
                scheduler_params=self.cfg.algorithm.training.scheduler_params,
            )

        elif algorithm == "ppo":
            training_args = self._setup_ppo_training()
            trainer = PPOTrainer(
                model=model_config.model_name_or_path,
                ref_model=model_config.model_name_or_path,  # Same model as reference
                tokenizer=tokenizer,
                args=training_args,
                reward_fn=self._countdown_reward_fn,
                train_dataset=train_dataset,
                eval_dataset=test_dataset,
                peft_config=get_peft_config(model_config),
            )

        else:
            raise ValueError(f"Unsupported algorithm: {algorithm}")

        # Train model
        trainer.train()
        trainer.save_model(training_args.output_dir)

        if self.cfg.algorithm.training.push_to_hub:
            trainer.push_to_hub(dataset_name='countdown-dataset')

    def inference(self):
        """Run inference using the trained model"""
        # Extract config values
        model_checkpoint = self.cfg.task.inference.checkpoint
        sc_num = self.cfg.task.inference.sc_num

        # Generate checkpoint path
        model_dir = self._get_checkpoint_path(model_checkpoint, self.cfg.model.trim)

        # Load test dataset
        _, test_dataset = self._prepare_dataset([self.cfg.task.test_file])

        # Load model and tokenizer
        tokenizer = AutoTokenizer.from_pretrained(
            model_dir,
            trust_remote_code=self.cfg.model.trust_remote_code
        )

        # Custom model for inference
        model = HFModel(
            model_pth=model_dir,
            tokenizer_pth=model_dir,
            max_new_tokens=self.cfg.task.inference.max_new_tokens
        )

        # Run inference on test dataset
        correct = 0
        rewards = 0
        total = 0
        results = []

        for example in tqdm(test_dataset):
            # Generate prompt
            prompt_data = self._generate_prompt(tokenizer, example)
            prompt = prompt_data["prompt"]

            # Generate responses
            outputs = []
            for _ in range(sc_num):
                output = model.generate([prompt], do_sample=True, temperature=0.0, verbose=False, skip_special_tokens=False).text[0]
                outputs.append(output)

            # Evaluate responses
            for output in outputs:
                # Prepare ground truth for scoring
                ground_truth = {
                    "target": prompt_data["target"],
                    "numbers": prompt_data["numbers"]
                }

                # Use the CountdownRewardModel for evaluation
                reward_model = CountdownRewardModel(prompt_data["target"], prompt_data["numbers"])

                # Calculate score
                score = reward_model.compute_score(output)

                # Extract solution
                solution = reward_model.extract_equation(output)

                # Record results
                results.append({
                    "prompt": prompt,
                    "output": output,
                    "solution": solution,
                    "target": prompt_data["target"],
                    "numbers": prompt_data["numbers"],
                    "score": score
                })

                rewards += score
                if score > 0.5:  # Assuming score > 0.5 means correct answer
                    correct += 1
                total += 1

        # Calculate accuracy
        accuracy = correct / total if total > 0 else 0
        rewards /= total if total > 0 else 0
        print(f'Accuracy: {accuracy}, Rewards: {rewards}')

        # Save results to output directory
        evaluation_results = {
            "accuracy": accuracy,
            "rewards": rewards,
            "model_checkpoint": model_checkpoint,
            "sc_num": sc_num,
            "detailed_results": results,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # with open(os.path.join(model_dir, "inference_results.json"), "w") as f:
        #     json.dump(evaluation_results, f, indent=2)

        return accuracy



class ArithmeticTrainer(BaseTrainer):
    """Class for training and inference on Arithmetic models"""

    def _prepare_dataset(self):
        """Prepare dataset for training"""
        all_samples = []
        for task_idx, file in enumerate(self.cfg.task.data_files):
            file_dataset = load_dataset('json', data_files=file)['train']
            # Annotate with difficulty
            file_dataset = file_dataset.add_column("task", [task_idx] * len(file_dataset))
            all_samples.extend(file_dataset)
        dataset = Dataset.from_list(all_samples)
        dataset = dataset.shuffle(seed=self.cfg.experiment.dataset_seed)
        return dataset

    def extract_answer(self, text):
        """Extract answer from raw gsm8k answer string"""
        text = text.replace(",", "")
        marker_pos = text.find('####')

        if marker_pos == -1:
            return None

        answer_text = text[marker_pos + 4:].strip()
        answer_text = answer_text.split()[0]

        try:
            return answer_text
        except ValueError:
            return None

    def _generate_prompt(self, tokenizer, example):
        """Generate prompt for the arithmetic model"""

        if 'gsm8k' in self.cfg.task.name:
            question = example["question"]
            sft = example["answer"]
            answer = self.extract_answer(sft)
            if 'gsm8k2' in self.cfg.task.name and example.get("task") == 0:
                answer = float(sft)
            instruction = f"Solve the following math problem\n{question}\n\n Show your work in <think> </think> tags. And return the final answer in <answer> </answer> tags, for example <answer> 500 </answer>."

        elif 'aqua' in self.cfg.task.name:
            question = example["question"]
            sft = example["rationale"]
            answer = example["answer"].strip()
            options = "  ".join(example["options"])
            instruction = f"Solve the following math problem and choose an answer from the given options\n{question}\n{options}\n\n Show your work in <think> </think> tags. And return the final answer in <answer> </answer> tags, for example <answer> C </answer>."

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
            "task" : example["task"]
        }

    @staticmethod
    def _is_formatted(response: str):
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

    @staticmethod
    def _is_correct(response: str, answer: str):
        answer_match = re.findall(r'<answer>\s*(.*?)\s*</answer>', response, re.DOTALL)
        if len(answer_match) > 0:
            if answer_match[0].strip() == answer:
                return True
        return False

    def arithmetic_reward_fn(self, prompts, completions, correctness_reward=0.9, formatted_reward=0.1, **kwargs):
        rewards = []
        for completion, answer in zip(completions, kwargs['answer']):
            try:
                completion = "<think>" + completion

                is_formatted, reason_str = self._is_formatted(completion)
                is_correct = self._is_correct(completion, answer)

                reward = 0.0
                if is_formatted:
                    reward += formatted_reward
                if is_correct:
                    reward += correctness_reward
                rewards.append(reward)

                if self.last_log_time is None:
                    self.last_log_time = time.time()
                if time.time() - self.last_log_time > 10:
                    self.last_log_time = time.time()
                    log_on_main(f"\n#########################\n{completion}\n-----\n{reason_str}\n{reward}\n-----\n#########################\n\n")

            except Exception as e:
                log_on_main(e)
                rewards.append(0.0)
        return rewards


    def train(self):
        """Train a model using the specified algorithm with configurations from Hydra"""
        # Extract config values
        model_name = self.cfg.model.name
        output_model_name = self.cfg.output.run_name
        algorithm = self.cfg.algorithm.name

        # Load tokenizer & model
        model_config = self._get_model_config()
        tokenizer = AutoTokenizer.from_pretrained(
            model_config.model_name_or_path,
            trust_remote_code=model_config.trust_remote_code
        )
        model = AutoModelForCausalLM.from_pretrained(
            model_config.model_name_or_path,
            torch_dtype=model_config.torch_dtype,
            trust_remote_code=model_config.trust_remote_code,
            attn_implementation=model_config.attn_implementation
        )
        peft_config = get_peft_config(model_config)

        # Prepare dataset
        dataset = self._prepare_dataset()
        dataset = dataset.map(lambda example: self._generate_prompt(tokenizer, example), remove_columns=dataset.column_names)
        log_on_main(dataset)

        # Setup training arguments based on algorithm
        if "grpo" in algorithm:
            training_args = self._setup_grpo_training()
            trainer = CurriculumGRPOTrainer(
                model=model,
                reward_funcs=self.arithmetic_reward_fn,
                args=training_args,
                train_dataset=dataset,
                processing_class=tokenizer,
                peft_config=peft_config,
                num_tasks=len(self.cfg.task.data_files),
                total_iterations=training_args.max_steps,
                data_schedule=self.cfg.algorithm.training.curriculum_schedule,
                scheduler_params=self.cfg.algorithm.training.scheduler_params,
            )
        elif algorithm == "ppo":
            training_args = self._setup_ppo_training()
            trainer = PPOTrainer(
                model=model,
                ref_model=model_config.model_name_or_path,  # Same model as reference
                tokenizer=tokenizer,
                args=training_args,
                reward_fn=self._reward_fn,
                train_dataset=dataset['train'],
                eval_dataset=dataset['test'],
                peft_config=peft_config,
            )
        else:
            raise ValueError(f"Unsupported algorithm: {algorithm}")

        # Train model
        trainer.train()
        trainer.save_model(training_args.output_dir)

        if self.cfg.algorithm.training.push_to_hub:
            trainer.push_to_hub(dataset_name='gsm8k-dataset')


    def inference(self):
        """Run inference using the trained model"""
        if self.cfg.task.name == "aqua":
            pass


        else:
            # Extract config values
            model_checkpoint = self.cfg.task.inference.checkpoint
            sc_num = self.cfg.task.inference.sc_num


            # Generate checkpoint path
            model_dir = self._get_checkpoint_path(model_checkpoint, self.cfg.model.trim)

            # Load model and tokenizer
            tokenizer = AutoTokenizer.from_pretrained(
                model_dir,
                trust_remote_code=self.cfg.model.trust_remote_code
            )

            # Load test dataset
            if "gsm8k" in self.cfg.task.name:
                dataset = datasets.load_dataset("gsm8k", "main", split="test")
                dataset = dataset.add_column("task", [0] * len(dataset))
            else:
                dataset = self._prepare_dataset()
                train_test_split = dataset.train_test_split(test_size=self.cfg.experiment.test_size)
                dataset = train_test_split["test"]

            test_dataset = dataset.map(lambda example: self._generate_prompt(tokenizer, example))
            # Custom model for inference
            model = HFModel(
                model_pth=model_dir,
                tokenizer_pth=model_dir,
                max_new_tokens=self.cfg.task.inference.max_new_tokens
            )



            correct = 0
            rewards = 0
            total = 0
            resume = 0
            batch_size = 16
            results = []

            pbar = tqdm(range(0, len(test_dataset), batch_size),
                        initial=resume,
                        desc=self.cfg.task.name)

            for batch_start in pbar:
            # Generate batched responses
                batch = test_dataset[batch_start: batch_start + batch_size]
                batch_examples = [dict(zip(batch, t)) for t in zip(*batch.values())]
                inputs = [input["prompt"] for input in batch_examples]

                outputs = model.generate(inputs,
                                            hide_input=True,
                                            do_sample=True,
                                            skip_special_tokens=False,
                                            temperature=0.0).text

                for output_idx, output in enumerate(outputs):
                    answer = test_dataset[batch_start + output_idx]["answer"]
                    reward_model = GSM8KRewardModel(answer)
                    score = reward_model.compute_score(output)

                    # Record results
                    results.append({
                        "prompt": inputs[output_idx],
                        "output": output,
                        "solution": answer,
                        "score": score
                    })

                    if score > 0.5:
                        correct += 1
                    total += 1
                accuracy = correct / total if total > 0 else 0
                print(accuracy)

            # Calculate accuracy
            accuracy = correct / total if total > 0 else 0
            rewards /= total if total > 0 else 0
            print(f'Accuracy: {accuracy}, Rewards: {rewards}')


            # Save results to output directory
            evaluation_results = {
                "accuracy": accuracy,
                "rewards": rewards,
                "model_checkpoint": model_checkpoint,
                "sc_num": sc_num,
                "detailed_results": results,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            os.makedirs(model_dir, exist_ok=True)
            with open(os.path.join(model_dir, "inference_results.json"), "w") as f:
                json.dump(evaluation_results, f, indent=2)


            return accuracy

class RLReasoner:
    """Class for reasoning with RL models"""

    def __init__(self, base_model, temperature=0.8, sc_num=1, model_type="completion", icl_example=""):
        self.base_model = base_model
        self.temperature = temperature
        self.model_type = model_type
        self.sc_num = sc_num
        self.tokenizer = base_model.tokenizer
        self.icl_example = icl_example

    def get_r1_prompt(self, example):
        r1_prefix = [{
            "role": "system",
            "content": "You are a helpful assistant. You first thinks about the reasoning process in the mind and then provides the user with the answer.\n"
        },
            {
                "role": "user",
                "content": f"I am playing with a set of blocks where I need to arrange the blocks into stacks. Here are the actions I can do\n\nPick up a block\nUnstack a block from on top of another block\nPut down a block\nStack a block on top of another block\n\nI have the following restrictions on my actions:\nI can only pick up or unstack one block at a time.\nI can only pick up or unstack a block if my hand is empty.\nI can only pick up a block if the block is on the table and the block is clear. A block is clear if the block has no other blocks on top of it and if the block is not picked up.\nI can only unstack a block from on top of another block if the block I am unstacking was really on top of the other block.\nI can only unstack a block from on top of another block if the block I am unstacking is clear.\nOnce I pick up or unstack a block, I am holding the block.\nI can only put down a block that I am holding.\nI can only stack a block on top of another block if I am holding the block being stacked.\nI can only stack a block on top of another block if the block onto which I am stacking the block is clear.\nOnce I put down or stack a block, my hand becomes empty.\nHere is the format of the actions: \n\npick up the [block_name] block # for example: pick up the blue block\nunstack the [block_name] block from on top of the [another_block_name] block # for example: unstack the orange block from on top of the black block\nput down the [block_name] block # for example put down the red block\nstack the [block_name] block on top of the [another_block_name] block # for example: stack the yellow block on top of the red block \n\n{self.icl_example}\n\nHere is the initial state of the blocks: {example['init']}\n\nHere is the goal state of the blocks: {example['goal']}.\nShow your work in the <think> </think> tags. Return the final sequence of actions as the plan in the <answer> </answer> tags.\n"
            },
            {
                "role": "assistant",
                "content": "Let me solve this step by step.\n<think>"
            }
        ]
        return self.tokenizer.apply_chat_template(r1_prefix, tokenize=False, continue_final_message=True)

    def __call__(self, example, prompt=None):
        inputs = self.get_r1_prompt(example)
        outputs = []
        for _ in range(self.sc_num):
            if self.model_type == "completion":
                outputs.append(self.base_model.generate([inputs],
                                                        hide_input=True,
                                                        do_sample=True,
                                                        temperature=self.temperature).text[0].strip())
        return outputs


def occupy_gpu_memory(gb=75, device="cuda:0"):
    """
    Allocates a tensor on the specified GPU that occupies approximately `gb` GB of memory.
    The tensor remains allocated indefinitely (until the process is terminated).
    """
    # Calculate the target memory in bytes.
    target_bytes = gb * 1024 ** 3
    # For float32, each element takes 4 bytes.
    num_elements = target_bytes // 4
    torch.cuda.empty_cache()
    print(f"Allocating a tensor with {num_elements} float32 elements (~{gb}GB) on {device}.")

    try:
        # Allocate the tensor on the specified device.
        tensor = torch.empty(num_elements, dtype=torch.float32, device=device)
        tensor.fill_(0)
        print(f"Successfully allocated ~{gb}GB on {device}. Holding memory indefinitely...")
    except RuntimeError as e:
        print("Failed to allocate memory. Your GPU may not have enough free memory.")
        raise e

    # Hold the memory indefinitely.
    while True:
        print("Holding memory...")
        time.sleep(60)


@hydra.main(config_path="conf", config_name="config", version_base="1.3")
def main(cfg: DictConfig):
    """Main entry point for training and inference with Hydra configuration"""
    print(OmegaConf.to_yaml(cfg))

    # Select the appropriate trainer based on the task
    task = cfg.task.name
    if "blocksworld" in task:
        trainer = BlocksWorldTrainer(cfg)
    elif "countdown" in task:
        trainer = CountdownTrainer(cfg)
    elif "gsm8k" or "easymath" or "aqua" in task:
        trainer = ArithmeticTrainer(cfg)
    else:
        raise ValueError(f"Unknown task: {task}. Choose either 'blocksworld', 'countdown', or 'gsm8k'")

    # Check which mode to run
    if cfg.mode == "train":
        trainer.train()
    elif cfg.mode == "inference":
        trainer.inference()
    else:
        raise ValueError(f"Unknown mode: {cfg.mode}. Choose either 'train' or 'inference'")

    # Optional: Occupy GPU memory after training (useful for server environments)
    if cfg.get("occupy_gpu_memory", False):
        occupy_gpu_memory(gb=cfg.occupy_gpu_memory_gb, device=cfg.gpu_device)


if __name__ == "__main__":
    main()