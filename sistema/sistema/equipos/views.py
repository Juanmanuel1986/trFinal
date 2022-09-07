from django.shortcuts import render
from django.http import HttpResponse
from .models import Equipo
# Create your views here.

def inicio(request): #es la solicitud que se le va a hacer a la aplicacion
    return render(request,'paginas/inicio.html') 

def nosotros(request): #es la solicitud que se le va a hacer a la aplicacion
    return render(request,'paginas/nosotros.html') #busca archivo nosotros.html y lo renderiza, lo busca en paginas/nosotros. dentro de templates.    


def abmequipos(request): #accedo al index para ver los equipos.
    abmequipos = Equipo.objects.all()
    #print(abmequipos) 
    return render(request,'abmequipos/index.html', {'abmequipos': abmequipos})

def niveles(request): 
    return render(request,'paginas/niveles.html')    


def crear(request): #vista para la creacion de los equipos
    return render(request,'abmequipos/crear.html')    


def editar(request): #vista para la creacion de los equipos
    return render(request,'abmequipos/editar.html')    

