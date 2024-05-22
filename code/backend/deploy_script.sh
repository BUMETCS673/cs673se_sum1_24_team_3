#!/bin/bash
# deploy_script.sh

# Navigate to your project directory
# shellcheck disable=SC2164
cd code/backend/Django

# Activate the virtual environment
source venv/bin/activate

# Update the source code
git pull origin main

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Restart Gunicorn service
sudo systemctl restart gunicorn

# Optionally restart Nginx if it's used as a reverse proxy
sudo systemctl restart nginx

# Deactivate the virtual environment
deactivate

echo "Deployment complete."