# Simple Fullstack App

Простое fullstack приложение с PostgreSQL, FastAPI и React.

## 🚀 Быстрый старт

### Запуск с Docker Compose
```bash
docker-compose up --build
```

### Доступ к приложению
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **PostgreSQL**: localhost:5432

## 🛠️ Технологии

- **Backend**: Python FastAPI + SQLAlchemy + PostgreSQL
- **Frontend**: React + современный CSS
- **Database**: PostgreSQL 15
- **Containerization**: Docker + Docker Compose

## 📊 API Endpoints

- `GET /api/items` - Получить все записи
- `POST /api/items` - Создать новую запись
- `DELETE /api/items/{id}` - Удалить запись
- `GET /api/items/{id}` - Получить запись по ID

## 🔧 Разработка

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm start
```

## 📝 Структура БД

Таблица `items`:
- `id` (SERIAL PRIMARY KEY)
- `caption` (VARCHAR(255) NOT NULL)

## 🐳 Docker команды

```bash
# Запуск всех сервисов
docker-compose up --build

# Запуск в фоновом режиме
docker-compose up -d

# Остановка сервисов
docker-compose down

# Просмотр логов
docker-compose logs

# Пересборка конкретного сервиса
docker-compose build backend
docker-compose build frontend
```

## 🔍 Troubleshooting

### Если порты заняты:
```bash
# Измените порты в docker-compose.yml
ports:
  - "3001:80"    # frontend
  - "8001:8000"  # backend
  - "5433:5432"  # postgres
```

### Если контейнеры не запускаются:
```bash
# Очистите Docker
docker system prune -a
docker-compose down -v
docker-compose up --build
```
