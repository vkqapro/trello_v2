FROM python:3.12.0-alpine3.18

RUN mkdir "/automation"

COPY ./ /automation
WORKDIR /automation

RUN python3 -m pip install .

