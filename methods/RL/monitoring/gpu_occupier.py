#!/usr/bin/env python3
"""
GPU Occupier Script
Occupies a GPU with dummy PyTorch operations to reserve it for our training.
"""

import torch
import argparse
import signal
import sys
import time
from datetime import datetime

def signal_handler(sig, frame):
    """Handle graceful shutdown"""
    print(f"\n[{datetime.now()}] Received shutdown signal. Cleaning up...")
    sys.exit(0)

def occupy_gpu(gpu_index, memory_gb=15):
    """
    Occupy a GPU with dummy operations
    
    Args:
        gpu_index: Which GPU to occupy
        memory_gb: How many GB to allocate (default 15GB)
    """
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    device = f'cuda:{gpu_index}'
    print(f"[{datetime.now()}] Occupying GPU {gpu_index} with ~{memory_gb}GB memory")
    
    try:
        # Calculate tensor size (float32 = 4 bytes per element)
        elements_per_gb = 1024 * 1024 * 1024 // 4
        total_elements = memory_gb * elements_per_gb
        
        # Create large tensor on GPU
        print(f"[{datetime.now()}] Allocating tensor with {total_elements:,} elements...")
        dummy_tensor = torch.randn(total_elements, device=device, dtype=torch.float32)
        print(f"[{datetime.now()}] Successfully allocated {memory_gb}GB on GPU {gpu_index}")
        
        # Run dummy operations in a loop
        iteration = 0
        while True:
            # Perform some operations to keep GPU busy
            result = torch.matmul(dummy_tensor[:1000], dummy_tensor[:1000])
            result = torch.sin(result)
            result = torch.exp(result)
            
            # Occasional status update
            iteration += 1
            if iteration % 100 == 0:
                print(f"[{datetime.now()}] GPU {gpu_index} occupied - iteration {iteration}")
            
            # Small sleep to not be too aggressive
            time.sleep(0.1)
            
    except RuntimeError as e:
        print(f"[{datetime.now()}] Error occupying GPU {gpu_index}: {e}")
        return False
    except Exception as e:
        print(f"[{datetime.now()}] Unexpected error: {e}")
        return False
    
    return True

def main():
    parser = argparse.ArgumentParser(description='Occupy a GPU with dummy operations')
    parser.add_argument('gpu_index', type=int, help='GPU index to occupy')
    parser.add_argument('--memory', type=int, default=15, help='GB of memory to allocate (default: 15)')
    args = parser.parse_args()
    
    if not torch.cuda.is_available():
        print("Error: CUDA is not available")
        sys.exit(1)
    
    if args.gpu_index >= torch.cuda.device_count():
        print(f"Error: GPU {args.gpu_index} not found. Available GPUs: {torch.cuda.device_count()}")
        sys.exit(1)
    
    occupy_gpu(args.gpu_index, args.memory)

if __name__ == "__main__":
    main()