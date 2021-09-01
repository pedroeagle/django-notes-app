from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView 
from .serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
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
    def delete(self, request, note):
        user = User().get_user(request)
        notes = Note.objects.filter(user_id=user.id, id=note).all()
        if not notes:
            raise AuthenticationFailed(f'Note {note} doesn\'t exist')
        serializer = NoteSerializer(data=notes, many=True)
        serializer.is_valid()
        notes.delete()
        return Response({'message': f'The note {note} was successfully deleted.'})
