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


class Musica(models.Model):
    id_musica = models.AutoField(primary_key=True)
    nombre_artista_musica = models.CharField(max_length=50)
    nombre_disco_musica = models.CharField(max_length=50)
    descripcion_musica = RichTextField(blank=True, null=True)
    username_musica = models.CharField(max_length=50)
    fecha_creacion_musica = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Musica: {self.nombre_artista_musica} {self.nombre_disco_musica}"


class ImagenMusica(models.Model):
    id_musica = models.OneToOneField(Musica, on_delete=models.CASCADE)
    imgmus = models.ImageField(upload_to='musica', null=True, blank=True)


class Cine(models.Model):
    id_cine = models.AutoField(primary_key=True)
    nombre_pelicula_cine = models.CharField(max_length=50)
    nombre_director_cine = models.CharField(max_length=50)
    descripcion_cine = RichTextField(blank=True, null=True)
    username_cine = models.CharField(max_length=50)
    fecha_creacion_cine = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cine: {self.nombre_pelicula_cine} {self.nombre_director_cine}"


class ImagenCine(models.Model):
    id_cine = models.OneToOneField(Cine, on_delete=models.CASCADE)
    imgcin = models.ImageField(upload_to='cine', null=True, blank=True)


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50)
    apellido_usuario = models.CharField(max_length=50)
    fecha_nacimiento_usuario = models.DateField()
    email_usuario = models.EmailField(unique=True)
    fecha_creacion_usuario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Usuario: {self.nombre_usuario} {self.apellido_usuario}"
