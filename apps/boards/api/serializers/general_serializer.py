from apps.boards.models import Board,TaskList,Task

from  rest_framework import serializers

class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        exclude = ('state','create_at','update_at','deleted_at')

class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskList
        exclude = ('state','create_at','update_at','deleted_at')


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        exclude = ('state','create_at','update_at','deleted_at')