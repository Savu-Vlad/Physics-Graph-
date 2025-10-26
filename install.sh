#!/usr/bin/env bash
set -euo pipefail

# Change this if your main file has a different name
APP_MAIN="graph_physics.py"

# 1) Create venv if missing
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

# 2) Activate venv
# shellcheck disable=SC1091
source .venv/bin/activate

# 3) Upgrade pip & install deps
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo "✔ Virtual env ready at .venv"
echo "   To run: ./run.sh"
echo
echo "If you see a Tk error like 'libtk8.6.so missing' on Arch:"
echo "  sudo pacman -S tk"
echo
# small sanity check: warn if main file not found
if [ ! -f "$APP_MAIN" ]; then
  echo "⚠ Note: $APP_MAIN not found in current dir."
fi
