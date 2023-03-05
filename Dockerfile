FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE=1\
PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt