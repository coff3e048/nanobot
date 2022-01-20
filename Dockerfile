FROM python:3.10-slim-bullseye


RUN apt update && apt upgrade -y \
	&& apt install -y curl git \
	gcc g++ \
	ffmpeg


#RUN useradd -ms /bin/bash nanobot

RUN mkdir /nanobot
WORKDIR /nanobot

COPY ./requirements.txt requirements.txt

WORKDIR /nanobot
RUN pip install -r \
	requirements.txt

#USER nanobot
ENTRYPOINT ["python", "bot/ignition.py"]