from django.contrib import admin

from django.contrib import admin
from .models import Game

class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'uploaded_at')  # Отображаем ID игры, пользователя и время загрузки
    search_fields = ('user__username',)  # Поиск по имени пользователя
    list_filter = ('uploaded_at',)  # Фильтрация по времени загрузки

admin.site.register(Game, GameAdmin)
