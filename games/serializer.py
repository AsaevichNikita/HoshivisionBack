from rest_framework import serializers
from .models import GoGame

class GoGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoGame
        fields = '__all__'