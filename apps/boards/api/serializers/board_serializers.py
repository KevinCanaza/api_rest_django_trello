from apps.boards.models import Board

from rest_framework import serializers

class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        exlude = ('state',)