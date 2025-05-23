#!/bin/bash

# GPU Monitor Launch Script
echo "Starting GPU monitor for variance regularized training..."
echo "Monitor will check every 5 minutes for 2 GPUs with at least 20GB free memory"

# Change to the RL directory
cd /data/shurui.gui/Projects/Sys2Bench/methods/RL

# Activate conda environment
source /data/shurui.gui/mambaforge/etc/profile.d/conda.sh
conda activate sys2bench

# Start the monitor in background with nohup
nohup python gpu_monitor_updated.py citrinegui@gmail.com > gpu_monitor.log 2>&1 &

# Get the process ID
PID=$!
echo "GPU monitor started with PID: $PID"
echo "Monitor log: gpu_monitor.log"
echo ""
echo "Commands:"
echo "  - Check status: tail -f gpu_monitor.log"
echo "  - Check if ready: ls GPU_READY_FLAG.txt"
echo "  - Stop monitor: kill $PID"

# Save PID to file
echo $PID > gpu_monitor.pid

echo ""
echo "When GPUs are available:"
echo "1. A file named GPU_READY_FLAG.txt will be created"
echo "2. An executable script run_training_*.sh will be generated"
echo "3. You can start training by running that script"