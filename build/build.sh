#!/usr/bin/env bash

set -euo pipefail

python3 -m venv buildproj
. buildproj/bin/activate

pip install --upgrade pip
pip install -r requirements.txt --force-reinstall --upgrade

python3 -m ipykernel install --user --name=buildproj

python3 a_build_ui.py
python3 c_detect_and_apply_changes.py
python3 b_extract_vars.py

deactivate

rm -rf buildproj