from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    return render(request, 'index/base.html')


def index(request):
    return render(request, 'index/index.html')
