#!/bin/bash
# Activate AI Brain environment
source /mnt/projects/ai-brain/venv/bin/activate
export AI_BRAIN_HOME=/mnt/projects/ai-brain
export PYTHONPATH=$AI_BRAIN_HOME:$PYTHONPATH
echo "🧠 AI Brain environment activated"
echo "Location: $AI_BRAIN_HOME"
echo "Python: $(which python3)"
