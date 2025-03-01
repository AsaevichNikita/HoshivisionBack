from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import GoGame
from .serializer import GoGameSerializer

class GoGameViewSet(viewsets.ViewSet):
    """
    ViewSet для работы с партиями в Го.
    Поддерживает GET, POST и DELETE.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request):
        """
        GET /api/gogames/ - Получить список всех партий.
        """
        queryset = GoGame.objects.all()
        serializer = GoGameSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        POST /api/gogames/ - Создать новую партию.
        """
        serializer = GoGameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        DELETE /api/gogames/{id}/ - Удалить партию по ID.
        """
        try:
            game = GoGame.objects.get(pk=pk)
            game.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except GoGame.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)