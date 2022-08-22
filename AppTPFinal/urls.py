from django.urls import path
from AppTPFinal.views import Main, cargar_literatura, cargar_Musica, cargar_Cine, datos_usuario, datos_crear_usuario, \
    mostrar_literatura

urlpatterns = [
    path('', Main, name='TPFinalMain'),
    path('CrearUsuario/', datos_crear_usuario, name='TPFinalCrearUsuarios'),
    path('DatosUsuario/', datos_usuario, name='TPFinalMostrarUsuarios'),
    path('CrearLiteratura/', cargar_literatura, name='TPFinalCargarliteratura'),
    path('Musica/', cargar_Musica, name='TPFinalCargarMusica'),
    path('Cine/', cargar_Cine, name='TPFinalCargarCine'),
    path('LiteraturaExistente/', mostrar_literatura, name='TPFinalBuscarLiteratura'),

]
