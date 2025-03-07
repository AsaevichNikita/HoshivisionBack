from django.db import models
from games.models import Game

class Analyze(models.Model):
    game = models.OneToOneField(Game, on_delete=models.SET_NULL, null=True, blank=True, related_name='analysis')
    sgf_content = models.TextField()
    last_analyzed_at = models.DateTimeField(auto_now=True)  # Добавлено поле времени последнего анализа

    def __str__(self):
        return f"Analysis for Game {self.game.id}" if self.game else "Unanalyzed Game"

