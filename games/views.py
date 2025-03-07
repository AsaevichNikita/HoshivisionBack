from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Game
from .serializer import GoGameSerializer

class GameViewSet(viewsets.ViewSet):
    """
    ViewSet для работы с партиями в Го.
    Поддерживает GET, POST и DELETE.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request):
        """
        GET /api/games/ - Получить список всех партий.
        """
        queryset = Game.objects.all()
        serializer = GoGameSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        POST /api/games/ - Создать новую партию.
        """
        serializer = GoGameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        DELETE /api/games/{id}/ - Удалить партию по ID.
        """
        try:
            game = Game.objects.get(pk=pk)
            game.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Game.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)