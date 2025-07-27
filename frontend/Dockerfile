
FROM node:18-alpine as build

WORKDIR /app

# Установка дополнительных зависимостей для Alpine
RUN apk add --no-cache python3 make g++

# Копирование package.json
COPY package.json ./

# Очистка npm кеша и установка зависимостей
RUN npm cache clean --force
RUN npm install --legacy-peer-deps

# Копирование исходного кода и сборка
COPY . .
RUN npm run build

# Production stage с nginx
FROM nginx:alpine

# Копирование собранного приложения
COPY --from=build /app/build /usr/share/nginx/html

# Копирование конфигурации nginx
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]
