# Start from a Python 3 Debian-based image
FROM python:3.9.10-slim-buster

RUN mkdir "/automation"

# Set working directory
WORKDIR /automation

# Install Python dependencies
COPY ./ /automation

RUN apt-get update \
    && apt-get install -y wget gnupg ca-certificates \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install playwright pytest-playwright==0.5.2

# Run playwright install to auto-install the browser binaries.
RUN playwright install

RUN python3 -m pip install .