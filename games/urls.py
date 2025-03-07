
from django.urls import path
from . import api

urlpatterns = [
    path('game', api.GameListAPIView.as_view(), name='api_games'),
]