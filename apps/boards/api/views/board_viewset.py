from rest_framework import generics
from rest_framework import status

#
from rest_framework import viewsets

#
from rest_framework.response import Response

from apps.setup_initial.api import GeneralListApiWiev
from apps.boards.api.serializers.board_serializers import BoardSerializer


class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return (
                self.get_serializer()
                .Meta.model.objects.filter(id=pk, state=True)
                .first()
            )

    def list(self, request):
        board_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(board_serializer.data, status=status.HTTP_200_OK)

    def create(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Tablero creado correctamente!"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            board_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data
            )
        if board_serializer.is_valid():
            board_serializer.save()
            return Response(board_serializer.data, status=status.HTTP_200_OK)
        return Response(board_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        board = self.get_queryset().filter(id=pk).first()
        if board:
            board.state = False
            board.save()
            return Response(
                {"message": "Tablero eliminado correctamente!"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"error": "No existe un tablero con estos datos!"},
            status=status.HTTP_400_BAD_REQUEST,
        )
