#!/bin/bash

#SBATCH --job-name=TrainReasoner
#SBATCH --nodes=1
#SBATCH --time=0-8:00:00
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --gres=gpu:a100:2
#SBATCH --partition=gpu
#SBATCH --mem=16G
#SBATCH --overcommit 
#SBATCH --output=logs/%j.log


echo "$(date '+%Y-%m-%d %H:%M:%S') Job ${SLURM_JOB_ID} started ..."


ml CUDA
ml WebProxy
ml Miniconda3
source /sw/eb/sw/Miniconda3/23.10.0-1/etc/profile.d/conda.sh
conda activate sys2bench_env
cd $SCRATCH/projects/Sys2Bench


ROOT_PATH="$SCRATCH/projects/Sys2Bench" \
accelerate launch \
--mixed_precision bf16 \
--num_processes 1 \
--num_machines 1 \
--use_deepspeed \
--gpu_ids 0,1 \
--zero_stage 3 \
--offload_optimizer_device none \
--offload_param_device none \
--gradient_accumulation_steps 4 \
--zero3_init_flag true \
--dynamo_backend no \
methods/RL/main.py \
model=qwen15 \
task=aqua \
algorithm.training.curriculum_schedule=balanced \
algorithm.training.max_steps=1600 \
algorithm.training.report_to=\[tensorboard\] \
algorithm.training.save_strategy=no \
algorithm.training.push_to_hub=false \
algorithm.training.tf32=true \
algorithm.training.per_device_train_batch_size=1 \
algorithm.training.vllm_gpu_memory_utilization=0.7 \
task.training.max_prompt_length=400 \
task.training.max_completion_length=512


echo "$(date '+%Y-%m-%d %H:%M:%S') Job ${SLURM_JOB_ID} stopped ..."
