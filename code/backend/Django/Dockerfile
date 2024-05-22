# Use an official Python runtime as a base image
FROM python:3.8

# Set the working directory in Docker
WORKDIR /app

# Install Python dependencies
COPY ./backend/Django/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django application folder contents into the container at /app
COPY ./backend/Django /app/

# Set environment variable for Django settings module to use production settings
ENV DJANGO_SETTINGS_MODULE=code.backend.Django.production_settings

# Command to run the application using Gunicorn, adjust the application path as necessary
CMD ["gunicorn", "survey_form_backend.wsgi:application", "--bind", "0.0.0.0:8000"]