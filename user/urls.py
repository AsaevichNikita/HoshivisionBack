from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),  # Главная страница приложения
    path('profile/', views.profile, name='profile'),  # Пример маршрута для профиля
]
