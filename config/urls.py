# config/urls.py
from django.contrib import admin
from django.urls import path, include, re_path
from django.http import HttpResponse
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# Простое приветствие для корневого URL
def home_view(request):
    return HttpResponse("""
    <html>
    <head>
        <title>Atomic Habits Tracker API</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            h1 { color: #333; }
            a { color: #0066cc; text-decoration: none; }
            a:hover { text-decoration: underline; }
            .container { max-width: 800px; margin: 0 auto; }
            .link-list { list-style: none; padding: 0; }
            .link-list li { margin: 10px 0; padding: 10px; background: #f5f5f5; border-radius: 5px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🏆 Atomic Habits Tracker API</h1>
            <p>Добро пожаловать в API трекера атомных привычек!</p>

            <h2>🔗 Полезные ссылки:</h2>
            <ul class="link-list">
                <li><a href="/admin/">📊 Админка Django</a></li>
                <li><a href="/api/habits/">📋 API привычек</a></li>
                <li><a href="/swagger/">📖 Документация Swagger</a></li>
                <li><a href="/api/users/register/">👤 Регистрация пользователя</a></li>
                <li><a href="/api/token/">🔐 Получение токена</a></li>
            </ul>

            <h2>📞 Эндпоинты API:</h2>
            <ul>
                <li><strong>GET /api/habits/</strong> - Список привычек текущего пользователя</li>
                <li><strong>POST /api/habits/</strong> - Создание новой привычки</li>
                <li><strong>GET /api/habits/public/</strong> - Список публичных привычек</li>
                <li><strong>POST /api/users/register/</strong> - Регистрация нового пользователя</li>
                <li><strong>POST /api/token/</strong> - Получение JWT токена</li>
            </ul>
        </div>
    </body>
    </html>
    """)


# Настройки для Swagger документации
schema_view = get_schema_view(
    openapi.Info(
        title="Atomic Habits API",
        default_version='v1',
        description="API для трекера полезных привычек",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@habits.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Домашняя страница
    path('', home_view, name='home'),

    # Админка
    path('admin/', admin.site.urls),

    # Аутентификация JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API привычек
    path('api/', include('habits.urls')),

    # API пользователей
    path('api/users/', include('users.urls')),

    # Документация Swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
