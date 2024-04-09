# Use Python 3.11 slim image from Debian Buster as the base image
FROM python:3.11-slim-buster

# Update package lists and install ImageMagick
RUN apt-get update && apt-get install -y imagemagick

# Modify ImageMagick's policy file to allow read/write for paths with "@" 
# and ensure PDF processing capabilities are enabled
RUN sed -i 's|<policy domain="path" rights="none" pattern="@\*"/>|<!-- <policy domain="path" rights="none" pattern="@\*"/> -->|' /etc/ImageMagick-6/policy.xml

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# # Expect .env file
# ENV ENV_FILE=.env

# ENV GOOGLE_APPLICATION_CREDENTIALS_JSON=${GOOGLE_APPLICATION_CREDENTIALS_JSON}
# ENV IG_PASSWORD=${IG_PASSWORD}
# ENV IG_USERNAME=${IG_USERNAME}

# Run your application when the container launches
CMD ["python", "main.py"]
