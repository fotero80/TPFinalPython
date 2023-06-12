from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from AppDocumentosPerdidos.views import Main

urlpatterns = [
    path('', Main,),
    path('admin/', admin.site.urls),
    path('DocumentosPerdidos/', include('AppDocumentosPerdidos.urls')),
    path('DocumentosPerdidos/', include('UserCoder.urls')),
    path('DocumentosPerdidos/', include('Mensajes.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
