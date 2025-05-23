#!/usr/bin/env python3
"""
GPU Monitor Script for GRPO Training
Monitors GPU availability and sends email notification when suitable GPUs are available
"""

import subprocess
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os
import sys

def check_gpu_availability(min_free_memory_gb=20, num_gpus_needed=2):
    """
    Check if enough GPUs are available with sufficient free memory
    
    Args:
        min_free_memory_gb: Minimum free memory in GB required per GPU
        num_gpus_needed: Number of GPUs needed
        
    Returns:
        tuple: (available, gpu_info) where available is bool and gpu_info is list of available GPU indices
    """
    try:
        # Run nvidia-smi to get GPU memory info
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

def send_email_notification(recipient_email, available_gpus, server_name="dive7.engr.tamu.edu"):
    """
    Send email notification when GPUs are available
    
    Note: This uses a simple approach. In production, you might want to use
    a proper email service or configure SMTP settings appropriately.
    """
    subject = f"GPUs Available on {server_name} for Variance Regularized Training"
    
    gpu_list = "\n".join([f"  - GPU {gpu_id}: {free_gb:.1f} GB free" for gpu_id, free_gb in available_gpus])
    
    body = f"""Good news! The required GPUs are now available on {server_name} for your variance regularized curriculum training.

Available GPUs:
{gpu_list}

You can now run the training command:

WANDB_PROJECT=Sys2Bench-VarReg ROOT_PATH=/data/shurui.gui/Projects/Sys2Bench CUDA_VISIBLE_DEVICES={available_gpus[0][0]},{available_gpus[1][0]} accelerate launch \\
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
    algorithm.training.max_steps=1600

Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    # Create a simple notification file instead of email
    # (since we can't send real emails without SMTP credentials)
    notification_file = f"gpu_ready_notification_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(notification_file, 'w') as f:
        f.write(f"To: {recipient_email}\n")
        f.write(f"Subject: {subject}\n\n")
        f.write(body)
    
    print(f"Notification saved to {notification_file}")
    print(f"GPUs are ready! GPU {available_gpus[0][0]} and GPU {available_gpus[1][0]} are available.")
    
    # Also try to send a system notification using mail command if available
    try:
        mail_cmd = f'echo "{body}" | mail -s "{subject}" {recipient_email}'
        subprocess.run(mail_cmd, shell=True, capture_output=True)
        print(f"Email sent to {recipient_email}")
    except:
        print("Could not send email via mail command")
    
    return notification_file

def monitor_gpus(recipient_email="citrinegui@gmail.com", 
                 check_interval_seconds=300,  # Check every 5 minutes
                 min_free_memory_gb=20,
                 num_gpus_needed=2):
    """
    Monitor GPUs and send notification when available
    """
    print(f"Starting GPU monitor...")
    print(f"Looking for {num_gpus_needed} GPUs with at least {min_free_memory_gb}GB free memory")
    print(f"Will check every {check_interval_seconds} seconds")
    print(f"Notification will be sent to: {recipient_email}")
    print("-" * 50)
    
    check_count = 0
    while True:
        check_count += 1
        print(f"\nCheck #{check_count} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        available, gpu_info = check_gpu_availability(min_free_memory_gb, num_gpus_needed)
        
        if available:
            print(f"✓ Found {len(gpu_info)} suitable GPUs!")
            notification_file = send_email_notification(recipient_email, gpu_info)
            print(f"Notification saved to: {notification_file}")
            print("\nMonitoring complete. GPUs are ready for training!")
            break
        else:
            print(f"✗ Only {len(gpu_info)} GPUs available (need {num_gpus_needed})")
            if gpu_info:
                print("  Available GPUs with sufficient memory:")
                for gpu_id, free_gb in gpu_info:
                    print(f"    - GPU {gpu_id}: {free_gb:.1f} GB free")
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
    print("=" * 50)
    
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