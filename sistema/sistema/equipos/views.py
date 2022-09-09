from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Equipo
from .forms import EquipoForm,UserRegisterForm,UserEditForm

#login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


#decorador
# Para el decorador
from django.contrib.auth.decorators import login_required     



# Create your views here.
@login_required
def inicio(request): #es la solicitud que se le va a hacer a la aplicacion
    return render(request,'paginas/inicio.html') 

@login_required
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
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('abmequipos')
    return render(request,'abmequipos/editar.html', {'formulario':formulario})    


def eliminar(request,id):
    equipo = Equipo.objects.get(id=id)
    equipo.delete()
    return redirect('abmequipos') 



#login
def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "paginas/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "paginas/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "paginas/loginfallido.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "paginas/login.html", {"form": form})    


#registro

def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"paginas/inicio.html" ,  {"mensaje":"SU USUARIO FUE CREADO CORRECTAMENTE"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"paginas/registro.html" ,  {"form":form})


 #editarperfil
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "paginas/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "paginas/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})
