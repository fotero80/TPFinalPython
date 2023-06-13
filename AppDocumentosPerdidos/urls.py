from django.urls import path
from AppDocumentosPerdidos.views import *
from UserCoder.views import *


urlpatterns = [
    path('', Main, name='DocumentosPerdidosMain'),

    #Urls utilizadas para el CRUD de documento
    path('Documento/Crear/', documento_crear, name='DocumentoCrear'),
    path('Documento/Buscar/', documento_buscar, name='DocumentoBuscar'),
    path('Documento/Eliminar/<int:id_documento>', documento_eliminar, name='DocumentoEliminar'),
    path('Documento/Modificar/<int:id_documento>', documento_modificar, name='DocumentoModificar'),
    path('Documento/BuscarVer/', documento_buscar_ver, name='DocumentoBuscarVer'),
    path('Documento/Ver/<int:id_documento>', documento_ver, name='DocumentoVer'),

    path('Contacto', contact, name='Contact'),

]