#!/bin/bash

echo "🛑 Остановка Simple Fullstack App"
echo "================================="

# Определяем команду docker-compose
if command -v docker-compose &> /dev/null; then
    DOCKER_COMPOSE_CMD="docker-compose"
else
    DOCKER_COMPOSE_CMD="docker compose"
fi

echo "🐳 Остановка контейнеров..."
$DOCKER_COMPOSE_CMD down

echo "✅ Приложение остановлено!"
