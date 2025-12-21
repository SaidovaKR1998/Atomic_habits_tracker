#!/bin/bash
set -e

echo "🚀 Starting deployment..."

cd ~/apps/atomic-habits

# Копируем файлы с GitHub
git pull origin main

# Останавливаем старые контейнеры
docker-compose -f docker-compose.prod.yaml down

# Собираем и запускаем новые
docker-compose -f docker-compose.prod.yaml up -d --build

# Выполняем миграции
docker-compose -f docker-compose.prod.yaml exec -T backend python manage.py migrate --noinput

# Собираем статику
docker-compose -f docker-compose.prod.yaml exec -T backend python manage.py collectstatic --noinput

echo "✅ Deployment completed!"
