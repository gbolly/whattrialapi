from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, plain_password: str) -> str:
        validate_password(plain_password)
        return make_password(plain_password)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(label="Email", write_only=True)
    password = serializers.CharField(label="Password", write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)
            if not user:
                raise serializers.ValidationError(
                    'Incorrect email or password.', code='authorization')
        else:
            raise serializers.ValidationError(
                'Both "email" and "password" are required.', code='authorization')

        attrs['user'] = user
        return attrs
