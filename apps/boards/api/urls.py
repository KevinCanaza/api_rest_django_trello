from django.urls import path

from apps.boards.api.views.general_views import (
    BoardListAPIView,
)
from apps.boards.api.views.board_views import (
    BoardListCreateAPIView,
    BoardRetrieveUpdateDestroyAPIView,
)

from apps.boards.api.views.task_list_views import (
    TaskListListCreateAPIView,
    TaskListRetrieveUpdateDestroyAPIView,
)

from apps.boards.api.views.task_views import (
    TaskListCreateAPIView,
    TaskRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path("board/", BoardListCreateAPIView.as_view(), name="board_create"),
    path(
        "board/retrieve-update-destroy/<int:pk>/",
        BoardRetrieveUpdateDestroyAPIView.as_view(),
        name="board_retrieve_update_destroy",
    ),
    path("task_list/", TaskListListCreateAPIView.as_view(), name="task_list_list_create"),
    path(
        "task_list/retrieve-update-destroy/<int:pk>/",
        TaskListRetrieveUpdateDestroyAPIView.as_view(),
        name="task_list_retrieve_update_destroy",
    ),
]
