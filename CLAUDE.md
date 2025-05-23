# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Sys2Bench is a comprehensive benchmark for evaluating the reasoning and planning abilities of Large Language Models (LLMs) using various inference-time techniques. It tests LLMs across 11 diverse tasks in 5 categories:
- **Algorithmic Reasoning**: Game of 24, Binpacking
- **Planning**: Blocksworld, Trip Plan, Calendar Plan, Rubik's Cube
- **Arithmetic Reasoning**: GSM8K, AQuA
- **Logical Reasoning**: ProntoQA
- **Common Sense Reasoning**: StrategyQA, HotPotQA

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