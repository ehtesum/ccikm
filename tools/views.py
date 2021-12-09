from django.shortcuts import render
from django.http import HttpResponse

#tools -> index

def index(request):
    return HttpResponse("Hello")


def new(request):
    return HttpResponse('New')


# Create your views here.
