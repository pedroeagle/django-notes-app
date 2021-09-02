from django.urls import path
from . import views

urlpatterns = [
    path('', views.NoteView.as_view()),
    path('<int:note>', views.NoteView().as_view())
]