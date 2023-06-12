from django.urls import path
from AppDocumentosPerdidos.views import *
from UserCoder.views import *


urlpatterns = [
    path('', Main, name='DocumentosPerdidosMain'),

    #Urls utilizadas para el CRUD de literatura
    path('Literatura/Crear/', literatura_crear, name='LiteraturaCrear'),
    path('Literatura/Buscar/', literatura_buscar, name='LiteraturaBuscar'),
    path('Literatura/Eliminar/<int:id_literatura>', literatura_eliminar, name='LiteraturaEliminar'),
    path('Literatura/Modificar/<int:id_literatura>', literatura_modificar, name='LiteraturaModificar'),
    path('Literatura/BuscarVer/', literatura_buscar_ver, name='LiteraturaBuscarVer'),
    path('Literatura/Ver/<int:id_literatura>', literatura_ver, name='LiteraturaVer'),

    path('Contacto', contact, name='Contact'),

]