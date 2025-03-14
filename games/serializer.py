from rest_framework import serializers
from .models import Game
from django.core.exceptions import ValidationError
from .models import validate_sgf  # Импортируем валидатор

class GoGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'user', 'sgf_content', 'uploaded_at']
        read_only_fields = ['user', 'uploaded_at']  # Эти поля заполняются автоматически

    def validate_sgf_content(self, value):
        """
        Валидация поля sgf_content.
        """
        validate_sgf(value)  # Используем наш валидатор
        return value

    def create(self, validated_data):
        """
        Переопределяем метод create, чтобы автоматически сохранить пользователя.
        """
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)