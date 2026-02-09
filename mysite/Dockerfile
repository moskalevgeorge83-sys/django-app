FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app

WORKDIR /app

# СИСТЕМНЫЕ БИБЛИОТЕКИ ДЛЯ PILLOW
RUN apt-get update && apt-get install -y \
    libjpeg62-turbo-dev \
    libpng-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Установка Poetry
RUN pip install --no-cache-dir --timeout=600 poetry==1.8.3

# Копирование зависимостей
COPY pyproject.toml poetry.lock ./

# ТОЛЬКО MAIN зависимости (БЕЗ dev/toolbar)
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY . .

ENV DJANGO_DEBUG=1
EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && gunicorn mysite.wsgi:application --bind 0.0.0.0:8000"]


