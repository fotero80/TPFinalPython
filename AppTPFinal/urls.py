from django.urls import path
from AppTPFinal.views import Main, datos_crear_literatura, cargar_Musica, cargar_Cine, datos_Usuario, datos_crear_usuario

urlpatterns = [
    path('',Main, name='TPFinalMain'),
    path('CrearUsuario/', datos_crear_usuario, name='TPFinalCrearUsuarios'),
    path('DatosUsuario/', datos_Usuario, name='TPFinalMostrarUsuarios'),
    path('CrearLiteratura/', datos_crear_literatura, name='TPFinalCrearliteratura'),
    path('Musica/', cargar_Musica, name='TPFinalCargarMusica'),
    path('Cine/>', cargar_Cine, name='TPFinalCargarCine'),

]