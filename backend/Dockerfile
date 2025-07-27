FROM python:3.11-slim

WORKDIR /app

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Обновление pip
RUN pip install --upgrade pip

# Копирование requirements
COPY requirements.txt .

# Установка зависимостей без сборки из исходников
RUN pip install --no-cache-dir --only-binary=all -r requirements.txt || \
    pip install --no-cache-dir -r requirements.txt

# Копирование кода
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]