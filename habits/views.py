# habits/views.py
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from .models import Habit
from .serializers import HabitSerializer


# ВРЕМЕННО отключаем аутентификацию для тестирования
class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer

    def get_queryset(self):
        return Habit.objects.all()


class PublicHabitListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)