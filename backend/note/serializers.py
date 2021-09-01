from rest_framework import serializers
from django.db import models
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta():
        model = Note
        fields = ['title', 'content', 'user']
        extra_kwargs = {
            'user': {'write_only': True}
        }