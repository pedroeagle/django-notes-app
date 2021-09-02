from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView 
from .serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
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
            raise NotFound(f'Note {note} doesn\'t exist')
        serializer = NoteSerializer(data=notes, many=True)
        serializer.is_valid()
        notes.delete()
        return Response({'message': f'The note {note} was successfully deleted.'})
    def patch(self, request, note):
        user = User().get_user(request)
        found_note = Note.objects.filter(user_id=user.id, id=note)
        if not found_note:
            raise NotFound(f'Note {note} doesn\'t exist')
        data = dict(request.data.dict())
        data.update({'user': user.id})
        serializer = NoteSerializer(data = data)
        serializer.is_valid(raise_exception=True)
        found_note.update(title = data['title'], content = data['content'])
        return Response(serializer.data)