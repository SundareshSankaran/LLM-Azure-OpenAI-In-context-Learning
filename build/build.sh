#!/usr/bin/env bash

set -euo pipefail

python -m venv buildproj
. buildproj/bin/activate

pip install --upgrade pip
pip install -r requirements.txt --force-reinstall --upgrade

python -m ipykernel install --user --name=buildproj

python build_ui.py

deactivate

rm -rf buildproj