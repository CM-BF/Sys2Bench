#!/usr/bin/env python3
"""
GPU Monitor with Automatic Occupation
Monitors GPU availability and automatically occupies them to reserve for training
"""

import subprocess
import time
import smtplib
import ssl
import json
import os
import signal
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from cryptography.fernet import Fernet

# Global variables for cleanup
prep_processes = []

def signal_handler(sig, frame):
    """Handle cleanup on exit"""
    print(f"\n[{datetime.now()}] Received shutdown signal. Cleaning up...")
    cleanup_prep_processes()
    sys.exit(0)

def cleanup_prep_processes():
    """Kill all preparation processes"""
    for proc in prep_processes:
        if proc.poll() is None:  # Process is still running
            print(f"Terminating preparation process {proc.pid}")
            proc.terminate()
            proc.wait()
    prep_processes.clear()

def load_email_config():
    """Load email configuration from encrypted storage"""
    config_dir = os.path.expanduser("~/.sys2bench")
    config_file = os.path.join(config_dir, "email_config.json")
    key_file = os.path.join(config_dir, "email.key")
    
    if not os.path.exists(config_file) or not os.path.exists(key_file):
        raise FileNotFoundError(
            "Email configuration not found. Please run setup_email.py first."
        )
    
    # Load encryption key
    with open(key_file, 'rb') as f:
        key = f.read()
    cipher_suite = Fernet(key)
    
    # Load config
    with open(config_file, 'r') as f:
        config = json.load(f)
    
    # Decrypt password
    config['password'] = cipher_suite.decrypt(
        config['encrypted_password'].encode()
    ).decode()
    
    return config

def check_gpu_availability(min_free_memory_gb=20, num_gpus_needed=2):
    """Check if enough GPUs are available with sufficient free memory"""
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
        
        if len(available_gpus) >= num_gpus_needed:
            return True, available_gpus[:num_gpus_needed]
        else:
            return False, available_gpus
            
    except Exception as e:
        print(f"Error checking GPU availability: {e}")
        return False, []

def prepare_gpus(gpu_list, memory_per_gpu=15):
    """Start environment preparation processes for given GPUs"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    prep_script = os.path.join(script_dir, "sys_rl_prepare.py")
    
    # Make sure the preparation script exists
    if not os.path.exists(prep_script):
        print(f"Error: RL preparation script not found at {prep_script}")
        return False
    
    # Start preparation process for each GPU
    for gpu_id, free_gb in gpu_list:
        print(f"Starting RL environment preparation on GPU {gpu_id}...")
        
        # Python command that will work on the remote system
        python_cmd = "python3"
        
        cmd = [python_cmd, prep_script, str(gpu_id), "--resource", str(memory_per_gpu)]
        
        try:
            # Start the process in the background
            proc = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                preexec_fn=os.setsid  # Create new process group for easier cleanup
            )
            prep_processes.append(proc)
            print(f"✓ RL environment preparation started for GPU {gpu_id} (PID: {proc.pid})")
            
            # Give it a moment to allocate memory
            time.sleep(2)
            
            # Check if process is still running
            if proc.poll() is not None:
                stdout, stderr = proc.communicate()
                print(f"✗ Environment preparation failed for GPU {gpu_id}")
                print(f"  stdout: {stdout.decode()}")
                print(f"  stderr: {stderr.decode()}")
                return False
                
        except Exception as e:
            print(f"Error starting RL preparation for GPU {gpu_id}: {e}")
            return False
    
    print(f"\n✓ Successfully prepared {len(gpu_list)} GPUs!")
    return True

def save_preparation_pids():
    """Save preparation PIDs to file for later cleanup"""
    pid_file = "rl_prep_pids.txt"
    with open(pid_file, 'w') as f:
        for proc in prep_processes:
            f.write(f"{proc.pid}\n")
    print(f"Preparation PIDs saved to {pid_file}")

def send_email_notification(config, prepared_gpus, server_name="dive7.engr.tamu.edu"):
    """Send email notification when GPUs are prepared and ready"""
    
    gpu_list = "\n".join([f"  - GPU {gpu_id}: {free_gb:.1f} GB free (now prepared)" 
                         for gpu_id, free_gb in prepared_gpus])
    
    subject = f"GPUs Secured on {server_name} - Ready for Variance Regularized Training"
    
    # Handle both single GPU (test) and dual GPU cases
    if len(prepared_gpus) >= 2:
        cuda_devices = f"{prepared_gpus[0][0]},{prepared_gpus[1][0]}"
    else:
        cuda_devices = f"{prepared_gpus[0][0]}"
    
    command = f"""WANDB_PROJECT=Sys2Bench-VarReg ROOT_PATH=/data/shurui.gui/Projects/Sys2Bench CUDA_VISIBLE_DEVICES={cuda_devices} accelerate launch \\
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
    
    # Add test indication if only 1 GPU
    test_note = " (TEST MODE)" if len(prepared_gpus) == 1 else ""
    
    body = f"""Good news! The required GPUs have been secured on {server_name} for your variance regularized curriculum training{test_note}.

Prepared GPUs:
{gpu_list}

⚠️ IMPORTANT: The GPUs are currently being held by preparation processes to prevent others from using them.

To run your training:
1. SSH to {server_name}
2. Kill the preparation processes:
   cat rl_prep_pids.txt | xargs kill
3. cd /data/shurui.gui/Projects/Sys2Bench
4. source /data/shurui.gui/mambaforge/etc/profile.d/conda.sh
5. conda activate sys2bench
6. Run the training command:

{command}

Preparation PIDs for reference:
{', '.join(str(proc.pid) for proc in prep_processes)}

Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

This is an automated notification from the GPU monitor.
"""
    
    # Create message
    message = MIMEMultipart()
    message["From"] = config['sender_email']
    message["To"] = config['recipient_email']
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    
    # Send email
    try:
        if config['use_tls']:
            # TLS connection
            context = ssl.create_default_context()
            with smtplib.SMTP(config['smtp_server'], config['smtp_port']) as server:
                server.starttls(context=context)
                server.login(config['sender_email'], config['password'])
                server.send_message(message)
        else:
            # SSL connection
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(config['smtp_server'], config['smtp_port'], 
                                   context=context) as server:
                server.login(config['sender_email'], config['password'])
                server.send_message(message)
        
        print(f"✓ Email sent successfully to {config['recipient_email']}")
        return True
        
    except Exception as e:
        print(f"✗ Failed to send email: {e}")
        # Save notification locally as backup
        backup_file = f"gpu_notification_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(backup_file, 'w') as f:
            f.write(f"Subject: {subject}\n\n{body}")
        print(f"  Notification saved locally to: {backup_file}")
        return False

