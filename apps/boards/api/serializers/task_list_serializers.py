from rest_framework import serializers

from apps.boards.models import TaskList
from apps.boards.api.serializers.general_serializer import BoardSerializer

class TaskListSerializer(serializers.ModelSerializer):

    # Primer metodo

    # board_id = BoardSerializer()
    # Segundo metodo
    # board_id = serializers.RelatedField()
    # Tercer metodo

    class Meta:
        model = TaskList
        exclude = ('state','create_at','update_at','deleted_at')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'title': instance.title,
            'board_id': instance.board_id.name if instance.board_id is not None  else ''
        }



