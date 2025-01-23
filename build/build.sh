#!/usr/bin/env bash

set -euo pipefail

python -m venv buildproj
. buildproj/bin/activate

pip install --upgrade pip uv
uv pip install -r requirements.txt --force-reinstall --upgrade

python -m ipykernel install --user --name=buildproj

python a_build_ui_and_code.py
python c_detect_and_apply_changes.py
python b_extract_vars.py


deactivate

rm -rf buildproj/