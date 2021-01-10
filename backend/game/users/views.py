from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from users.serializers import LoginSerializer, UserSerializer

User = get_user_model()


class PlayerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user: User = serializer.validated_data.get('user')
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'user': UserSerializer(user).data,
            'token': token.key
        }, status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], url_path='logout')
    def logout(self, request, *args, **kwargs):
        request.auth.delete()
        return Response({'detail': 'User successfully logged out!'}, status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'], permission_classes=(permissions.IsAuthenticated,), url_path='user')
    def get_user(self, request, *args, **kwargs):
        return Response({
            'user': UserSerializer(request.user, context=self.get_serializer_context()).data
        }, status.HTTP_200_OK)






