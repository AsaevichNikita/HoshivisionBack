from rest_framework import serializers
from .models import Game

class GoGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'