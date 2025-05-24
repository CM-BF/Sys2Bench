#!/bin/bash

echo "=== Starting GPU Monitor in Tmux Session ==="

# Kill any existing monitor processes first
echo "Cleaning up any existing processes..."
pkill -f "rl_environment_monitor_immediate.py" 2>/dev/null || true
pkill -f "sys_rl.py" 2>/dev/null || true

# Kill any existing screen sessions named 'claude'
screen -S claude -X quit 2>/dev/null || true

# Remove old PID file
rm -f rl_prep_pids.txt

# Change to project directory
cd /data/shurui.gui/Projects/Sys2Bench

# Set up conda environment
source /data/shurui.gui/mambaforge/etc/profile.d/conda.sh
conda activate sys2bench

# Kill any existing tmux sessions named 'claude'
tmux kill-session -t claude 2>/dev/null || true

# Create new tmux session and start the monitor
echo "Starting monitor in tmux session 'claude'..."
tmux new-session -d -s claude "cd /data/shurui.gui/Projects/Sys2Bench && source /data/shurui.gui/mambaforge/etc/profile.d/conda.sh && conda activate sys2bench && python methods/RL/monitoring/rl_environment_monitor_immediate.py 2>&1 | tee -a gpu_monitor_tmux.log"

# Give it a moment to start
sleep 3

# Check if it's running
if tmux has-session -t claude 2>/dev/null; then
    echo "✓ Monitor started successfully in tmux session 'claude'"
    echo ""
    echo "To view the monitor:"
    echo "  tmux attach -t claude"
    echo ""
    echo "To detach from tmux:"
    echo "  Press Ctrl+B, then D"
    echo ""
    echo "To stop the monitor:"
    echo "  tmux kill-session -t claude"
else
    echo "✗ Failed to start monitor in tmux session"
    exit 1
fi

# Check current status
echo ""
echo "Current GPU status:"
nvidia-smi --query-gpu=index,memory.used,memory.free,utilization.gpu --format=csv

echo ""
echo "Active processes:"
ps aux | grep -E "(rl_environment_monitor|sys_rl\.py)" | grep -v grep || echo "No processes found yet"

echo ""
echo "Tmux sessions:"
tmux ls