from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request): #es la solicitud que se le va a hacer a la aplicacion
    return HttpResponse("<h1>Bienvenido</h1>")
    