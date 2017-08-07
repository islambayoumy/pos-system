FROM python:3.6
ENV PYTHONUNBUFFERED 1

ADD . /pos_system
WORKDIR /pos_system

RUN pip install -r requirements.txt