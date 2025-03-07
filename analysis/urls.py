from django.urls import path
from . import api

urlpatterns = [
    path('analysis', api.AnalyzeListAPIView.as_view(), name='api_analyzes'),
]