from django.urls import path 
from . import views # para acceder a las vistas, para preguntarle al usuario a que vista vamos a entrar a traves de la url.


urlpatterns = [
    path('', views.inicio, name='inicio'), # aqui el usuario puede entrar y acceder a la vista. En la parte de name, dice con la palabra que voy a ingresar en este caso inicio.
]   #        vista q entra ,lo que escribe en el navegador.
