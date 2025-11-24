INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Сторонние приложения
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'drf_yasg',
    'django_celery_beat',

    # Ваши приложения
    'users',
    'habits',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Адрес вашего React/Vue фронтенда
    "https://yourfrontend.com",
]

CORS_ALLOW_ALL_ORIGINS = False # Для продакшена лучше False и явно указать адреса выше