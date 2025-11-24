from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HabitViewSet, PublicHabitListAPIView

router = DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habits')

urlpatterns = [
    # URL для ViewSet (автоматически создает: habits/, habits/<id>/, etc.)
    path('', include(router.urls)),

    # Отдельный URL для публичных привычек
    path('public/', PublicHabitListAPIView.as_view(), name='public-habits'),
]