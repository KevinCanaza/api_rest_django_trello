from rest_framework import serializers

from apps.boards.models import Task
from apps.boards.api.serializers.general_serializer import BoardSerializer

class TaskSerializer(serializers.ModelSerializer):

    # Primer metodo

    # board_id = BoardSerializer()
    # Segundo metodo
    # board_id = serializers.RelatedField()
    # Tercer metodo

    class Meta:
        model = Task
        exclude = ('state','create_at','update_at','deleted_at')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'title': instance.title,
            'description': instance.description,
            'assigne': instance.assigne,
            'task_list_id': instance.task_list_id.title if instance.task_list_id is not None  else ''
        }
