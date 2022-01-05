FROM python:3.10-slim-bullseye


RUN apt update && apt upgrade -y \
	&& apt install -y curl git \
	gcc g++

RUN useradd -ms /bin/bash nanobot

RUN mkdir /nanobot
WORKDIR /nanobot

COPY ./requirements.txt requirements.txt

USER nanobot
WORKDIR /nanobot
RUN pip install -r \
	requirements.txt

ENTRYPOINT ["python", "/nanobot/bot/ignition.py"]
