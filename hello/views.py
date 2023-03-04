from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def fernando(request):
    return HttpResponse("Hola Fernando")

def david(request):
    return HttpResponse("Hola David")

def saludo(request, name):
    return render(request, "hello/saludo.html",{
        "name": name.capitalize()
    })