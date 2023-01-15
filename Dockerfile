# Use the official Python image as the base image
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .Docker

# Expose the port on which the application will run
EXPOSE 5000

# Run the application
CMD ["python", "main.py"]