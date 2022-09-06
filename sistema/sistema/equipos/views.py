from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request): #es la solicitud que se le va a hacer a la aplicacion
    return HttpResponse("<h1>Bienvenido</h1>")


def nosotros(request): #es la solicitud que se le va a hacer a la aplicacion
    return render(request,'paginas/nosotros.html') #busca archivo nosotros.html y lo renderiza, lo busca en paginas/nosotros. dentro de templates.    


def abmequipos(request): #accedo al index para ver los equipos.
    return render(request,'abmequipos/index.html')
