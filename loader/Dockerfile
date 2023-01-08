# Use python base image
FROM python:3.10

# Disable python log buffering
ENV PYTHONUNBUFFERED=1

# Update apt-get and install packages
RUN apt-get update && \
    apt-get install -y \
        python3-dev python3-pip \
        postgresql-client \
        vim \
        netcat

# Get various csv tools.
RUN pip install csvkit

# Set working directory
WORKDIR /app

# Copy all files from context
COPY . /app

# Upgrade pip and install packages specified in requirements
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt

# Run load.py every time this container is executed
RUN chmod +x /app/entrypoint.sh
# CMD python load.py
