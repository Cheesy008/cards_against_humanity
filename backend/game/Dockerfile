FROM python:3.7.5-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code
WORKDIR /code

COPY . .

RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt
