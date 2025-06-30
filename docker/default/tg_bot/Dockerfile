# 1. Базовый образ Python
FROM python:3.12.9-slim

# 2. Установка curl (например, для healthcheck) и удаление кэша apt
RUN apt-get update && apt-get install --no-install-recommends -y curl \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

# 3. Установка рабочей директории
WORKDIR /app

# 4. Копирование проекта
COPY ./tg_bot /app

# 5. Установка зависимостей через pip
# Убедись, что requirements.txt лежит в ./assistant_bot/
COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip setuptools wheel \
  && pip install -r requirements.txt
