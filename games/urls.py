
from .views import GameViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include  # Добавьте include

# Создаем роутер и регистрируем ViewSet
router = DefaultRouter()
router.register(r'gogames', GameViewSet, basename='gogame')

urlpatterns = [
    path('', include(router.urls)),  # Подключаем маршруты роутера
]