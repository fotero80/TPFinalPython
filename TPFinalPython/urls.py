from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from AppTPFinal.views import Main

urlpatterns = [
    path('', Main, name='TPFinalMain'),
    path('admin/', admin.site.urls),
    path('TPFinal/', include('AppTPFinal.urls')),
    path('TPFinal/', include('UserCoder.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
