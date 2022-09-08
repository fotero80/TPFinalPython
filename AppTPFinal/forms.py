from django import forms
from ckeditor.widgets import CKEditorWidget


class DateImput(forms.DateInput):
    input_type = 'date'


class Literatura_Form(forms.Form):
    nombre_literatura = forms.CharField(max_length=50)
    autor_literatura = forms.CharField(max_length=50)
    editorial_literatura = forms.CharField(max_length=50)
    descripcion_literatura = forms.CharField(widget=CKEditorWidget())
    imglit = forms.ImageField(required=False)



class Buscar_Literatura_Form(forms.Form):
    nombre_literatura = forms.CharField(max_length=50)
    autor_literatura = forms.CharField(max_length=50)
    editorial_literatura = forms.CharField(max_length=50)
    descripcion_literatura = forms.CharField(max_length=50)


class Musica_Form(forms.Form):
    nombre_artista_musica = forms.CharField(max_length=50)
    nombre_disco_musica = forms.CharField(max_length=50)
    descripcion_musica = forms.CharField(widget=CKEditorWidget())
    imgmus = forms.ImageField(required=False)


class Buscar_Musica_Form(forms.Form):
    nombre_artista_musica = forms.CharField(max_length=50)
    nombre_disco_musica = forms.CharField(max_length=50)
    descripcion_musica = forms.CharField(max_length=50)


class Cine_Form(forms.Form):
    nombre_pelicula_cine = forms.CharField(max_length=50)
    nombre_director_cine = forms.CharField(max_length=50)
    descripcion_cine = forms.CharField(widget=CKEditorWidget())
    imgcin = forms.ImageField(required=False)


class Buscar_Cine_Form(forms.Form):
    nombre_pelicula_cine = forms.CharField(max_length=50)
    nombre_director_cine = forms.CharField(max_length=50)
    descripcion_cine = forms.CharField(max_length=50)
