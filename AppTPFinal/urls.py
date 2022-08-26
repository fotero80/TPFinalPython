from django.urls import path
from AppTPFinal.views import *

urlpatterns = [
    path('', Main, name='TPFinalMain'),
    #Urls utilizadas para el CRUD de usuarios
    path('Usuario/Crear/', usuario_crear, name='TPFinalUsuariosCrear'),
    path('Usuario/Buscar/', usuario_buscar, name='TPFinalUsuariosBuscar'),
    path('Usuario/Eliminar/<int:id_usuario>', usuario_eliminar, name='TPFinalUsuariosEliminar'),

    #Urls utilizadas para el CRUD de literatura
    path('Literatura/Crear/', cargar_literatura, name='TPFinalLiteraturaCrear'),
    path('Literatura/Buscar/', buscar_literatura, name='TPFinalLiteraturaBuscar'),
    path('Literatura/Eliminar/<int:id_literatura>', literatura_eliminar, name='TPFinalLiteraturaEliminar'),

    # Urls utilizadas para el CRUD de musica
    path('Musica/Crear/', cargar_Musica, name='TPFinalMusicaCrear'),
    path('Musica/Buscar/', buscar_musica, name='TPFinalMusicaBuscar'),
    path('Literatura/Eliminar/<int:id_musica>', musica_eliminar, name='TPFinalMusicaEliminar'),

    # Urls utilizadas para el CRUD de cine
    path('Cine/Crear/', cargar_Cine, name='TPFinalCineCrear'),
    path('Cine/Buscar/', buscar_cine, name='TPFinalCineBuscar'),
    path('Literatura/Eliminar/<int:id_literatura>', cine_eliminar, name='TPFinalCineEliminar'),

]
