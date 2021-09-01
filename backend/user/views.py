from django import http
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
from dotenv import load_dotenv
import os
import jwt, datetime

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User or password is incorrect.')
        if not user.check_password(password):
            raise AuthenticationFailed('User or password is incorrect.')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        load_dotenv()
        token = jwt.encode(payload, os.getenv('JWT_SECRET'), algorithm='HS256').decode('utf-8')
        response = Response()
        response.data = {
            'jwt': token
        }
        response.set_cookie(key='jwt', value=token, httponly=True)
        return response