from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateNoteView.as_view()),
]