from django.urls import path
from .views import GameListCreateView, GameRetrieveUpdateDestroyView

urlpatterns = [
    # GET /games/ - Получить список всех партий.
    # POST /games/ - Создать новую партию.
    path('', GameListCreateView.as_view(), name='game-list-create'),

    # GET /games/{id}/ - Получить детали партии по ID.
    # PUT /games/{id}/ - Полное обновление партии по ID.
    # PATCH /games/{id}/ - Частичное обновление партии по ID.
    # DELETE /games/{id}/ - Удалить партию по ID.
    path('<int:pk>', GameRetrieveUpdateDestroyView.as_view(), name='game-retrieve-update-destroy'),
]