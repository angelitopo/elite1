#!/bin/bash

# Update package list and install Python and pip if not installed
echo "Setting up the environment..."
sudo apt-get update && sudo apt-get install -y python3 python3-pip

# Install virtual environment
pip3 install virtualenv

# Create and activate virtual environment
virtualenv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
echo "Starting the Streamlit app..."
streamlit run app.py
