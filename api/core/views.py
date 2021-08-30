from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import RegisterUserSerializer, LoginSerializer, UserSerializer
from .models import User
from rest_framework import generics
from rest_framework import exceptions
from .authentication import JWTAuthentication, generate_access_token
# Create your views here.


class LoggedInUser(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes =[JWTAuthentication]

    def get(self, request, pk=None, format=None):
        serializer =self.get_serializer(request.user)
        response = Response()

        response.data = {
            'message': "User Information retreived successfully",
            'data': serializer.data
        }

        return response

class RegisterUserView(generics.GenericAPIView):
    serializer_class = RegisterUserSerializer

    def post(self, request, format=None):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.data

        password = validated_data.pop('password', None)
        confirm_password = validated_data.pop('confirm_password', None)

        if password != confirm_password:
            raise exceptions.APIException('Passwords do not match')

        instance = User(**validated_data)
        instance.set_password(password)

        instance.save()

        response = Response()

        response.data = {
            'message': 'User created successfully',
        }

        return response


        

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        data = request.data

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(email=serializer.data.get('email'))
        if not user:
            raise exceptions.APIException('User with email address does not exist')

        if not user.check_password(serializer.data.get('password')):
            raise exceptions.APIException('Incorrect Password')

        response = Response()

        response.data = {
            'message': 'Login Successful',
            'token': generate_access_token(user=user)
        }

        return response


