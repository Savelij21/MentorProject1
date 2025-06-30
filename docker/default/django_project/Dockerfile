# Используем базовый образ Python
FROM python:3.12.9-slim AS python

# Устанавливаем переменные окружения для Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Обновляем индексы пакетов и устанавливаем системные зависимости
RUN apt-get update && apt-get install --no-install-recommends -y \
  build-essential \
  libpq-dev \
  curl \
  gnupg \
  lsb-release \
  && echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" \
     > /etc/apt/sources.list.d/pgdg.list \
  && curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
  && apt-get update \
  && apt-get install --no-install-recommends -y postgresql-client-17 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY ./django_project /app

# Копируем файл зависимостей
COPY ./requirements.txt /app/requirements.txt

# Установка зависимостей через pip
RUN pip install --upgrade pip setuptools wheel \
  && pip install -r requirements.txt

