from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    sgf_content = models.TextField()

    def __str__(self):
        return f"Game {self.id} by {self.user.username} at {self.uploaded_at}"