from django.db import models
from ckeditor.fields import RichTextField


class documento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    nombre_documento = models.CharField(max_length=50)
    autor_documento = models.CharField(max_length=50)
    editorial_documento = models.CharField(max_length=50)
    descripcion_documento = RichTextField(blank=True, null=True)
    username_documento = models.CharField(max_length=50)
    fecha_creacion_documento = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"documento: {self.nombre_documento} {self.autor_documento}"


class Imagendocumento(models.Model):
    id_documento = models.OneToOneField(documento, on_delete=models.CASCADE)
    imglit = models.ImageField(upload_to='documento', null=True, blank=True)


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50)
    apellido_usuario = models.CharField(max_length=50)
    fecha_nacimiento_usuario = models.DateField()
    email_usuario = models.EmailField(unique=True)
    fecha_creacion_usuario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Usuario: {self.nombre_usuario} {self.apellido_usuario}"
