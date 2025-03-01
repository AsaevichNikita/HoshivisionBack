from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class GoGame(models.Model):
    # Игроки (можно извлечь из SGF)
    black_player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='black_player_games')
    white_player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='white_player_games')

    # SGF-файл (хранится как текст)
    sgf_content = models.TextField()

    # Дата создания записи
    created_at = models.DateTimeField(auto_now_add=True)

    # Флаг завершенности партии
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return f"Game {self.id}: {self.black_player} (Black) vs {self.white_player} (White)"

    def get_board_size(self):
        """
        Извлекает размер доски из SGF-файла.
        """
        import re
        match = re.search(r'SZ\[(\d+)\]', self.sgf_content)
        if match:
            return int(match.group(1))
        return 19  # По умолчанию 19x19

    def get_result(self):
        """
        Извлекает результат партии из SGF-файла.
        """
        import re
        match = re.search(r'RE\[([BWR]\+[\d.]+|Draw)\]', self.sgf_content)
        if match:
            return match.group(1)
        return None

    def get_players(self):
        """
        Извлекает имена игроков из SGF-файла.
        """
        import re
        black_player_name = re.search(r'PB\[([^\]]+)\]', self.sgf_content)
        white_player_name = re.search(r'PW\[([^\]]+)\]', self.sgf_content)
        return {
            'black': black_player_name.group(1) if black_player_name else None,
            'white': white_player_name.group(1) if white_player_name else None,
        }

    class Meta:
        verbose_name = "Go Game"
        verbose_name_plural = "Go Games"