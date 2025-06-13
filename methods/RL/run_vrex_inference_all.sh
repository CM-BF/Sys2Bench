#!/bin/bash

# Run inference for all VREx configurations on all countdown levels
# This script tests generalization across different problem difficulties

ROOT_PATH=/data/shurui.gui/Projects/gateway/Sys2Bench

# Test files for different difficulty levels
declare -a test_files=(
    "citrinegui/countdown_n2t100_1-100"
    "citrinegui/countdown_n3t100_1-100"
    "citrinegui/countdown_n4t100_1-100"
    "citrinegui/countdown_n5t100_1-100"
    "citrinegui/countdown_n6t100_1-100"
)

# Model checkpoints to test (from 400-step runs)
declare -a models=(
    "Qwen2.5-1.5B-Instruct_countdown2345_grpo_variance_regularized_0.5_0.5_True_400"
)

# GPU assignment
gpu_id=4

# Run inference for each model on each test set
for model in "${models[@]}"; do
    for i in "${!test_files[@]}"; do
        test_file="${test_files[$i]}"
        difficulty=$((i + 2))  # 2, 3, 4, 5, 6
        
        echo "Running inference for $model on countdown${difficulty}..."
        
        CUDA_VISIBLE_DEVICES=$gpu_id ROOT_PATH=$ROOT_PATH python methods/RL/main.py \
            mode=inference \
            task=countdown2345 \
            algorithm=grpo \
            model=qwen15 \
            model.family=citrinegui \
            model.trim="$model" \
            task.test_file="$test_file" \
            algorithm.training.max_steps=400 \
            task.inference.batch_size=32 \
            2>&1 | tee "methods/RL/logs/vrex_400_inference_countdown${difficulty}.log"
        
        # Extract and save results
        echo "Completed countdown${difficulty} for $model"
        echo "---"
        
        # Small delay between runs
        sleep 5
    done
done

echo "All inference runs completed!"