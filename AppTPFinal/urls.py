from django.urls import path
from AppTPFinal.views import Main, cargar_Literatura, cargar_Musica, cargar_Cine, datos_Usuario, datos_crear_usuario

urlpatterns = [
    path('',Main, name='TPFinalMain'),
    path('Literatura/', cargar_Literatura, name='TPFinalCargarLiteratura'),
    path('Musica/', cargar_Musica, name='TPFinalCargarMusica'),
    path('Cine/>', cargar_Cine, name='TPFinalCargarCine'),
    path('CrearUsuario/', datos_crear_usuario, name='TPFinalCrearUsuarios'),
    path('DatosUsuario/', datos_Usuario, name='TPFinalMostrarUsuarios'),

]