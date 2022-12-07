# syntax=docker/dockerfile:1

# pull official base image
FROM python:3.10.6

# install dependencies
RUN apt-get update && apt-get install -y apt-transport-https && \
    apt-get install -y libssl-dev libffi-dev gcc python3-dev musl-dev build-essential \
    libpq-dev 

# set working directory
WORKDIR /app

# Set environment variables
ENV FLASK_RUN_HOST=0.0.0.0

# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r /usr/src/app/requirements.txt

# add entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

EXPOSE 5000

# add app
COPY . /app
