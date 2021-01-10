from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers, exceptions

from .models import Profile

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('avatar',)


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'profile',)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        required=True
    )

    def validate(self, attrs):
        attrs = super(LoginSerializer, self).validate(attrs)
        user: User = authenticate(username=attrs['username'], password=attrs['password'])

        if not user:
            raise exceptions.AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise exceptions.AuthenticationFailed('Account disabled, contact admin')

        attrs['user'] = user

        return attrs


