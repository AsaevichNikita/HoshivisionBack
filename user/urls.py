from django.urls import path
from . import api

urlpatterns = [
    path('user', api.UserListAPIView.as_view(), name='api_users'),
]
