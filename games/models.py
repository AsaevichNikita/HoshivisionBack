from django.db import models
from django.contrib.auth.models import User

from sgfmill import sgf, sgf_moves
import re
from django.core.exceptions import ValidationError

def validate_sgf(value):
    """
    Валидатор для проверки SGF-формата.
    Использует регулярное выражение для базовой проверки и sgfmill для детальной валидации.
    """
    # Базовая проверка регулярным выражением
    if not re.match(r'^\(;.*\)$', value, re.DOTALL):
        raise ValidationError('Invalid SGF format. SGF must start with "(;" and end with ")".')

    # Детальная проверка с использованием sgfmill
    try:
        # Преобразуем строку в байты
        sgf_bytes = value.encode('utf-8')
        sgf_game = sgf.Sgf_game.from_string(sgf_bytes)
        # Проверка на наличие хотя бы одного хода
        if not list(sgf_moves.extract_main_sequence(sgf_game)):
            raise ValidationError('SGF must contain at least one move.')
    except Exception as e:
        raise ValidationError(f'Invalid SGF format: {str(e)}')

class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    sgf_content = models.TextField(validators=[validate_sgf])  # Добавляем валидатор

    def __str__(self):
        return f"Game {self.id} by {self.user.username} at {self.uploaded_at}"

    def clean(self):
        """
        Дополнительная валидация при сохранении модели.
        """
        super().clean()
        validate_sgf(self.sgf_content)