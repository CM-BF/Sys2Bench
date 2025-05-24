#!/bin/bash

echo "=== Starting GPU Monitor in Screen Session ==="

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

# Create a script that will run in screen with proper environment
cat > run_monitor_in_screen.sh << 'EOF'
#!/bin/bash
source /data/shurui.gui/mambaforge/etc/profile.d/conda.sh
conda activate sys2bench
cd /data/shurui.gui/Projects/Sys2Bench
echo "[$(date)] Starting RL Environment Monitor with improved sys_rl.py"
echo "Monitor PID: $$"
python methods/RL/monitoring/rl_environment_monitor_immediate.py 2>&1 | tee -a gpu_monitor_screen.log
EOF

chmod +x run_monitor_in_screen.sh

# Start screen session with the monitor
echo "Starting monitor in screen session 'claude'..."
screen -dmS claude bash run_monitor_in_screen.sh

# Give it a moment to start
sleep 3

# Check if it's running
if screen -ls | grep -q "claude"; then
    echo "✓ Monitor started successfully in screen session 'claude'"
    echo ""
    echo "To view the monitor:"
    echo "  screen -r claude"
    echo ""
    echo "To detach from screen:"
    echo "  Press Ctrl+A, then D"
    echo ""
    echo "To stop the monitor:"
    echo "  screen -S claude -X quit"
else
    echo "✗ Failed to start monitor in screen session"
    exit 1
fi

# Check current status
echo ""
echo "Current GPU status:"
nvidia-smi --query-gpu=index,memory.used,memory.free,utilization.gpu --format=csv

echo ""
echo "Active processes:"
ps aux | grep -E "(rl_environment_monitor|sys_rl\.py)" | grep -v grep || echo "No processes found yet"