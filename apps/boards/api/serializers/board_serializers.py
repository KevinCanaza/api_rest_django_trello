from rest_framework import serializers
from apps.boards.models import Board

class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        exclude = ('state','create_at','update_at','deleted_at')