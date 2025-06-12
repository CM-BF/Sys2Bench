# CLAUDE_RL.md

This file provides comprehensive guidance for Claude Code when working with the RL (Reinforcement Learning) components of Sys2Bench.

## ⚠️ IMPORTANT INSTRUCTIONS

**Document Priority**: 
- CLAUDE.md has **HIGHER PRIORITY** than CLAUDE_RL.md when there are conflicts about commands to use
- CLAUDE.md has been checked by the user, while CLAUDE_RL.md was written by Claude Code
- Always refer to CLAUDE.md first for training commands and configurations

**Working Approach**:
- Read all configurations, files, and scripts carefully before making changes
- Focus on testing and exploring the variance regularized (vrex) scheduler
- The main entry point is `methods/RL/main.py` - never use other entry points
- Main task focus is countdown tasks with curriculum learning

## Table of Contents

1. [🚀 Quick Start](#-quick-start)
2. [📋 What I've Accomplished](#-what-ive-accomplished)
3. [🧠 Deep Implementation Understanding](#-deep-implementation-understanding)
4. [🔧 Common Development Pipeline](#-common-development-pipeline)
5. [📊 Key Parameters for Variance Regularized Scheduler](#-key-parameters-for-variance-regularized-scheduler)
6. [🎯 Next Steps](#-next-steps)
7. [📋 Common Tasks](#-common-tasks)
8. [🛠️ Troubleshooting](#️-troubleshooting)
9. [📚 Important Files Reference](#-important-files-reference)
10. [🔍 Key Insights](#-key-insights)

## 🚀 Quick Start

### Essential Tools & Commands

```bash
# SSH to remote server (requires VPN connection)
ssh shurui.gui@dive7.engr.tamu.edu

# Check GPU availability
nvidia-smi --query-gpu=index,memory.used,memory.free --format=csv,noheader

# Upload files to remote
rsync -av local_file shurui.gui@dive7.engr.tamu.edu:/data/shurui.gui/Projects/Sys2Bench/methods/RL/

# Activate environment on remote
source /data/shurui.gui/mambaforge/etc/profile.d/conda.sh
conda activate sys2bench

# Git workflow
git add files...
git commit -m "message"
git status
```

For remote development workflow (editing locally, syncing files, using tmux), see: `/REMOTE_DEVELOPMENT_GUIDE.md`

## 📋 What I've Accomplished

### 1. **Variance Regularized Curriculum Scheduler**
- **Location**: `schedulers/variance_regularized_scheduler.py`
- **Purpose**: Implements OOD generalization principles from VREx and GroupDRO
- **Features**:
  - Adaptive task sampling based on performance variance
  - GroupDRO-style exponential weighting for worst-group focus
  - VREx-inspired variance penalty to encourage uniform performance
  - Configurable warmup, update intervals, and blending parameters

### 2. **Integration into Main Training Pipeline**
- **Modified**: `main.py`
  - Added import for variance regularized scheduler
  - Added to `schedule_funcs` dictionary
  - Added performance tracking placeholders in `CurriculumGRPOTrainer`
  - Store batch task IDs for future performance updates

### 3. **GPU Monitoring System**
- **Location**: `monitoring/gpu_monitor_email.py`
- **Features**:
  - Automated GPU availability checking
  - Email notifications when GPUs are ready
  - Secure credential storage with encryption
  - Test mode for single GPU verification

### 4. **Comprehensive WandB Logging Integration**
- **Enhanced**: `variance_regularized_scheduler.py`
- **Features**:
  - Task-specific mean rewards and variances
  - Cross-task variance (VREx penalty) tracking
  - Task sampling probabilities monitoring
  - GroupDRO weights logging
  - Task frequency analysis

### 5. **Successful Training and Evaluation Results**
- **Training**: 1600-step VREx curriculum training on countdown2345 task
  - Final training reward: **54.16%** on training tasks (2-5 numbers)
  - Comprehensive VREx-specific metrics logged to WandB
  - Adaptive task sampling successfully implemented

- **Generalization Evaluation**: countdown6 task (harder 6-number problems)
  - Accuracy: **9.18%** (18.26% reward) on out-of-distribution test
  - Model shows generalization capability despite difficulty increase
  - Inference completed successfully with VREx-trained model

### 6. **Paper Baseline Comparison Results**
Based on "Curriculum Reinforcement Learning from Easy to Hard Tasks Improves LLM Reasoning" ([arxiv.org/html/2506.06632v1](https://arxiv.org/html/2506.06632v1)):

| Scheduler | OOD Accuracy (6-number countdown) | Notes |
|-----------|-----------------------------------|-------|
| **Balanced** | 9.2% | Standard baseline |
| **Classical CL** | 12.6% | Traditional curriculum learning |
| **Cosine (E2H-C)** | 6.4% | Smooth transition curriculum |
| **Gaussian (E2H-G) Best** | **14.2%** | E2H-G (0.5, 0.5) - Best paper result |
| **VREx (Our Implementation)** | **9.18%** | Variance regularized curriculum |

**Key Findings:**
- **VREx achieves competitive performance** at 9.18% OOD accuracy
- **Matches Balanced baseline** (9.2%) performance closely  
- **Outperforms Cosine** scheduler (6.4%) significantly
- **Below best Gaussian** (14.2%) but shows promise for further optimization
- **First successful implementation** of variance regularization for curriculum RL

### 7. **Directory Reorganization**
```
methods/RL/
├── conf/                            # Hydra configurations
├── logs/                            # Training and inference logs
├── monitoring/                      # GPU monitoring scripts
├── schedulers/                      # Curriculum schedulers
├── scripts/                         # Utility and setup scripts
├── utils/                           # Helper files and patches
├── *_reward_model.py                # Task-specific reward models
├── main.py                          # Main training entry point
├── implementation_understanding.md  # Deep technical documentation
└── CLAUDE_RL.md                    # This documentation
```

## 🧠 Deep Implementation Understanding

For a comprehensive technical understanding of the E2H curriculum learning implementation with variance regularized scheduler, see:

**[📖 implementation_understanding.md](implementation_understanding.md)**

This document covers:
- Core architecture and data flow
- TaskSampler mechanism in detail
- All 5 curriculum schedulers (balanced, classic, cosine, gaussian, variance_regularized)
- Variance regularized scheduler deep dive with theoretical foundations
- Complete reward feedback loop analysis
- Configuration system and integration points
- Critical implementation details and gotchas

**Priority**: Read this document carefully before making any modifications to the training pipeline.

## 🔧 Common Development Pipeline

### 1. **Local Development**
```bash
# Edit files locally
vim methods/RL/main.py

# Test syntax locally
python -m py_compile methods/RL/main.py

# Commit changes
git add methods/RL/main.py
git commit -m "Add feature X"
```

### 2. **Remote Deployment**
```bash
# Check VPN connection first!
ping dive7.engr.tamu.edu

# Upload to remote
rsync -av methods/RL/main.py shurui.gui@dive7.engr.tamu.edu:/data/shurui.gui/Projects/Sys2Bench/methods/RL/

# SSH to remote
ssh shurui.gui@dive7.engr.tamu.edu
```

### 3. **GPU Check & Training**
```bash
# On remote server
cd /data/shurui.gui/Projects/Sys2Bench
source /data/shurui.gui/mambaforge/etc/profile.d/conda.sh
conda activate sys2bench

# Check GPUs (need 2 GPUs: 1 for model, 1 for VLLM ~20GB)
nvidia-smi

# Run training (example)
WANDB_PROJECT=Sys2Bench ROOT_PATH=/data/shurui.gui/Projects/Sys2Bench \
CUDA_VISIBLE_DEVICES=0,1 accelerate launch \
    --num_processes 1 \
    --config_file methods/RL/deep_speed.yaml \
    methods/RL/main.py \
    mode=train \
    task=countdown6 \
    algorithm=grpo \
    algorithm.training.curriculum_schedule=variance_regularized \
    model=qwen15 \
    algorithm.training.max_steps=1600
```

## 📊 Key Parameters for Variance Regularized Scheduler

```yaml
algorithm.training.scheduler_params:
  min_prob: 0.1              # Minimum probability for each task
  temperature: 1.0           # Softmax temperature
  beta: 0.7                  # Blend factor (0=uniform, 1=fully adaptive)
  warmup_steps: 100          # Steps before adaptive sampling
  vrex_penalty_weight: 1.0   # Weight for variance penalty
  groupdro_alpha: 0.01       # Learning rate for group weights
  window_size: 100           # Performance tracking window
```

## 🎯 Next Steps

### Immediate Tasks
1. ✅ **GPU availability verified** - GPUs 0,1 available with sufficient memory
2. ✅ **VREx scheduler bugs fixed** - Fixed missing data_schedule attribute and training_step signature
3. ✅ **Training verified** - VREx scheduler successfully executing during training steps
4. ✅ **Add VREx logging** - Integrated comprehensive WandB logging for VREx-specific metrics
5. ✅ **Run full training** - Completed 1600-step VREx training on countdown2345 (Final reward: 54.16%)
6. ✅ **Evaluate generalization** - Tested VREx model on countdown6 task (9.18% accuracy on harder problems)
7. **Analyze results** - Compare variance regularized vs. other schedulers
8. **Baseline comparison** - Run training with balanced/cosine schedulers for comparison

### Future Improvements
1. **Performance Tracking Integration**
   - Currently has placeholders in `CurriculumGRPOTrainer.training_step()`
   - Need to capture actual rewards during training
   - Update `_last_batch_rewards` attribute

2. **Scheduler Evaluation**
   - Track cross-task performance variance over time
   - Compare convergence speed vs. baseline schedulers
   - Analyze final model generalization

3. **Extended Testing**
   - Test on multiple tasks beyond countdown
   - Ablation studies on scheduler parameters
   - Multi-seed evaluation for robustness

## 🛠️ Troubleshooting

### Common Issues

1. **VPN Connection Required**
   - Error: `Could not resolve hostname dive7.engr.tamu.edu`
   - Solution: Connect to university VPN first

2. **GPU Memory Requirements**
   - GRPO needs 2 GPUs: 1 for training, 1 for VLLM (~20GB)
   - Check with: `nvidia-smi --query-gpu=index,memory.free --format=csv`

3. **Environment Activation**
   - Always activate `sys2bench` environment before running
   - Path: `/data/shurui.gui/mambaforge/envs/sys2bench`

4. **Email Notifications**
   - Setup: `python scripts/setup_email.py`
   - Test: `python monitoring/gpu_monitor_email.py --test`
   - Credentials stored in `~/.sys2bench/`

## 📚 Important Files Reference

### Core Training
- `main.py` - Main training script with Hydra configuration
- `train.py` - Original training script
- `inference.py` - Inference script

### Reward Models
- `blocksworld_reward_model.py` - Block arrangement evaluation
- `countdown_reward_model.py` - Arithmetic expression validation
- `gsm8k_reward_model.py` - Math problem checking
- `coding_reward_model.py` - Code execution testing

### Configuration
- `conf/config.yaml` - Main configuration
- `conf/algorithm/grpo_variance_regularized.yaml` - VarReg specific config
- `conf/model/qwen15.yaml` - Model configurations
- `conf/task/countdown*.yaml` - Task configurations

### Monitoring & Utilities
- `monitoring/gpu_monitor_email.py` - GPU availability monitor
- `scripts/setup_email.py` - Email configuration setup
- `scripts/train_variance_regularized.sh` - Training launch script

## 📋 Common Tasks

### Task 1: Monitor and Reserve GPUs
Use the GPU monitor to automatically reserve GPUs when they become available.

```bash
# Direct execution (if on remote server)
cd /data/shurui.gui/Projects/Sys2Bench
conda activate sys2bench
python methods/RL/monitoring/rl_environment_monitor_immediate.py

# Or using tmux for persistent monitoring
# See /REMOTE_DEVELOPMENT_GUIDE.md for tmux utilities usage
```

**What it does:**
- Monitors GPUs every 60 seconds
- Immediately occupies any GPU with 50GB+ free memory using `sys_rl.py`
- Sends email notification when 2 GPUs are ready
- Holds GPUs until you're ready to train

### Task 2: Run RL Training
Once GPUs are reserved, kill the occupation processes and start training.

```bash
# On remote server
cd /data/shurui.gui/Projects/Sys2Bench

# Kill GPU occupation processes if any
ps -ef | grep "sys_rl.py\|rl_environment_monitor" | grep -v grep | awk '{print $2}' | xargs kill

# Verify environment (already activated)
# conda activate sys2bench

# ✅ VERIFIED WORKING COMMANDS:

# Test VREx scheduler (verified working - logs in methods/RL/logs/)
timeout 600 bash -c "WANDB_PROJECT=Sys2Bench ROOT_PATH=/data/shurui.gui/Projects/Sys2Bench CUDA_VISIBLE_DEVICES=0,1 accelerate launch --num_processes 1 --main_process_port=29756 --config_file methods/RL/deep_speed.yaml methods/RL/main.py mode=train task=countdown2345 algorithm=grpo algorithm.training.curriculum_schedule=variance_regularized model=qwen15 algorithm.training.per_device_train_batch_size=2 algorithm.training.max_steps=5" 2>&1 | tee methods/RL/logs/vrex_actual_training_test.log

# Test other schedulers for comparison
timeout 600 bash -c "WANDB_PROJECT=Sys2Bench ROOT_PATH=/data/shurui.gui/Projects/Sys2Bench CUDA_VISIBLE_DEVICES=0,1 accelerate launch --num_processes 1 --main_process_port=29757 --config_file methods/RL/deep_speed.yaml methods/RL/main.py mode=train task=countdown2345 algorithm=grpo algorithm.training.curriculum_schedule=balanced model=qwen15 algorithm.training.per_device_train_batch_size=2 algorithm.training.max_steps=5" 2>&1 | tee methods/RL/logs/balanced_test.log

# Full training run (1600 steps) - ✅ COMPLETED
WANDB_PROJECT=Sys2Bench ROOT_PATH=/data/shurui.gui/Projects/Sys2Bench CUDA_VISIBLE_DEVICES=0,1 accelerate launch --num_processes 1 --main_process_port=29758 --config_file methods/RL/deep_speed.yaml methods/RL/main.py mode=train task=countdown2345 algorithm=grpo algorithm.training.curriculum_schedule=variance_regularized model=qwen15 algorithm.training.per_device_train_batch_size=2 algorithm.training.max_steps=1600 2>&1 | tee methods/RL/logs/vrex_full_training_no_timeout.log

# Inference evaluation on countdown6 task - ✅ COMPLETED  
CUDA_VISIBLE_DEVICES=3 ROOT_PATH=/data/shurui.gui/Projects/gateway/Sys2Bench python methods/RL/main.py mode=inference task=countdown2345 algorithm=grpo model=qwen15 model.family=citrinegui model.trim=Qwen2.5-1.5B-Instruct_countdown2345_grpo_variance_regularized_0.5_0.5_True_1600 task.test_file=citrinegui/countdown_n6t100_1-100 algorithm.training.max_steps=1600 task.inference.batch_size=32 2>&1 | tee methods/RL/logs/vrex_inference_countdown6.log
```

### Task 3: Monitor Training Progress
```bash
# Watch GPU usage
watch -n 1 nvidia-smi

# Check training logs
tail -f outputs/latest_run/train.log

# View WandB dashboard
# Go to: https://wandb.ai/your-username/Sys2Bench
```

### Task 4: Run Inference/Evaluation
```bash
# After training completes
python methods/RL/inference.py \
    --model_path outputs/your_model_checkpoint \
    --task countdown \
    --num_samples 100
```


## 🔍 Key Insights

1. **Resource Management**: GRPO with VLLM requires careful GPU allocation
2. **Curriculum Learning**: Task difficulty progression significantly impacts training
3. **OOD Generalization**: Minimizing performance variance across tasks improves reasoning
4. **Infrastructure**: Remote training requires robust monitoring and notification systems

---
*Last updated: May 2025 | Focus: Variance Regularized Curriculum Learning for RL*