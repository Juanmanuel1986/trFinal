from django.urls import path 
from . import views # para acceder a las vistas, para preguntarle al usuario a que vista vamos a entrar a traves de la url.
from django.conf import settings
from django.contrib.staticfiles.urls import static

#logout
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', views.inicio, name='inicio'), # aqui el usuario puede entrar y acceder a la vista. En la parte de name, dice con la palabra que voy a ingresar en este caso inicio.
    path('nosotros', views.nosotros, name='nosotros'),
    #     URL  ----- VISTA ------ ?
    path('abmequipos', views.abmequipos, name='abmequipos'),
    path('niveles', views.niveles, name='niveles'),
    path('abmequipos/crear', views.crear, name='crear'),# con esto podemos acceder a la vista crear
    #path('abmequipos/editar', views.editar, name='editar'),#
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
   # path('eliminar/<id>', views.eliminar, name='eliminar'),
    path('abmequipos/editar/<int:id>', views.editar, name='editar'),#

    #login
    path('login', views.login_request, name="Login"),

    #registro
    path('register', views.register, name='Register'),
 
    #logout
    path('logout', LogoutView.as_view(template_name='paginas/logout.html'), name='Logout'),
 


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
