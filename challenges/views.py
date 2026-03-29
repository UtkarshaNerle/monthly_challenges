from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def january(request):
    return HttpResponse("heyy")

def february(request):
    return HttpResponse("im okay")

def march(request):
    return HttpResponse("im gonna play the game")