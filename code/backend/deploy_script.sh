#!/bin/bash

# Assuming the script is for a Django project
echo "Starting deployment process..."

# Activate virtual environment if needed
# source /path/to/venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Deployment completed."