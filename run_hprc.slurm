#!/bin/bash

#SBATCH --job-name=TrainReasoner
#SBATCH --account=ASC25013
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --partition=gpu-a100
#SBATCH --time=0-8:00:00
#SBATCH --overcommit 
#SBATCH --output=logs/%j.log


echo "$(date '+%Y-%m-%d %H:%M:%S') Job ${SLURM_JOB_ID} started ..."


mu="0.5"
sigma="0.5"
max_steps="1600"
for i in "$@"; do
  case "$i" in
    --model=*)
      model="${i#*=}"
      ;;
    --task=*)
      task="${i#*=}"
      ;;
    --schedule=*)
      schedule="${i#*=}"
      ;;
    --mu=*)
      mu="${i#*=}"
      ;;
    --sigma=*)
      sigma="${i#*=}"
      ;;
    --max_steps=*)
      max_steps="${i#*=}"
      ;;
  esac
done


source $WORK/miniconda3/etc/profile.d/conda.sh
conda activate sys2bench_env
cd $WORK/projects/Sys2Bench


ROOT_PATH="$WORK/projects/Sys2Bench" \
accelerate launch \
--mixed_precision bf16 \
--num_processes 2 \
--num_machines 1 \
--use_deepspeed \
--gpu_ids all \
--zero_stage 3 \
--offload_optimizer_device none \
--offload_param_device none \
--gradient_accumulation_steps 4 \
--zero3_init_flag true \
--zero3_save_16bit_model true \
--dynamo_backend no \
methods/RL/main.py \
mode=train \
model="$model" \
task="$task" \
algorithm.training.curriculum_schedule="$schedule" \
algorithm.training.scheduler_params.mu_exp="$mu" \
algorithm.training.scheduler_params.sigma="$sigma" \
algorithm.training.max_steps="$max_steps" \
algorithm.training.report_to=\[tensorboard\] \
algorithm.training.push_to_hub=false \
algorithm.training.save_strategy=no \
algorithm.training.vllm_gpu_memory_utilization=0.8


# methods/RL/main.py \
# mode=inference \
# model="$model" \
# task="$task" \
# algorithm.training.curriculum_schedule="$schedule" \
# algorithm.training.scheduler_params.mu_exp="$mu" \
# algorithm.training.scheduler_params.sigma="$sigma" \
# algorithm.training.max_steps="$max_steps" \


echo "$(date '+%Y-%m-%d %H:%M:%S') Job ${SLURM_JOB_ID} stopped ..."
