from django.urls import path
from AppTPFinal.views import Main, cargar_literatura, cargar_Musica, cargar_Cine, usuario_buscar, usuario_crear, \
    buscar_literatura, buscar_cine, buscar_musica, usuario_eliminar

urlpatterns = [
    path('', Main, name='TPFinalMain'),
    #Urls utilizadas para el CRUD de usuarios
    path('Usuario/Crear/', usuario_crear, name='TPFinalUsuariosCrear'),
    path('Usuario/Buscar/', usuario_buscar, name='TPFinalUsuariosBuscar'),
    path('Usuario/Eliminar/<str:nombre_usuario>', usuario_eliminar, name='TPFinalUsuariosEliminar'),

    #Urls utilizadas para el CRUD de literatura
    path('Literatura/Crear/', cargar_literatura, name='TPFinalLiteraturaCrear'),
    path('Literatura/Buscar/', buscar_literatura, name='TPFinalLiteraturaBuscar'),

    # Urls utilizadas para el CRUD de musica
    path('Musica/Crear/', cargar_Musica, name='TPFinalMusicaCrear'),
    path('Musica/Buscar/', buscar_musica, name='TPFinalMusicaBuscar'),

    # Urls utilizadas para el CRUD de cine
    path('Cine/Crear/', cargar_Cine, name='TPFinalCineCrear'),
    path('Cine/Buscar/', buscar_cine, name='TPFinalCineBuscar'),

]
