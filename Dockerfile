FROM python:3.12.0-alpine3.18

# Update apk repositories
RUN apk update

# Install dependencies
RUN apk add --no-cache \
    curl \
    gnupg \
    ca-certificates

RUN mkdir "/automation"

# Install Chrome
RUN apt-get update && apt-get install -y \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg \
  --no-install-recommends \
  && curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update && apt-get install -y \
  google-chrome-stable \
  fontconfig fonts-ipafont-gothic \
  --no-install-recommends \
  && rm -rf /var/lib/apt/lists/*

# Install ChromeDriver
RUN CHROME_VERSION=$(google-chrome-stable --version | awk '{ print $3 }' | awk -F'.' '{ print $1 }') \
  && DRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION") \
  && curl -sSL https://chromedriver.storage.googleapis.com/$DRIVER_VERSION/chromedriver_linux64.zip -o /tmp/driver.zip \
  && mkdir /usr/local/bin/chromedriver \
  && unzip /tmp/driver.zip -d /usr/local/bin/chromedriver \
  && rm /tmp/driver.zip \
  && chmod +x /usr/local/bin/chromedriver \
  && ln -s /usr/local/bin/chromedriver/chromedriver /usr/bin/chromedriver

# Set Paths for Chromedriver and Google Chrome
#ENV PATH "/usr/local/bin/chromedriver:$PATH"
#ENV PATH "/usr/bin/google-chrome:$PATH"




COPY ./ /automation
WORKDIR /automation

RUN python3 setup.py install
RUN python3 -m pip install .

