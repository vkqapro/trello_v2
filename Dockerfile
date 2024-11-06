FROM python:3.12.0-alpine3.18

#RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
#RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-2.30-r0.apk
#RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-bin-2.30-r0.ap

RUN apk update && apk add openjdk11-jre curl tar && curl -o allure-2.13.8.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz && tar -zxvf allure-2.13.8.tgz -C /opt/ && ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure && rm allure-2.13.8.tgz

RUN mkdir /automation

COPY ./ /automation
WORKDIR /automation

RUN python3 -m pip install .