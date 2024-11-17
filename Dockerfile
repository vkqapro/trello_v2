
FROM python:3.12.0-alpine3.18

RUN mkdir "/automation"
# Set work directory
WORKDIR /automation

# Install Python dependencies
COPY ./ /automation
RUN pip install --upgrade pip
RUN pip install playwright pytest-playwright==0.5.2
RUN python3 -m pip install .

