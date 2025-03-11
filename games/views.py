from rest_framework import generics, permissions
from .models import Game
from .serializer import GoGameSerializer

class GameListCreateView(generics.ListCreateAPIView):
    """
    Представление для получения списка партий и создания новой партии.
    """
    queryset = Game.objects.all()
    serializer_class = GoGameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Переопределяем метод для сохранения пользователя, создавшего партию.
        """
        serializer.save(user=self.request.user)

class GameRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Представление для получения, обновления и удаления партии.
    """
    queryset = Game.objects.all()
    serializer_class = GoGameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]