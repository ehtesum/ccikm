from django.shortcuts import render
from django.http import HttpResponse
from . models import Tools

#tools -> index

def index(request):
    tools = Tools.objects.all()
    return render(request, 'index.html', {'tools': tools})

def new(request):
    return HttpResponse('New')


# Create your views here.
