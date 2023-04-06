ARG BASE_IMAGE=python:3.10-slim-bullseye
FROM ${BASE_IMAGE}
RUN apt-get update \
	&& apt-get install build-essential git gcc -y \
	&& apt-get clean

RUN mkdir /data
RUN mkdir /data/src
COPY ./ /data
WORKDIR /data/src

RUN pip3 install -r /data/requirements.txt
RUN pip3 install -r /data/requirements.dev.txt

EXPOSE 8000