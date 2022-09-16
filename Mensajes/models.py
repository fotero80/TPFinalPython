from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Mensajes(models.Model):
    id_mensaje = models.AutoField(primary_key=True)
    usuario_origen = models.CharField(max_length=50)
    usuario_destino = models.CharField(max_length=50)
    mensaje = RichTextField(blank=True, null=True)
    fecha_creacion_mensaje = models.DateTimeField(auto_now_add=True)
