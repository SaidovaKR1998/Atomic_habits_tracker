# habits/views.py
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import ListAPIView
from .models import Habit
from .serializers import HabitSerializer
from .pagination import HabitsPagination


class HabitViewSet(viewsets.ModelViewSet):
    """ViewSet для CRUD операций с привычками"""
    serializer_class = HabitSerializer
    permission_classes = [AllowAny]  # Пока оставляем доступ для всех
    pagination_class = HabitsPagination  # Используем нашу пагинацию

    def get_queryset(self):
        return Habit.objects.all().order_by('-id')  # Сортируем по новизне

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            from django.contrib.auth.models import User
            user = User.objects.first()
            serializer.save(user=user)


class PublicHabitListAPIView(ListAPIView):
    """Эндпоинт для списка публичных привычек"""
    serializer_class = HabitSerializer
    permission_classes = [AllowAny]
    pagination_class = HabitsPagination  # Используем нашу пагинацию
    queryset = Habit.objects.filter(is_public=True).order_by('-id')
