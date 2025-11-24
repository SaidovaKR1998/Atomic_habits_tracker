# users/views.py
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserCreateAPIView(generics.CreateAPIView):
    """Регистрация нового пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer