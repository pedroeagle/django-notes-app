from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the users index.")
def login(request):
    return HttpResponse("Login")
def signup(request):
    return HttpResponse("Sign Up")