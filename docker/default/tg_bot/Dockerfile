FROM python:3.12.9-slim

RUN apt-get update && apt-get install --no-install-recommends -y \
    gcc libc-dev libpq-dev curl \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
COPY ./tg_bot /app

RUN pip install --upgrade pip setuptools wheel \
  && pip install -r requirements.txt
