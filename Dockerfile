# Use an official Python runtime as the base image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy  the application's code to the container
COPY . .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Specify the command to run your Flask app within the container
CMD ["python", "app.py"]
