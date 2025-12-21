# Atomic Habits Tracker 🏆

Курсовая работа - бэкенд часть SPA веб-приложения для трекера полезных привычек, вдохновленного книгой Джеймса Клира "Атомные привычки".

## 📋 Функциональность

- ✅ Регистрация и аутентификация пользователей (JWT)
- ✅ CRUD операции для привычек
- ✅ Валидации привычек согласно требованиям книги
- ✅ Пагинация (5 привычек на страницу)
- ✅ Публичные привычки
- ✅ Настройка CORS для фронтенда
- ✅ Интеграция с Telegram для напоминаний
- ✅ Отложенные задачи через Celery
- ✅ Полное покрытие тестами (>80%)
- ✅ Проверка кода Flake8

## 📚 API Документация
После запуска сервера доступна документация:

Swagger UI: http://localhost:8000/swagger/

ReDoc: http://localhost:8000/redoc/

## 📊 Основные эндпоинты
POST /api/users/register/ - Регистрация

POST /api/token/ - Получение JWT токена

GET /api/habits/ - Список привычек пользователя

POST /api/habits/ - Создание привычки

GET /api/habits/public/ - Публичные привычки

# Atomic Habits Tracker

Приложение для отслеживания привычек с напоминаниями и Telegram-ботом.

## 🚀 Быстрый запуск (Docker Compose)

### 1. Клонирование репозитория
git clone https://github.com/SadovaKR1998/Atomic_habits_tracker.git
cd Atomic_habits_tracker

### 2. Создание файла окружения
cp .env.example .env

Отредактируйте .env файл, установите свои значения:
SECRET_KEY=ваш-секретный-ключ
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgresql://habits_user:Said43Said43@db:5432/habits_db
REDIS_URL=redis://redis:6379/0
TELEGRAM_BOT_TOKEN=ваш-telegram-токен

### 3. Запуск проекта
- Для разработки:
docker-compose up --build
- Или в фоновом режиме:
docker-compose up -d --build

### 4. Проверка работоспособности
Откройте в браузере:
- Django приложение: http://localhost:8000
- API документация: http://localhost:8000/api/schema/swagger-ui/
- Admin панель: http://localhost:8000/admin/

## 🐳 Docker Compose Сервисы
После запуска docker-compose up будут запущены следующие контейнеры:

1. web (Django)

- Порт: 8000
- Проверка: curl http://localhost:8000/health/

docker-compose exec web python manage.py check

2. db (PostgreSQL)

- Порт: 5432
- Проверка подключения:

docker-compose exec db pg_isready -U habits_user

3. redis

- Порт: 6379
- Проверка:

docker-compose exec redis redis-cli ping

4. celery_worker (Celery Worker)

- Обработка фоновых задач
- Проверка:

docker-compose logs celery_worker

5. celery_beat (Celery Beat)

- Планировщик периодических задач
- Проверка:

docker-compose logs celery_beat

6. nginx (если настроен)

- Порт: 80
- Проверка: curl http://localhost

## 📊 Статус всех сервисов

- Проверить статус всех контейнеров
docker-compose ps

- Просмотреть логи всех сервисов
docker-compose logs

- Просмотреть логи конкретного сервиса
docker-compose logs web
docker-compose logs celery_worker

## 🔧 Полезные команды
Инициализация базы данных

- Создать миграции
docker-compose exec web python manage.py makemigrations

- Применить миграции
docker-compose exec web python manage.py migrate

- Создать суперпользователя
docker-compose exec web python manage.py createsuperuser

Работа со статикой

- Собрать статические файлы
docker-compose exec web python manage.py collectstatic --noinput

Тестирование

- Запустить тесты
docker-compose exec web python manage.py test

- Запустить тесты с покрытием
docker-compose exec web python manage.py test --coverage

Администрирование

- Открыть shell Django
docker-compose exec web python manage.py shell

# Проверить здоровье приложения
docker-compose exec web python manage.py check --deploy

## 📱 Telegram Бот
Настройка бота
1) Создайте бота через @BotFather в Telegram
2) Получите токен 
3) Добавьте токен в .env файл:

TELEGRAM_BOT_TOKEN=ваш-токен-бота

Проверка работы бота

- Проверить, что бот запущен
docker-compose logs web | grep "bot"

- Или проверить через Django shell
docker-compose exec web python manage.py shell

## 🚀 Production Deploy
Для продакшн-развертывания используйте отдельный конфиг:

docker-compose -f docker-compose.prod.yaml up -d

## 🛠️ Устранение неполадок
Сервис не запускается

- Пересобрать и запустить
docker-compose down
docker-compose up --build

- Проверить логи
docker-compose logs --tail=100

Проблемы с базой данных

- Сбросить базу данных (осторожно!)
docker-compose down -v
docker-compose up -d

- Сделать бекап
docker-compose exec db pg_dump -U habits_user habits_db > backup.sql

Проблемы с Redis

- Очистить кеш Redis
docker-compose exec redis redis-cli FLUSHALL