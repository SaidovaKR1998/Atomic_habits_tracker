#!/bin/bash
set -e

echo "🚀 Starting deployment..."

cd ~/apps/atomic-habits

# Останавливаем старые контейнеры
docker-compose -f docker-compose.prod.yaml down || true

# Собираем и запускаем новые
docker-compose -f docker-compose.prod.yaml up -d --build

# Ждём запуска контейнеров
sleep 10

# Выполняем миграции
docker-compose -f docker-compose.prod.yaml exec -T backend python manage.py migrate --noinput

# Собираем статику
docker-compose -f docker-compose.prod.yaml exec -T backend python manage.py collectstatic --noinput

echo "✅ Deployment completed!"
echo "🌐 Application is running at: http://$(curl -s ifconfig.me):8000"
