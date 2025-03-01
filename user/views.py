from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Добро пожаловать в Hoshivision!")

def profile(request):
    return HttpResponse("Это страница профиля.")
