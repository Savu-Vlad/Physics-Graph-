#!/usr/bin/env bash
set -euo pipefail

APP_MAIN="graph_physics.py"

# Activate venv
source .venv/bin/activate

# Run the app
python "$APP_MAIN"
