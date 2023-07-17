from rest_framework.routers import DefaultRouter
from apps.boards.api.views.task_viewset import TaskViewSet
from apps.boards.api.views.task_list_viewset import TaskListViewSet
from apps.boards.api.views.board_viewset import BoardViewSet

router = DefaultRouter()

router.register(r'tasks',TaskViewSet,basename='tasks')
router.register(r'tasks_lists',TaskListViewSet,basename='tasks_lists')
router.register(r'boards',BoardViewSet,basename='boards')

urlpatterns = router.urls