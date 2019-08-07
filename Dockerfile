FROM python:3.7-alpine
MAINTAINER Lucas Morais lucasmorais.dev@gmail.com
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code/pontos_turisticos
COPY ./code /code

COPY ./requeriments.txt /requeriments.txt
RUN pip install -r /requeriments.txt

RUN adduser -D webuser
USER webuser