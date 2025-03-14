from django.test import TestCase
from django.contrib.auth.models import User
from .models import Game
from django.core.exceptions import ValidationError

class GameModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_valid_sgf(self):
        """
        Проверка валидного SGF.
        """
        game = Game(user=self.user, sgf_content='(;GM[1]FF[4]SZ[19];B[aa];W[bb])')  # Валидный SGF с ходами
        try:
            game.full_clean()  # Вызовет валидацию
        except ValidationError:
            self.fail("Valid SGF raised ValidationError unexpectedly.")

    def test_invalid_sgf(self):
        """
        Проверка невалидного SGF (без ходов).
        """
        game = Game(user=self.user, sgf_content='(;GM[1]FF[4]SZ[19])')  # Нет ходов
        with self.assertRaises(ValidationError) as context:
            game.full_clean()  # Вызовет валидацию
        self.assertIn('SGF must contain at least one move', str(context.exception))

    def test_invalid_sgf_format(self):
        """
        Проверка некорректного формата SGF.
        """
        game = Game(user=self.user, sgf_content='invalid sgf')  # Некорректный SGF
        with self.assertRaises(ValidationError) as context:
            game.full_clean()  # Вызовет валидацию
        self.assertIn('Invalid SGF format', str(context.exception))
