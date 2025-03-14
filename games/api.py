from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Game
from .serializer import GoGameSerializer

class GameViewSet(viewsets.ViewSet):
    """
    ViewSet для работы с партиями в Го.
    Поддерживает GET, POST, PUT, PATCH и DELETE.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        """
        Возвращает сериализатор для текущего действия.
        """
        return GoGameSerializer

    def list(self, request):
        """
        GET /api/games/ - Получить список всех партий.
        """
        queryset = Game.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        POST /api/games/ - Создать новую партию.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Остальные методы (retrieve, update, partial_update, destroy) остаются без изменений