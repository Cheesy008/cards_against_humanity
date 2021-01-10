from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from game.models import Game
from game.serializers import (
    GameListSerializer,
    GameSerializer,
    GameCreateUpdateSerializer,
)
from utils.viewsets import ViewSetBase

User = get_user_model()


class GameViewSet(ViewSetBase):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    serializer_action_classes = {
        'list': GameListSerializer,
        'create': GameCreateUpdateSerializer,
        'update': GameCreateUpdateSerializer,
    }

    def perform_create(self, serializer):
        serializer.validated_data['creator'] = self.request.user
        serializer.save()

