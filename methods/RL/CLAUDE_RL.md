# CLAUDE_RL.md

This file provides comprehensive guidance for Claude Code when working with the RL (Reinforcement Learning) components of Sys2Bench.

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

For remote development workflow (editing locally, syncing files, using tmux), see: `/REMOTE_WORKFLOW.md`

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

### 4. **Directory Reorganization**
```
methods/RL/
├── conf/                    # Hydra configurations
├── monitoring/              # GPU monitoring scripts
├── schedulers/              # Curriculum schedulers
├── scripts/                 # Utility and setup scripts
├── utils/                   # Helper files and patches
├── *_reward_model.py        # Task-specific reward models
├── main.py                  # Main training entry point
└── CLAUDE_RL.md            # This documentation
```

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
1. **Wait for GPU availability** - Monitor is running with PID saved in `gpu_monitor.pid`
2. **Run training** when 2 GPUs with 20GB+ free memory are available
3. **Evaluate results** - Compare variance regularized vs. other schedulers

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
# See /REMOTE_WORKFLOW.md for how to sync files and use tmux utilities

# Quick start (using tmux utilities from tmux_utils/):
cd ../../tmux_utils  # From methods/RL/
./run_in_tmux.sh "cd /data/shurui.gui/Projects/Sys2Bench" claude
./run_in_tmux.sh "conda activate sys2bench" claude  
./run_in_tmux.sh "python methods/RL/monitoring/rl_environment_monitor_immediate.py" claude
./check_tmux.sh claude  # Check status
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
ssh shurui.gui@dive7.engr.tamu.edu
cd /data/shurui.gui/Projects/Sys2Bench

# Kill occupation processes
cat rl_prep_pids.txt | xargs kill

# Activate environment
source /data/shurui.gui/mambaforge/etc/profile.d/conda.sh
conda activate sys2bench

# Run training (example with variance regularized scheduler)
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