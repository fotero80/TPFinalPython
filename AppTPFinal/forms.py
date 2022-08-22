from django import forms
from datetime import datetime


class Literatura_Form(forms.Form):
    nombre_literatura = forms.CharField(max_length=50)
    autor_literatura = forms.CharField(max_length=50)
    editorial_literatura = forms.CharField(max_length=50)
    anio_edicion_literatura = forms.IntegerField()
    email_usuario_literatura = forms.EmailField()


class Buscar_Literatura_Form(forms.Form):
    nombre_literatura = forms.CharField(max_length=50)
    autor_literatura = forms.CharField(max_length=50)
    editorial_literatura = forms.CharField(max_length=50)
    anio_edicion_literatura = forms.IntegerField()


class Musica_Form(forms.Form):
    nombre_artista_musica = forms.CharField(max_length=50)
    nombre_disco_musica = forms.CharField(max_length=50)
    anio_lanzamiento_musica = forms.IntegerField()
    email_usuario_musica = forms.EmailField()


class Cine_Form(forms.Form):
    nombre_pelicula_cine = forms.CharField(max_length=50)
    nombre_director_cine = forms.CharField(max_length=50)
    anio_lanzamiento_cine = forms.IntegerField()
    email_usuario_cine = forms.EmailField()


class Usuario_Form(forms.Form):
    nombre_usuario = forms.CharField(max_length=50)
    apellido_usuario = forms.CharField(max_length=50)
    fecha_nacimiento_usuario = forms.DateField()
    email_usuario = forms.EmailField()
