# Use an official Python runtime as a base image
FROM python:3.10

# Set the working directory in Docker
WORKDIR /app

# Install Python dependencies
COPY backend/Django/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django application folder contents into the container at /app
COPY backend/Django .

# Set environment variable for Django settings module dynamically
ENV DJANGO_SETTINGS_MODULE=backend.Django.settings.production_settings

# Command to run the application using Gunicorn
CMD ["gunicorn", "backend.Django.wsgi:application", "--bind", "0.0.0.0:8000"]