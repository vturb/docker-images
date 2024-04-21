# Use a official Python runtime as a parent image
FROM python:alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Install any needed packages specified in requirements.txt
# Assuming you have a requirements.txt file with 'kestra' listed
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY main.py .

# Make port 80 available to the world outside this container
EXPOSE 80
