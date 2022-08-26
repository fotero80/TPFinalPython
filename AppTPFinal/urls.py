from django.urls import path
from AppTPFinal.views import *

urlpatterns = [
    path('', Main, name='TPFinalMain'),
    #Urls utilizadas para el CRUD de usuarios
    path('Usuario/Crear/', usuario_crear, name='TPFinalUsuariosCrear'),
    path('Usuario/Buscar/', usuario_buscar, name='TPFinalUsuariosBuscar'),
    path('Usuario/Eliminar/<int:id_usuario>', usuario_eliminar, name='TPFinalUsuariosEliminar'),
    path('Usuario/Modificar/<int:id_usuario>', usuario_modificar, name='TPFinalUsuariosModificar'),

    #Urls utilizadas para el CRUD de literatura
    path('Literatura/Crear/', literatura_crear, name='TPFinalLiteraturaCrear'),
    path('Literatura/Buscar/', literatura_buscar, name='TPFinalLiteraturaBuscar'),
    path('Literatura/Eliminar/<int:id_literatura>', literatura_eliminar, name='TPFinalLiteraturaEliminar'),
    path('Literatura/Modificar/<int:id_literatura>', literatura_modificar, name='TPFinalLiteraturaModificar'),

    # Urls utilizadas para el CRUD de musica
    path('Musica/Crear/', musica_crear, name='TPFinalMusicaCrear'),
    path('Musica/Buscar/', musica_buscar, name='TPFinalMusicaBuscar'),
    path('Musica/Eliminar/<int:id_musica>', musica_eliminar, name='TPFinalMusicaEliminar'),
    path('Musica/Modificar/<int:id_musica>', musica_modificar, name='TPFinalMusicaModificar'),

    # Urls utilizadas para el CRUD de cine
    path('Cine/Crear/', cine_crear, name='TPFinalCineCrear'),
    path('Cine/Buscar/', cine_buscar, name='TPFinalCineBuscar'),
    path('Cine/Eliminar/<int:id_cine>', cine_eliminar, name='TPFinalCineEliminar'),
    path('Cine/Modificar/<int:id_cine>', cine_modificar, name='TPFinalCineModificar'),

]
