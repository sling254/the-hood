from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def IndexView(request):
    return HttpResponse("Hello, world. You're at the hood index.")