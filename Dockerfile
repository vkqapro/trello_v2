# Start from a Python 3 Debian-based image
FROM python:3.12.0-slim-buster

RUN mkdir "/automation"

# Set working directory
WORKDIR /automation

# Install Python dependencies
COPY ./ /automation
RUN pip install --upgrade pip
RUN pip install playwright pytest-playwright==0.5.2

# Run playwright install to auto-install the browser binaries.
RUN playwright install

RUN python3 -m pip install .