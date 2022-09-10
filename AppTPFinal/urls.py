from django.urls import path
from AppTPFinal.views import *
from UserCoder.views import *

urlpatterns = [
    path('', Main, name='TPFinalMain'),
    #Urls utilizadas para el CRUD de usuarios
    #path('Usuario/Crear/', user_logon, name='TPFinalUsuariosCrear'),
    #path('Usuario/Buscar/', usuario_buscar, name='TPFinalUsuariosBuscar'),
    #path('Usuario/Eliminar/<int:username>', usuario_eliminar, name='TPFinalUsuariosEliminar'),
    #path('Usuario/Modificar/<int:username>', usuario_modificar, name='TPFinalUsuariosModificar'),

    #Urls utilizadas para el CRUD de literatura
    path('Literatura/Crear/', literatura_crear, name='TPFinalLiteraturaCrear'),
    path('Literatura/Buscar/', literatura_buscar, name='TPFinalLiteraturaBuscar'),
    path('Literatura/Eliminar/<int:id_literatura>', literatura_eliminar, name='TPFinalLiteraturaEliminar'),
    path('Literatura/Modificar/<int:id_literatura>', literatura_modificar, name='TPFinalLiteraturaModificar'),
    path('Literatura/BuscarVer/', literatura_buscar_ver, name='TPFinalLiteraturaBuscarVer'),
    path('Literatura/Ver/<int:id_literatura>', literatura_ver, name='TPFinalLiteraturaVer'),

    # Urls utilizadas para el CRUD de musica
    path('Musica/Crear/', musica_crear, name='TPFinalMusicaCrear'),
    path('Musica/Buscar/', musica_buscar, name='TPFinalMusicaBuscar'),
    path('Musica/Eliminar/<int:id_musica>', musica_eliminar, name='TPFinalMusicaEliminar'),
    path('Musica/Modificar/<int:id_musica>', musica_modificar, name='TPFinalMusicaModificar'),
    path('Musica/BuscarVer/', musica_buscar_ver, name='TPFinalMusicaBuscarVer'),
    path('Musica/Ver/<int:id_musica>', musica_ver, name='TPFinalMusicaVer'),

    # Urls utilizadas para el CRUD de cine
    path('Cine/Crear/', cine_crear, name='TPFinalCineCrear'),
    path('Cine/Buscar/', cine_buscar, name='TPFinalCineBuscar'),
    path('Cine/Eliminar/<int:id_cine>', cine_eliminar, name='TPFinalCineEliminar'),
    path('Cine/Modificar/<int:id_cine>', cine_modificar, name='TPFinalCineModificar'),
    path('Cine/BuscarVer/', cine_buscar_ver, name='TPFinalCineBuscarVer'),
    path('Cine/Ver/<int:id_cine>', cine_ver, name='TPFinalCineVer'),

    path('Contacto', contact, name='Contact'),

]
