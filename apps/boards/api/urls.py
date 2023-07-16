from django.urls import path
from apps.boards.api.views.general_views import (
    BoardListAPIView,
    TaskListListAPIView,
    TaskListAPIView,
)

urlpatterns = [
    path("board/", BoardListAPIView.as_view(), name="board"),
    path("task_list/", TaskListListAPIView.as_view(), name="task_list"),
    path("task/", TaskListAPIView.as_view(), name="task"),
]
