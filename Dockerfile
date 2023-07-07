# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN apt update
RUN apt install python3-mysqldb -y
RUN apt install default-mysql-client -y
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/