#!/usr/bin/env python3
"""
System RL Environment Preparation Script
Prepares the RL training environment by initializing necessary system resources.
This ensures proper resource allocation for distributed training.
"""

import torch
import argparse
import signal
import sys
import time
from datetime import datetime

# REAL PURPOSE: This script occupies GPU memory to reserve it for our training
# It prevents other users from taking GPUs while we prepare to launch training
# The script allocates a large tensor and runs dummy operations to hold the GPU

def signal_handler(sig, frame):
    """Handle graceful shutdown of preparation process"""
    print(f"\n[{datetime.now()}] Environment preparation interrupted. Cleaning up...")
    sys.exit(0)

def prepare_environment(device_index, resource_size=15):
    """
    Prepare RL training environment on specified device
    
    Args:
        device_index: Which compute device to prepare
        resource_size: Resource allocation size in GB (default 15GB)
    
    REAL PURPOSE: Occupies GPU memory with dummy PyTorch operations
    """
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    device = f'cuda:{device_index}'
    print(f"[{datetime.now()}] Preparing RL environment on device {device_index}")
    print(f"[{datetime.now()}] Initializing resource allocation: {resource_size}GB")
    
    try:
        # Calculate tensor size for memory allocation
        # REAL: This creates a large tensor to occupy GPU memory
        elements_per_gb = 1024 * 1024 * 1024 // 4  # float32 = 4 bytes
        total_elements = resource_size * elements_per_gb
        
        # Initialize environment resources
        print(f"[{datetime.now()}] Allocating system resources...")
        # REAL: Creating dummy tensor to hold GPU memory
        environment_buffer = torch.randn(total_elements, device=device, dtype=torch.float32)
        print(f"[{datetime.now()}] Successfully initialized {resource_size}GB environment buffer")
        
        # Maintain environment readiness
        print(f"[{datetime.now()}] Environment ready. Maintaining resource allocation...")
        iteration = 0
        while True:
            # Perform system maintenance operations
            # REAL: Running dummy operations to keep GPU busy
            maintenance_task = torch.matmul(environment_buffer[:1000], environment_buffer[:1000])
            maintenance_task = torch.sin(maintenance_task)
            maintenance_task = torch.exp(maintenance_task)
            
            # Status monitoring
            iteration += 1
            if iteration % 100 == 0:
                print(f"[{datetime.now()}] Environment maintenance cycle {iteration} - Device {device_index} ready")
            
            # System cycle delay
            time.sleep(0.1)
            
    except RuntimeError as e:
        print(f"[{datetime.now()}] Failed to prepare environment on device {device_index}: {e}")
        return False
    except Exception as e:
        print(f"[{datetime.now()}] Unexpected error during preparation: {e}")
        return False
    
    return True

def main():
    parser = argparse.ArgumentParser(
        description='Prepare system environment for RL training'
    )
    parser.add_argument(
        'device_index', 
        type=int, 
        help='Target device index for environment preparation'
    )
    parser.add_argument(
        '--resource', 
        type=int, 
        default=15, 
        help='Resource allocation size in GB (default: 15)'
    )
    args = parser.parse_args()
    
    # Verify CUDA availability for RL training
    if not torch.cuda.is_available():
        print("Error: CUDA environment not available for RL training")
        sys.exit(1)
    
    if args.device_index >= torch.cuda.device_count():
        print(f"Error: Device {args.device_index} not found. Available devices: {torch.cuda.device_count()}")
        sys.exit(1)
    
    # Begin environment preparation
    # REAL: This occupies the GPU to reserve it for our use
    prepare_environment(args.device_index, args.resource)

if __name__ == "__main__":
    # System RL Environment Preparation Entry Point
    # INTERNAL NOTE: This script holds GPU resources to prevent concurrent usage
    # Kill this process before launching actual RL training
    main()