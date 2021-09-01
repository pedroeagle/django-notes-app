from django.http import HttpResponse
from rest_framework.views import APIView
from .serializers import NoteSerializer
from rest_framework.response import Response
from user.models import User

class CreateNoteView(APIView):
    def post(self, request):
        user = User().get_user(request)
        print(user.id)
        data = dict(request.data.dict())
        data.update({'user': user.id})
        serializer = NoteSerializer(data = data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
