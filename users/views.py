from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request, 'users/login.html')


def register(request):
    return HttpResponse('<h1>Register</h1>')

