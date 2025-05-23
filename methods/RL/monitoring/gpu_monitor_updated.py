#!/usr/bin/env python3
"""
GPU Monitor Script for GRPO Training - Updated Version
Monitors GPU availability and creates notifications when suitable GPUs are available
"""

import subprocess
import time
from datetime import datetime
import os
import sys

def check_gpu_availability(min_free_memory_gb=20, num_gpus_needed=2):
    """
    Check if enough GPUs are available with sufficient free memory
    """
    try:
        cmd = "nvidia-smi --query-gpu=index,memory.free --format=csv,noheader,nounits"
        result = subprocess.run(cmd.split(), capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Error running nvidia-smi: {result.stderr}")
            return False, []
        
        # Parse GPU info
        available_gpus = []
        for line in result.stdout.strip().split('\n'):
            gpu_id, free_memory_mb = line.split(', ')
            free_memory_gb = float(free_memory_mb) / 1024
            
            if free_memory_gb >= min_free_memory_gb:
                available_gpus.append((int(gpu_id), free_memory_gb))
        
        # Check if we have enough GPUs
        if len(available_gpus) >= num_gpus_needed:
            return True, available_gpus[:num_gpus_needed]
        else:
            return False, available_gpus
            
    except Exception as e:
        print(f"Error checking GPU availability: {e}")
        return False, []

def create_notification(recipient_email, available_gpus, server_name="dive7.engr.tamu.edu"):
    """
    Create notification files when GPUs are available
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Create a highly visible notification file
    notification_dir = "/data/shurui.gui/Projects/Sys2Bench/methods/RL"
    notification_file = os.path.join(notification_dir, f"GPU_READY_{timestamp}.txt")
    ready_flag_file = os.path.join(notification_dir, "GPU_READY_FLAG.txt")
    
    gpu_list = "\n".join([f"  - GPU {gpu_id}: {free_gb:.1f} GB free" for gpu_id, free_gb in available_gpus])
    
    command = f"""WANDB_PROJECT=Sys2Bench-VarReg ROOT_PATH=/data/shurui.gui/Projects/Sys2Bench CUDA_VISIBLE_DEVICES={available_gpus[0][0]},{available_gpus[1][0]} accelerate launch \\
    --num_processes 1 \\
    --main_process_port=29850 \\
    --config_file methods/RL/deep_speed.yaml \\
    methods/RL/main.py \\
    mode=train \\
    task=countdown6 \\
    algorithm=grpo \\
    algorithm.training.curriculum_schedule=variance_regularized \\
    model=qwen15 \\
    algorithm.training.per_device_train_batch_size=2 \\
    algorithm.training.scheduler_params.min_prob=0.1 \\
    algorithm.training.scheduler_params.temperature=1.0 \\
    algorithm.training.scheduler_params.beta=0.7 \\
    algorithm.training.scheduler_params.warmup_steps=100 \\
    algorithm.training.scheduler_params.vrex_penalty_weight=1.0 \\
    algorithm.training.scheduler_params.groupdro_alpha=0.01 \\
    algorithm.training.scheduler_params.window_size=100 \\
    algorithm.training.max_steps=1600"""
    
    body = f"""🎉 GPUs ARE NOW AVAILABLE FOR VARIANCE REGULARIZED TRAINING! 🎉

Server: {server_name}
Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Available GPUs:
{gpu_list}

Ready to run command:
{command}

To start training:
1. cd /data/shurui.gui/Projects/Sys2Bench
2. source /data/shurui.gui/mambaforge/etc/profile.d/conda.sh
3. conda activate sys2bench
4. Run the command above

Recipient: {recipient_email}
"""
    
    # Write main notification
    with open(notification_file, 'w') as f:
        f.write(body)
    
    # Write flag file for easy checking
    with open(ready_flag_file, 'w') as f:
        f.write(f"GPUs READY at {datetime.now()}\n")
        f.write(f"GPU {available_gpus[0][0]} and GPU {available_gpus[1][0]} available\n")
    
    # Also create a script that can be directly executed
    script_file = os.path.join(notification_dir, f"run_training_{timestamp}.sh")
    with open(script_file, 'w') as f:
        f.write("#!/bin/bash\n")
        f.write("cd /data/shurui.gui/Projects/Sys2Bench\n")
        f.write("source /data/shurui.gui/mambaforge/etc/profile.d/conda.sh\n")
        f.write("conda activate sys2bench\n")
        f.write(command + "\n")
    
    os.chmod(script_file, 0o755)
    
    print("\n" + "="*80)
    print("🚀 GPU NOTIFICATION - READY FOR TRAINING! 🚀")
    print("="*80)
    print(body)
    print("="*80)
    print(f"\nNotification files created:")
    print(f"  - Main notification: {notification_file}")
    print(f"  - Flag file: {ready_flag_file}")
    print(f"  - Executable script: {script_file}")
    print(f"\nYou can run the training directly with:")
    print(f"  bash {script_file}")
    
    return notification_file

def monitor_gpus(recipient_email="citrinegui@gmail.com", 
                 check_interval_seconds=300,  # Check every 5 minutes
                 min_free_memory_gb=20,
                 num_gpus_needed=2):
    """
    Monitor GPUs and create notification when available
    """
    print(f"Starting GPU monitor...")
    print(f"Looking for {num_gpus_needed} GPUs with at least {min_free_memory_gb}GB free memory")
    print(f"Will check every {check_interval_seconds} seconds")
    print(f"Notification for: {recipient_email}")
    print("-" * 80)
    
    check_count = 0
    while True:
        check_count += 1
        print(f"\nCheck #{check_count} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        available, gpu_info = check_gpu_availability(min_free_memory_gb, num_gpus_needed)
        
        if available:
            print(f"✓ Found {len(gpu_info)} suitable GPUs!")
            notification_file = create_notification(recipient_email, gpu_info)
            
            # Try to send a system message if possible
            try:
                # Create a message that will be visible when you log in
                message = f"GPU READY: {len(gpu_info)} GPUs available for training!"
                wall_cmd = f'echo "{message}" | wall'
                subprocess.run(wall_cmd, shell=True, capture_output=True)
            except:
                pass
            
            print("\nMonitoring complete. GPUs are ready for training!")
            print("Check the notification files or run the generated script to start training.")
            break
        else:
            print(f"✗ Only {len(gpu_info)} GPUs available (need {num_gpus_needed})")
            if gpu_info:
                print("  Available GPUs with sufficient memory:")
                for gpu_id, free_gb in gpu_info:
                    print(f"    - GPU {gpu_id}: {free_gb:.1f} GB free")
            else:
                print("  No GPUs with sufficient memory available")
            print(f"  Waiting {check_interval_seconds} seconds before next check...")
            time.sleep(check_interval_seconds)

if __name__ == "__main__":
    # Configuration
    RECIPIENT_EMAIL = "citrinegui@gmail.com"
    CHECK_INTERVAL = 300  # 5 minutes
    MIN_FREE_MEMORY_GB = 20  # Need at least 20GB free for VLLM
    NUM_GPUS_NEEDED = 2  # Need 2 GPUs for training
    
    # Allow command line arguments
    if len(sys.argv) > 1:
        RECIPIENT_EMAIL = sys.argv[1]
    
    print("GPU Monitor for Variance Regularized Training")
    print("=" * 80)
    
    try:
        monitor_gpus(
            recipient_email=RECIPIENT_EMAIL,
            check_interval_seconds=CHECK_INTERVAL,
            min_free_memory_gb=MIN_FREE_MEMORY_GB,
            num_gpus_needed=NUM_GPUS_NEEDED
        )
    except KeyboardInterrupt:
        print("\n\nMonitoring stopped by user.")
    except Exception as e:
        print(f"\nError during monitoring: {e}")