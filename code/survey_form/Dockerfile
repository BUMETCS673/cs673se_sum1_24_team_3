# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Setting environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Setting working directory
WORKDIR /code

# Installing dependenceies
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the current directory into container at /code
COPY . /code/
