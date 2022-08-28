from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('TPFinal/', include('AppTPFinal.urls')),
    path('TPFinal/', include('UserCoder.urls'))
]