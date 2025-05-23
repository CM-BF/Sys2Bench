#!/bin/bash
# Script to restart GPU monitor with occupation feature

echo "Restarting GPU monitor with automatic occupation..."

# Kill existing monitor if running
if [ -f "gpu_monitor.pid" ]; then
    OLD_PID=$(cat gpu_monitor.pid)
    echo "Killing old monitor (PID: $OLD_PID)..."
    kill $OLD_PID 2>/dev/null
    rm gpu_monitor.pid
fi

# Kill any existing occupier processes
if [ -f "gpu_occupier_pids.txt" ]; then
    echo "Killing existing GPU occupiers..."
    cat gpu_occupier_pids.txt | xargs kill 2>/dev/null
    rm gpu_occupier_pids.txt
fi

# Start new monitor with occupation in background
echo "Starting new GPU monitor with occupation feature..."
cd /data/shurui.gui/Projects/Sys2Bench
nohup python methods/RL/monitoring/gpu_monitor_occupy.py > gpu_monitor_occupy.log 2>&1 &
NEW_PID=$!

# Save PID
echo $NEW_PID > gpu_monitor.pid
echo "✓ New monitor started with PID: $NEW_PID"
echo "  Log file: gpu_monitor_occupy.log"
echo ""
echo "The monitor will:"
echo "1. Check for available GPUs every 5 minutes"
echo "2. Automatically occupy 2 GPUs with 15GB each when found"
echo "3. Send email notification when GPUs are secured"
echo "4. Keep GPUs occupied until you're ready to run training"
echo ""
echo "To check status: tail -f gpu_monitor_occupy.log"
echo "To stop monitor: kill $(cat gpu_monitor.pid)"