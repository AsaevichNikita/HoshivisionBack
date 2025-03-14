from django.contrib import admin

from django.contrib import admin
from .models import Analyze

class AnalyzeAdmin(admin.ModelAdmin):
    list_display = ('game', 'last_analyzed_at')  # Отображаем игру и время последнего анализа
    search_fields = ('game__id',)  # Добавляем поиск по id игры
    list_filter = ('last_analyzed_at',)  # Фильтры по времени последнего анализа

admin.site.register(Analyze, AnalyzeAdmin)
