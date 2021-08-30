from rest_framework import fields, serializers
from rest_framework import exceptions
from .models import User
import re

def email_validator(func):
    def wrapper(self, email):
        email_regex =  r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if not re.fullmatch(email_regex, email):
            raise serializers.ValidationError("Please pass a valid email address")
        
        return email

    return wrapper



class RegisterUserSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    secret_phrase = serializers.CharField(required=True)
    profile_image = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    @email_validator
    def validate_email(self, email):
        return email

    def validate_password(self, password):
        if len(password) < 6:
            raise serializers.ValidationError('Password must be 6 characters long')
        
        return password


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    @email_validator
    def validate_email(self, email):
        return email


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','first_name', 'last_name', 'username', 'profile_image', 'email')