# habits/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from .models import Habit
from .serializers import HabitSerializer

class HabitViewSet(viewsets.ModelViewSet):
    """ViewSet для CRUD операций с привычками"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Пользователь видит только свои привычки
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # При создании привычки автоматически назначаем текущего пользователя
        serializer.save(user=self.request.user)

class PublicHabitListAPIView(ListAPIView):
    """Эндпоинт для списка публичных привычек"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    queryset = Habit.objects.filter(is_public=True)
