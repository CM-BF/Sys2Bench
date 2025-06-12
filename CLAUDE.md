# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Table of Contents

1. [Overview](#overview)
2. [📚 Documentation Structure](#-documentation-structure)
3. [Key Commands](#key-commands)
   - [Setup and Environment](#setup-and-environment)
   - [Running Experiments](#running-experiments)
   - [Batch Evaluation](#batch-evaluation)
   - [Reinforcement Learning](#reinforcement-learning-rl)
4. [Architecture and Code Structure](#architecture-and-code-structure)
   - [Core Framework](#core-framework-reasoners)
   - [Method Implementations](#method-implementations-methods)
   - [Key Design Patterns](#key-design-patterns)
5. [Common Development Patterns](#common-development-patterns)
   - [Model Selection](#model-selection)
   - [Temperature and Sampling](#temperature-and-sampling)
   - [Data Paths](#data-paths)
   - [Logging and Output](#logging-and-output)
6. [Adding New Tasks or Methods](#adding-new-tasks-or-methods)
7. [🎯 Quick Task Reference](#-quick-task-reference)
8. [Appendix: Method-Specific Details](#appendix-method-specific-details)

## Overview

Sys2Bench is a comprehensive benchmark for evaluating the reasoning and planning abilities of Large Language Models (LLMs) using various inference-time techniques. It tests LLMs across 11 diverse tasks in 5 categories:
- **Algorithmic Reasoning**: Game of 24, Binpacking
- **Planning**: Blocksworld, Trip Plan, Calendar Plan, Rubik's Cube
- **Arithmetic Reasoning**: GSM8K, AQuA
- **Logical Reasoning**: ProntoQA
- **Common Sense Reasoning**: StrategyQA, HotPotQA

## 📚 Documentation Structure

### Core Documentation
- **[README.md](/README.md)** - Project overview, setup instructions, and basic usage
- **[CLAUDE.md](/CLAUDE.md)** - This file, comprehensive guide for working with the codebase
- **[REMOTE_DEVELOPMENT_GUIDE.md](/REMOTE_DEVELOPMENT_GUIDE.md)** - Consolidated guide for remote development workflows

### Method-Specific Documentation
- **[methods/RL/CLAUDE_RL.md](methods/RL/CLAUDE_RL.md)** - Detailed RL implementation guide
- **[methods/AutoHD/README.md](methods/AutoHD/README.md)** - AutoHD method documentation
- Each method directory contains specific documentation and examples

### Remote Development Resources
For remote server development, GPU experiments, and long-running tasks, see:
- **[REMOTE_DEVELOPMENT_GUIDE.md](/REMOTE_DEVELOPMENT_GUIDE.md)** - Complete remote workflow guide

**Note**: Since we're working directly on the remote machine, the remote development workflows in the guide above are for reference when you need to work from a local machine.

## Key Commands

### Setup and Environment
```bash
# Initial setup (creates conda environment and sets environment variables)
bash setup.sh

# Activate environment
conda activate sys2bench

# Export API keys (required for OpenAI, optional for DeepInfra)
export OPENAI_API_KEY="your-api-key"
export DEEPINFRA_TOKEN="your-token"  # Optional for LLaMA models
```

### Running Experiments

**Run all benchmarks:**
```bash
bash sys2bench.sh
```

**Run specific method on task:**
```bash
# Shell script approach (recommended)
bash methods/[METHOD]/[TASK]/[method].sh

# Direct Python execution
python methods/[METHOD]/[TASK]/inference.py --base_lm openai --openai_model gpt-4o-mini [additional args]
```

**Methods available:** CoT, IO, RAP, ToT, AutoHD, RL

### Batch Evaluation
```bash
# Regular evaluation
GPU_IDX=0,1,2 bash batch_evaluate.sh [conda_env] [evaluate_step] [model_trim]

# Pass@k evaluation
GPU_IDX=0,1,2 bash batch_evaluate_pass_at_k.sh [conda_env] [evaluate_step]

# SLURM cluster submission
python batch_runner.py --cluster [ut/tamu]
```

### Reinforcement Learning (RL)

**Quick Start:**
```bash
# Set environment and run training
export ROOT_PATH=/path/to/Sys2Bench
accelerate launch --config_file methods/RL/deep_speed.yaml \
    methods/RL/main.py mode=train task=countdown algorithm=grpo model=qwen15
```

**Key Features:**
- Curriculum learning with multiple schedulers (balanced, cosine, gaussian, variance_regularized)
- Multi-task training across difficulty levels
- GRPO/PPO/SGRPO algorithm support
- Automated GPU monitoring and notifications

**For detailed RL documentation, see:** `methods/RL/CLAUDE_RL.md`

## Architecture and Code Structure

### Core Framework (`/reasoners/`)
- **Base classes**: Define abstract interfaces for search algorithms and world models
- **Algorithms**: Implementations of beam search, DFS, greedy, MCTS, and heuristic search
- **LM interfaces**: Unified API for OpenAI, HuggingFace, Anthropic, and LLaMA models
- **Benchmarks**: Task-specific implementations and evaluation logic

### Method Implementations (`/methods/`)
Each method follows a consistent structure:
- `inference.py`: Main execution script with method-specific logic
- `[method].sh`: Shell script with common parameter configurations
- `world_model.py`: Task state representation and transition logic (for search methods)
- `search_config.py`: Configuration for search algorithms
- `utils.py`: Helper functions and evaluation metrics

### Key Design Patterns
1. **World Model Pattern**: Search-based methods (RAP, ToT, AutoHD) use world models to represent task states and valid transitions
2. **Prompt Templates**: Each task has standardized prompts in `/prompts/[task]/`
3. **Distributed Execution**: Many scripts support multi-GPU via `torch.distributed.run`
4. **Configuration Management**: RL experiments use Hydra for complex configuration management


### Adding New Tasks or Methods
1. **New Task**: Add data to `/data/`, implement benchmark class in `/reasoners/benchmark/`, create prompts in `/prompts/`
2. **New Method**: Create directory in `/methods/`, implement inference script following existing patterns, add shell script for easy execution

## Common Development Patterns

### Model Selection
- OpenAI: `--base_lm openai --openai_model [gpt-4o/gpt-4o-mini]`
- LLaMA API: `--base_lm llamaapi --api_model_id Meta-Llama-3.1-70B-Instruct`
- HuggingFace: `--base_lm hf --model_dir [path]`

### Temperature and Sampling
- Most methods use `--temperature 0.8` for generation
- Search methods use beam size (`--n_beam`) and depth limit (`--depth_limit`)

### Data Paths
- Test data: `/data/[task]/test.json` or task-specific filenames
- Train data: `/data/[task]/train.json` (used for few-shot examples)
- Prompts: `/prompts/[task]/prompts.json`

### Logging and Output
- Logs are typically written to `logs/[method]/[task]/[timestamp]`
- Results include accuracy metrics and often per-example predictions
- Search methods may output tree visualizations or search traces
- RL outputs are saved in `outputs/[model]_[task]_[algorithm]_[timestamp]/`

---

## Appendix: Method-Specific Details

### Reinforcement Learning (RL)
For comprehensive RL documentation including:
- Detailed training configurations
- Reward model implementation
- Curriculum scheduler details
- GPU monitoring setup
- Debugging workflows

See: `methods/RL/CLAUDE_RL.md`

### Other Methods
Each method directory contains its own specific documentation and examples.
Refer to the respective method directories for detailed implementation guides.

## 🎯 Quick Task Reference

### For Running Experiments
1. **Simple experiment** (no GPU): Run directly with shell scripts
2. **GPU experiment**: Check GPU availability → run with appropriate CUDA_VISIBLE_DEVICES
3. **RL training**: See methods/RL/CLAUDE_RL.md for detailed instructions
4. **Monitor GPUs**: Use `nvidia-smi` or the RL monitoring system

### For Development
1. **Add new method**: Create directory structure following existing patterns
2. **Add new task**: Add data, benchmark class, and prompts
3. **Track experiments**: Use meaningful output directories and logging

### For Remote Development
See [REMOTE_DEVELOPMENT_GUIDE.md](/REMOTE_DEVELOPMENT_GUIDE.md) for complete workflow when working from a local machine.

## 📋 Important Notes

- **Follow existing patterns** - Check similar methods for conventions
- **Use meaningful names** - For output directories, logs, and sessions
- **Check GPU availability** - Before starting large experiments
- **Document your changes** - Update relevant documentation files