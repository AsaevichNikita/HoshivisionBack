
from .views import GoGameViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include  # Добавьте include

# Создаем роутер и регистрируем ViewSet
router = DefaultRouter()
router.register(r'gogames', GoGameViewSet, basename='gogame')

urlpatterns = [
    path('', include(router.urls)),  # Подключаем маршруты роутера
]