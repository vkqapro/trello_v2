# Use python 3.8 buster image
FROM python:3.8-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Update the system and install dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        apt-utils \
        curl \
        unzip \
    && curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb \
    && dpkg -i chrome.deb || apt-get install -yf \
    && rm chrome.deb

# Install chromedriver
RUN CHROME_VERSION=$(google-chrome-stable --version | grep -Eoi '([0-9]{1,3}\.){3}[0-9]{1,3}' | head -1) \
    && DRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION") \
    && curl -sSL "https://chromedriver.storage.googleapis.com/${DRIVER_VERSION}/chromedriver_linux64.zip" -o chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip -d /usr/bin \
    && chmod +x /usr/bin/chromedriver \
    && rm chromedriver_linux64.zip

# Set work directory
WORKDIR /automation

# Install Python dependencies
COPY ./ /automation
RUN python3 -m pip install .

# Copy application
COPY . .