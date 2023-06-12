from django.contrib.auth.views import LogoutView
from django.urls import path

from Mensajes.views import *

app_name='Mensajes'

urlpatterns = [
    path('Mensaje/BuscarVer/', mensaje_buscar_ver, name='MensajeBuscarVer'),
    path('Mensaje/Ver/<int:id_mensaje>', mensaje_ver, name='MensajeVer'),
    path('Mensaje/Enviar/<str:username>', mensaje_crear, name='MensajeEnviar'),
]

