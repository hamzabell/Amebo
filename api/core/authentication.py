import jwt
from datetime import datetime, timedelta
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from .models import User

def generate_access_token(user):
    payload = {
        'user_id': user.id,
        'exp': (datetime.now() + timedelta(hours=2)).timestamp(),
        'int': datetime.now().timestamp()
    }

    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf8')

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            raise exceptions.AuthenticationFailed('Please pass Authentication header')
        token  = auth_header.split(' ')[1]

        if not token:
            return None

        try:
            data = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token has expired')

        user = User.objects.get(id=data['user_id'])

        if not user:
            raise exceptions.AuthenticationFailed('User does not exist')

        return (user, None)