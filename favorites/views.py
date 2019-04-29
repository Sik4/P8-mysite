from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def favorites(request):
    return HttpResponse("Welcome to <strong>Favorites</strong>")