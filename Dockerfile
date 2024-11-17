
FROM python:3.12.0-alpine3.18

RUN mkdir "/automation"
# Set work directory
WORKDIR /automation

# Install Python dependencies
COPY ./ /automation
RUN pip install --upgrade pip
RUN python3 -m pip install .
