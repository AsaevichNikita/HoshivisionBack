from rest_framework.generics import ListAPIView
from . import serializer
from django.contrib.auth.models import User


class UserListAPIView(ListAPIView):
    serializer_class = serializer.UserListSerializer

    def get_queryset(self):
        return User.objects.all()