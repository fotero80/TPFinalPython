from django.contrib.auth.models import User
from django.db import models


class Literatura (models.Model):
    id_literatura = models.AutoField(primary_key=True)
    nombre_literatura = models.CharField(max_length=50)
    autor_literatura = models.CharField(max_length=50)
    editorial_literatura = models.CharField(max_length=50)
    anio_edicion_literatura = models.IntegerField()
    email_usuario_literatura = models.EmailField()

    def __str__(self):
        return f"Literatura: {self.nombre_literatura} {self.autor_literatura}"

class ImagenLiteratura (models.Model):
    id_literatura = models.OneToOneField(Literatura, on_delete=models.CASCADE) # Delete profile when user is deleted
    imglit = models.ImageField(upload_to='literatura', null=True, blank=True)


class Musica (models.Model):
    id_musica = models.AutoField(primary_key=True)
    nombre_artista_musica = models.CharField(max_length=50)
    nombre_disco_musica = models.CharField(max_length=50)
    anio_lanzamiento_musica = models.IntegerField()
    email_usuario_musica = models.EmailField()

    def __str__(self):
        return f"Musica: {self.nombre_artista_musica} {self.nombre_disco_musica}"


class Cine (models.Model):
    id_cine = models.AutoField(primary_key=True)
    nombre_pelicula_cine = models.CharField(max_length=50)
    nombre_director_cine = models.CharField(max_length=50)
    anio_lanzamiento_cine = models.IntegerField()
    email_usuario_cine = models.EmailField()

    def __str__(self):
        return f"Cine: {self.nombre_pelicula_cine} {self.nombre_director_cine}"


class Usuario (models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50)
    apellido_usuario = models.CharField(max_length=50)
    fecha_nacimiento_usuario = models.DateField()
    email_usuario = models.EmailField(unique=True)

    def __str__(self):
        return f"Usuario: {self.nombre_usuario} {self.apellido_usuario}"

