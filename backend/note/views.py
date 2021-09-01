from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView 
from .serializers import NoteSerializer
from rest_framework.response import Response
from user.models import User
from note.models import Note

class NoteView(APIView):
    def post(self, request):
        user = User().get_user(request)
        data = dict(request.data.dict())
        data.update({'user': user.id})
        serializer = NoteSerializer(data = data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def get(self, request):
        user = User().get_user(request)
        notes = Note.objects.filter(user_id=user.id).all()
        serializer = NoteSerializer(data=notes, many=True)
        serializer.is_valid()
        return Response(serializer.data)