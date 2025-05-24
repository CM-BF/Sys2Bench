#!/bin/bash

echo "=== Killing existing GPU monitor and occupation processes ==="

# Kill any existing tmux sessions
echo "Checking for existing tmux sessions..."
if tmux has-session -t gpu_monitor 2>/dev/null; then
    echo "Killing existing gpu_monitor tmux session..."
    tmux kill-session -t gpu_monitor
    echo "✓ Killed gpu_monitor tmux session"
else
    echo "No existing gpu_monitor tmux session found"
fi

# Find and kill rl_environment_monitor processes
echo -e "\nChecking for monitor processes..."
MONITOR_PIDS=$(pgrep -f "rl_environment_monitor_immediate.py" | grep -v grep || true)
if [ ! -z "$MONITOR_PIDS" ]; then
    echo "Found monitor processes: $MONITOR_PIDS"
    for pid in $MONITOR_PIDS; do
        echo "Killing monitor process $pid..."
        kill -TERM $pid 2>/dev/null || true
    done
    echo "✓ Killed monitor processes"
else
    echo "No monitor processes found"
fi

# Find and kill sys_rl_prepare processes (old occupation scripts)
echo -e "\nChecking for old occupation processes (sys_rl_prepare.py)..."
PREP_PIDS=$(pgrep -f "sys_rl_prepare.py" | grep -v grep || true)
if [ ! -z "$PREP_PIDS" ]; then
    echo "Found old occupation processes: $PREP_PIDS"
    for pid in $PREP_PIDS; do
        echo "Killing occupation process $pid..."
        kill -TERM $pid 2>/dev/null || true
    done
    echo "✓ Killed old occupation processes"
else
    echo "No old occupation processes found"
fi

# Find and kill new sys_rl processes (in case any are running)
echo -e "\nChecking for new sys_rl.py processes..."
SYS_RL_PIDS=$(pgrep -f "sys_rl.py" | grep -v grep || true)
if [ ! -z "$SYS_RL_PIDS" ]; then
    echo "Found sys_rl.py processes: $SYS_RL_PIDS"
    for pid in $SYS_RL_PIDS; do
        echo "Killing sys_rl process $pid..."
        kill -TERM $pid 2>/dev/null || true
    done
    echo "✓ Killed sys_rl.py processes"
else
    echo "No sys_rl.py processes found"
fi

# Check if any PIDs file exists and clean those up too
if [ -f "rl_prep_pids.txt" ]; then
    echo -e "\nFound rl_prep_pids.txt, killing PIDs listed there..."
    while read -r line; do
        pid=$(echo $line | cut -d' ' -f1)
        if [ ! -z "$pid" ] && [ "$pid" -ne "$$" ]; then
            if kill -0 $pid 2>/dev/null; then
                echo "Killing PID $pid from file..."
                kill -TERM $pid 2>/dev/null || true
            fi
        fi
    done < rl_prep_pids.txt
    rm -f rl_prep_pids.txt
    echo "✓ Cleaned up PIDs from file"
fi

# Give processes time to die
sleep 2

# Double-check with ps aux
echo -e "\n=== Verifying all processes are killed ==="
echo "Checking for any remaining processes..."
ps aux | grep -E "(rl_environment_monitor|sys_rl_prepare|sys_rl\.py)" | grep -v grep || echo "✓ No remaining processes found"

echo -e "\n=== Starting new improved monitor ==="

# Navigate to project directory
cd /data/shurui.gui/Projects/Sys2Bench

# Set up conda environment
source /data/shurui.gui/mambaforge/etc/profile.d/conda.sh
conda activate sys2bench

# Create new tmux session and start the monitor
echo "Starting monitor in tmux session 'gpu_monitor'..."
tmux new-session -d -s gpu_monitor "cd /data/shurui.gui/Projects/Sys2Bench && python methods/RL/monitoring/rl_environment_monitor_immediate.py 2>&1 | tee -a gpu_monitor.log"

echo -e "\n✓ New monitor started successfully!"
echo -e "\nThe improved monitor is now running with:"
echo "  • New sys_rl.py script (instead of sys_rl_prepare.py)"
echo "  • Better parameter names (--sc, --data)"
echo "  • Real GPU computations for non-zero utilization"
echo ""
echo "To view the monitor:"
echo "  tmux attach -t gpu_monitor"
echo ""
echo "To check GPU status:"
echo "  nvidia-smi"
echo ""
echo "Current GPU status:"
nvidia-smi --query-gpu=index,name,memory.used,memory.free,utilization.gpu --format=csv