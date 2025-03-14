from rest_framework import serializers
from .models import Game

class GoGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'user', 'sgf_content', 'uploaded_at']
        read_only_fields = ['user', 'uploaded_at']  # Эти поля заполняются автоматически

    def create(self, validated_data):
        """
        Переопределяем метод create, чтобы автоматически сохранить пользователя.
        """
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)