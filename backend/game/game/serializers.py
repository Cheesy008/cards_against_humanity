from django.contrib.auth import get_user_model
from rest_framework import serializers, exceptions

from game.models import Game
from users.serializers import UserSerializer

User = get_user_model()


class GameCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'is_active',)


class GameSerializer(serializers.ModelSerializer):
    creator = UserSerializer()
    players = UserSerializer(many=True)

    class Meta:
        model = Game
        fields = ('id', 'name', 'is_active', 'creator', 'players')


class GameListSerializer(serializers.ModelSerializer):
    creator_name = serializers.CharField(source='creator')

    class Meta:
        model = Game
        fields = ('id', 'name', 'is_active', 'creator_name')
        read_only_fields = ('__all__',)

