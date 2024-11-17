
FROM python:3.12-slim-buster

RUN mkdir "/automation"
# Set work directory
WORKDIR /automation

# Install Python dependencies
COPY ./ /automation
RUN python3 -m pip install .
