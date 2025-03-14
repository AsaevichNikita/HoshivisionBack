from django.urls import path
from .views import GameListCreateView, GameRetrieveDestroyView

urlpatterns = [
    # GET /games/ - Получить список всех партий.
    # POST /games/ - Создать новую партию.
    path('', GameListCreateView.as_view(), name='game-list-create'),

    # GET /games/{id}/ - Получить детали партии по ID.
    # DELETE /games/{id}/ - Удалить партию по ID.
    path('<int:pk>', GameRetrieveDestroyView.as_view(), name='game-retrieve-destroy'),
]