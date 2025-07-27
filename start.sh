#!/bin/bash

echo "🚀 Запуск Simple Fullstack App"
echo "==============================="

# Проверяем Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker не найден"
    exit 1
fi

# Определяем команду docker-compose
if command -v docker-compose &> /dev/null; then
    DOCKER_COMPOSE_CMD="docker-compose"
else
    DOCKER_COMPOSE_CMD="docker compose"
fi

echo "🐳 Запуск контейнеров..."
$DOCKER_COMPOSE_CMD up --build

echo "✅ Приложение запущено!"
echo "🌐 Frontend: http://localhost:3000"
echo "🔗 Backend API: http://localhost:8000"
echo "📚 API Docs: http://localhost:8000/docs"
