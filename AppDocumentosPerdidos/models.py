from django.db import models
from ckeditor.fields import RichTextField


class Literatura(models.Model):
    id_literatura = models.AutoField(primary_key=True)
    nombre_literatura = models.CharField(max_length=50)
    autor_literatura = models.CharField(max_length=50)
    editorial_literatura = models.CharField(max_length=50)
    descripcion_literatura = RichTextField(blank=True, null=True)
    username_literatura = models.CharField(max_length=50)
    fecha_creacion_literatura = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Literatura: {self.nombre_literatura} {self.autor_literatura}"


class ImagenLiteratura(models.Model):
    id_literatura = models.OneToOneField(Literatura, on_delete=models.CASCADE)
    imglit = models.ImageField(upload_to='literatura', null=True, blank=True)


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50)
    apellido_usuario = models.CharField(max_length=50)
    fecha_nacimiento_usuario = models.DateField()
    email_usuario = models.EmailField(unique=True)
    fecha_creacion_usuario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Usuario: {self.nombre_usuario} {self.apellido_usuario}"
