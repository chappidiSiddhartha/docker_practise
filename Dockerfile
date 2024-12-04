# Use an official Python 3.9.17 runtime as a parent image
FROM python:3.9.17-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Streamlit and Pillow (image processing library)
RUN pip install streamlit pillow

# Expose port 8080 to the world outside the container
EXPOSE 8080

# Define environment variable to prevent buffering of stdout
ENV PYTHONUNBUFFERED 1

# Run Streamlit when the container starts
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
