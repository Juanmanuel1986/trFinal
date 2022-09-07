from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Equipo
from .forms import EquipoForm
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
    formulario = EquipoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('abmequipos')
    return render(request,'abmequipos/crear.html', {'formulario': formulario})    


def editar(request,id): #vista para la creacion de los equipos
    abmequipo = Equipo.objects.get(id=id)
    formulario = EquipoForm(request.POST or None, request.FILES or None, instance = abmequipo)
    return render(request,'abmequipos/editar.html', {'formulario':formulario})    


def eliminar(request,id):
    equipo = Equipo.objects.get(id=id)
    equipo.delete()
    return redirect('abmequipos') 