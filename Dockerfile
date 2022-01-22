FROM python:3.10.1-slim

RUN apt update && apt install python3-dev default-libmysqlclient-dev build-essential libaio1 -y

WORKDIR /code

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade pip

COPY requirements/ requirements/

RUN pip install -r requirements/dev.txt

COPY . . 
