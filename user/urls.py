from django.urls import path
from .views import LogoutView, RegisterView, LoginView, UserView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('', UserView.as_view())
]