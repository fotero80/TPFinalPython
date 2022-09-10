from django.contrib.auth.views import LogoutView
from django.urls import path

from UserCoder.views import *

urlpatterns = [
    path('Login/', user_login, name='UserCoderLogin'),
    path('Logon/', user_logon, name='UserCoderLogon'),
    path('Logout/', LogoutView.as_view(template_name='UserCoder/logout.html'), name='UserCoderLogOut'),
    path('Usuario/Crear/', user_logon, name='TPFinalUsuariosCrear'),
    path('Usuario/Buscar/', usuario_buscar, name='TPFinalUsuariosBuscar'),
    path('Usuario/Eliminar/<str:username>', usuario_eliminar, name='TPFinalUsuariosEliminar'),
    path('Usuario/Modificar/<str:username>', usuario_modificar, name='TPFinalUsuariosModificar'),
]

