#!/bin/bash

# GPU Monitor Launch Script
# This script starts the GPU monitor in the background using nohup

echo "Starting GPU monitor for variance regularized training..."
echo "Monitor will check every 5 minutes for 2 GPUs with at least 20GB free memory"
echo "Notification will be sent to: citrinegui@gmail.com"

# Change to the RL directory
cd /data/shurui.gui/Projects/Sys2Bench/methods/RL

# Start the monitor in background with nohup
nohup python gpu_monitor.py citrinegui@gmail.com > gpu_monitor.log 2>&1 &

# Get the process ID
PID=$!
echo "GPU monitor started with PID: $PID"
echo "Monitor log: gpu_monitor.log"
echo ""
echo "To check monitor status: tail -f gpu_monitor.log"
echo "To stop monitor: kill $PID"

# Save PID to file for easy stopping later
echo $PID > gpu_monitor.pid

echo ""
echo "When GPUs become available, you will receive a notification and can run:"
echo "bash train_variance_regularized.sh"