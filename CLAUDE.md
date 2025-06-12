# CLAUDE.md

This file provides guidance for working with the Easy 2 Hard (E2H) Reasoner implementation in Sys2Bench.

## Table of Contents

1. [Overview](#overview)
2. [Paper Implementation](#paper-implementation)
3. [Key Commands](#key-commands)
4. [Architecture](#architecture)
5. [Curriculum Schedulers](#curriculum-schedulers)
6. [Supported Tasks](#supported-tasks)
7. [Configuration](#configuration)
8. [Running Experiments](#running-experiments)

## Overview

This repository contains the implementation of the paper "Curriculum Reinforcement Learning from Easy to Hard Tasks Improves LLM Reasoning" (https://arxiv.org/html/2506.06632v1). The E2H Reasoner uses curriculum reinforcement learning to improve language models' reasoning capabilities by training them on tasks with progressively increasing difficulty.

## Paper Implementation

The entire implementation is contained in `/methods/RL/main.py`, which serves as the only valid entry point. This implementation includes:

- **Task Sampling**: Custom `TaskSampler` class that implements curriculum scheduling
- **Curriculum Schedulers**: Multiple scheduling strategies for task difficulty progression
- **GRPO Training**: Modified `CurriculumGRPOTrainer` that integrates with the task sampling
- **Multi-task Support**: Training across different difficulty levels within each task

## Key Commands

### Setup and Environment
```bash
# Activate environment
conda activate sys2bench

# Set environment variable
export ROOT_PATH=/path/to/Sys2Bench
```

### Training with E2H
```bash
# Basic training command
accelerate launch --config_file methods/RL/deep_speed.yaml \
    methods/RL/main.py mode=train task=countdown algorithm=grpo model=qwen15

# With specific scheduler
accelerate launch --config_file methods/RL/deep_speed.yaml \
    methods/RL/main.py mode=train task=blocksworld algorithm=grpo \
    model=qwen15 algorithm.training.curriculum_schedule=cosine
```

### Inference
```bash
python methods/RL/main.py mode=inference task=countdown \
    task.inference.checkpoint=1200 model=qwen15
```

## Architecture

The implementation centers around the `TaskSampler` class (lines 56-131 in main.py) which manages curriculum learning:

```python
class TaskSampler(torch.utils.data.Sampler):
    def __init__(self, dataset, num_tasks, total_iterations, 
                 data_schedule, batch_size, scheduler_params, seed=0)
```

The sampler:
1. Organizes data by difficulty level (task 0 = easiest, task N-1 = hardest)
2. Applies the chosen scheduling function at each iteration
3. Samples tasks according to the computed probabilities

## Curriculum Schedulers

The implementation includes five scheduling strategies:

### 1. **Balanced Schedule** (`balanced`)
- Equal probability for all difficulty levels throughout training
- P(task_i) = 1/num_tasks

### 2. **Classical Curriculum** (`classic`)
- Sequential progression through difficulties
- Trains on task i for T/num_tasks iterations before moving to task i+1

### 3. **Cosine Schedule** (`cosine`)
- Smooth transition from easy to hard tasks
- Uses cosine annealing to shift probabilities
- Includes minimum probability floor to prevent task starvation

### 4. **Gaussian Schedule** (`gaussian`)
- Bell curve that moves from easy to hard tasks
- Configurable parameters:
  - `mu_exp`: Controls progression speed (default: 1.0)
  - `sigma`: Standard deviation of the Gaussian
  - `min_prob`: Minimum probability per task

### 5. **Variance Regularized** (`variance_regularized`)
- Adaptive scheduling based on performance variance
- Imported from external module
- Updates probabilities based on reward feedback

## Supported Tasks

The implementation supports four main task categories:

1. **BlocksWorld** - Planning task with block manipulation
2. **Countdown** - Arithmetic puzzle solving
3. **Arithmetic** - GSM8K, AQuA, MATH datasets
4. **Coding** - Programming problem solving

Each task has multiple difficulty levels defined by separate data files.

## Configuration

The system uses Hydra for configuration management. Key configuration options:

```yaml
# Algorithm settings
algorithm:
  name: grpo  # or ppo
  training:
    curriculum_schedule: cosine  # balanced, classic, gaussian, variance_regularized
    scheduler_params:
      mu_exp: 1.0
      sigma: 0.5
      min_prob: 0.1
    max_steps: 1200
    per_device_train_batch_size: 4

# Task settings
task:
  name: countdown  # blocksworld, gsm8k, etc.
  data_files:
    - data/countdown/easy.json
    - data/countdown/medium.json
    - data/countdown/hard.json

# Model settings
model:
  name: Qwen/Qwen2.5-1.5B-Instruct
  family: Qwen
```

## Running Experiments

### Training Examples

**Countdown with Gaussian scheduler:**
```bash
accelerate launch --config_file methods/RL/deep_speed.yaml \
    methods/RL/main.py mode=train task=countdown algorithm=grpo \
    model=qwen15 algorithm.training.curriculum_schedule=gaussian \
    algorithm.training.scheduler_params.sigma=0.5 \
    algorithm.training.scheduler_params.mu_exp=0.8
```

**BlocksWorld with Cosine scheduler:**
```bash
accelerate launch --config_file methods/RL/deep_speed.yaml \
    methods/RL/main.py mode=train task=blocksworld algorithm=grpo \
    model=qwen15 algorithm.training.curriculum_schedule=cosine
```

### Monitoring Training
- Logs are saved to Hydra output directory
- Task sampling probabilities are logged at each iteration
- Rewards and format compliance are tracked

### Key Implementation Details

1. **Prompt Format**: All tasks use a consistent format with `<think>` tags for reasoning and task-specific answer tags
2. **Reward Functions**: Each task has a custom reward function that validates format and correctness
3. **Batch Sampling**: Tasks are sampled per-batch based on scheduler probabilities
4. **Data Exhaustion**: When a difficulty level's data is exhausted, it's reshuffled

## 📋 Important Notes

- **Entry Point**: Always use `methods/RL/main.py` as the entry point
- **Scheduler Selection**: Choose scheduler based on task characteristics
- **GPU Memory**: Configure batch size and gradient accumulation based on available memory
- **Checkpoint Saving**: Models are saved at regular intervals defined in configuration