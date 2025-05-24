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

# Kill any existing tmux sessions named 'claude' (suppress library warnings)
tmux kill-session -t claude 2>&1 | grep -v "no version information" || true

# Create a wrapper script for the monitor that activates conda
cat > run_monitor_wrapper.sh << 'EOF'
#!/bin/bash
cd /data/shurui.gui/Projects/Sys2Bench
source /data/shurui.gui/mambaforge/etc/profile.d/conda.sh
conda activate sys2bench
echo "[$(date)] Starting RL Environment Monitor with improved sys_rl.py"
python methods/RL/monitoring/rl_environment_monitor_immediate.py 2>&1 | tee -a gpu_monitor_tmux.log
EOF

chmod +x run_monitor_wrapper.sh

# Create new tmux session and start the monitor (suppress library warnings)
echo "Starting monitor in tmux session 'claude'..."
tmux new-session -d -s claude bash run_monitor_wrapper.sh 2>&1 | grep -v "no version information"

# Give it a moment to start
sleep 3

# Check if it's running (suppress library warnings)
if tmux has-session -t claude 2>&1 | grep -v "no version information"; then
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
tmux ls 2>&1 | grep -v "no version information" || echo "No tmux sessions found"