def monitor_and_prepare_gpus(check_interval_seconds=300, min_free_memory_gb=20, 
                           num_gpus_needed=2, memory_to_prepare=15):
    """Monitor GPUs and automatically prepare them when available"""
    
    # Set up signal handlers for cleanup
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Load email configuration
    try:
        email_config = load_email_config()
        print(f"✓ Email configuration loaded")
        print(f"  Will send notifications to: {email_config['recipient_email']}")
    except Exception as e:
        print(f"✗ Error loading email configuration: {e}")
        print("  Please run setup_email.py first to configure email settings")
        return
    
    print(f"\nStarting GPU monitor with automatic occupation...")
    print(f"Looking for {num_gpus_needed} GPUs with at least {min_free_memory_gb}GB free memory")
    print(f"Will prepare with {memory_to_prepare}GB per GPU when found")
    print(f"Will check every {check_interval_seconds} seconds")
    print("-" * 60)
    
    check_count = 0
    while True:
        check_count += 1
        print(f"\nCheck #{check_count} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        available, gpu_info = check_gpu_availability(min_free_memory_gb, num_gpus_needed)
        
        if available:
            print(f"✓ Found {len(gpu_info)} suitable GPUs!")
            print("Attempting to prepare GPUs...")
            
            # Try to prepare the GPUs
            if prepare_gpus(gpu_info, memory_to_prepare):
                # Save PIDs for later cleanup
                save_preparation_pids()
                
                # Send email notification
                email_sent = send_email_notification(email_config, gpu_info)
                
                if email_sent:
                    print("\n🎉 Email notification sent successfully!")
                else:
                    print("\n⚠️  Email sending failed, but notification was saved locally")
                
                print("\n✓ GPUs are prepared and ready for training!")
                print("  Remember to kill the preparation processes before running training:")
                print("  cat rl_prep_pids.txt | xargs kill")
                
                # Keep the monitor running to maintain the preparation processes
                print("\nMonitor will continue running to maintain GPU occupation.")
                print("Press Ctrl+C to stop the monitor and release GPUs.")
                
                # Enter maintenance mode - just keep running
                while True:
                    time.sleep(60)  # Check every minute that preparations are still running
                    alive_count = sum(1 for proc in prep_processes if proc.poll() is None)
                    if alive_count < len(prep_processes):
                        print(f"⚠️  Warning: Only {alive_count}/{len(prep_processes)} preparations still running")
                        break
                
            else:
                print("✗ Failed to prepare GPUs, will retry...")
                cleanup_prep_processes()
        else:
            print(f"✗ Only {len(gpu_info)} GPUs available (need {num_gpus_needed})")
            if gpu_info:
                print("  Available GPUs with sufficient memory:")
                for gpu_id, free_gb in gpu_info:
                    print(f"    - GPU {gpu_id}: {free_gb:.1f} GB free")
            print(f"  Waiting {check_interval_seconds} seconds before next check...")
            time.sleep(check_interval_seconds)

if __name__ == "__main__":
    import sys
    
    # Configuration
    CHECK_INTERVAL = 300  # 5 minutes
    MIN_FREE_MEMORY_GB = 20  # Need at least 20GB free for VLLM
    NUM_GPUS_NEEDED = 2  # Need 2 GPUs for training
    MEMORY_TO_OCCUPY = 15  # Prepare 15GB per GPU (leaving some room)
    
    # Allow command line arguments
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        # Test mode - check for just 1 GPU
        print("TEST MODE: Checking for 1 GPU only")
        NUM_GPUS_NEEDED = 1
        CHECK_INTERVAL = 10  # Check every 10 seconds in test mode
    
    print("GPU Monitor with Automatic Occupation")
    print("=" * 60)
    
    try:
        monitor_and_prepare_gpus(
            check_interval_seconds=CHECK_INTERVAL,
            min_free_memory_gb=MIN_FREE_MEMORY_GB,
            num_gpus_needed=NUM_GPUS_NEEDED,
            memory_to_prepare=MEMORY_TO_OCCUPY
        )
    except KeyboardInterrupt:
        print("\n\nMonitoring stopped by user.")
        cleanup_prep_processes()
    except Exception as e:
        print(f"\nError during monitoring: {e}")
        cleanup_prep_processes()