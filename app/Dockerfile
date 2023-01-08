# Use python base image
FROM python:3.10

# Disable python log buffering
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH "${PYTHONPATH}:/docker-app"

# Update apt-get and install packages
RUN apt-get update && \
    apt-get install -y \
        python3-dev python3-pip \
        postgresql-client \
        vim

# Set working directory
WORKDIR /docker-app

# Copy all files from context
COPY . /docker-app

# Upgrade pip and install packages specified in requirements
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt

CMD streamlit run home_page.py --server.port 80
