#!/bin/bash

# Create a virtual environment in the directory 'venv'
python -m venv venv

# Add a line to set PYTHONPATH in the activation script
echo 'export PYTHONPATH="$(dirname $(realpath $0)):$PYTHONPATH"' >> venv/bin/activate

# Activate the virtual environment
source venv/bin/activate

# Install requirements from requirements.txt
pip install -r requirements.txt
