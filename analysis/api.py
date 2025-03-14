from rest_framework.generics import ListAPIView
from . import serializer
from . import models


class AnalyzeListAPIView(ListAPIView):
    serializer_class = serializer.AnalyzeListSerializer

    def get_queryset(self):
        return models.Analyze.objects.all()