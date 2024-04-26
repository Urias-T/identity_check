FROM python:3.11

LABEL maintainer "Triumph"

COPY ../ /app

WORKDIR /app

RUN apt-get update 

RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install -r requirements.txt

ENV PORT 8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 300 main:app