from rest_framework import generics

from apps.setup_initial.api import GeneralListApiWiev
from apps.boards.api.serializers.general_serializer import (
    BoardSerializer,
    TaskListSerializer,
    TaskSerializer,
)


class BoardListAPIView(GeneralListApiWiev):
    serializer_class = BoardSerializer


class TaskListListAPIView(GeneralListApiWiev):
    serializer_class = TaskListSerializer

    
class TaskListAPIView(GeneralListApiWiev):
    serializer_class = TaskSerializer
