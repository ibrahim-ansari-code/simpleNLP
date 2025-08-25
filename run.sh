#!/bin/bash

# Simple script to run the NLP system
echo "Starting NLP Question-Answer System..."
echo "======================================"

# Change to the script's directory
cd "$(dirname "$0")"

# Run the Python script using the virtual environment
./venv/bin/python run.py
