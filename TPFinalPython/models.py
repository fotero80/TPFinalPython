from django.db import models


class Literatura (models.Model):
    nombre_literatura = models.CharField(max_length=50)
    autor_literatura = models.CharField(max_length=50)
    editorial_literatura = models.CharField(max_length=50)
    año_edicion_literatura = models.IntegerField()
    email_usuario_literatura = models.EmailField()


class Musica (models.Model):
    nombre_artista_musica = models.CharField(max_length=50)
    nombre_disco_musica = models.CharField(max_length=50)
    año_lanzamiento_musica = models.CharField(max_length=50)
    email_usuario_musica = models.EmailField()


class Cine (models.Model):
    nombre_pelicula_cine = models.CharField(max_length=50)
    nombre_director_cine = models.CharField(max_length=50)
    año_lanzamiento_musica = models.CharField(max_length=50)
    email_usuario_cine = models.EmailField()

class Usuario (models.Model):
    nombre_usuario = models.CharField(max_length=50)
    apellido_usuario = models.CharField(max_length=50)
    fecha_nacimiento_usuario = models.DateField(max_length=8)
    email_usuario = models.EmailField()