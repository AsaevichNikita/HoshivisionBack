from rest_framework.generics import ListAPIView
from . import serializer
from . import models


class GameListAPIView(ListAPIView):
    serializer_class = serializer.GoGameSerializer

    def get_queryset(self):
        return models.Game.objects.all()
    