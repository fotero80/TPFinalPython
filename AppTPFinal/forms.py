from django import forms


class DateImput(forms.DateInput):
    input_type = 'date'


class Literatura_Form(forms.Form):
    nombre_literatura = forms.CharField(max_length=50)
    autor_literatura = forms.CharField(max_length=50)
    editorial_literatura = forms.CharField(max_length=50)
    anio_edicion_literatura = forms.IntegerField()
    imglit = forms.ImageField(required=False)
    #email_usuario_literatura = forms.EmailField()


class Buscar_Literatura_Form(forms.Form):
    nombre_literatura = forms.CharField(max_length=50)
    autor_literatura = forms.CharField(max_length=50)
    editorial_literatura = forms.CharField(max_length=50)
    anio_edicion_literatura = forms.IntegerField()


class Musica_Form(forms.Form):
    nombre_artista_musica = forms.CharField(max_length=50)
    nombre_disco_musica = forms.CharField(max_length=50)
    anio_lanzamiento_musica = forms.IntegerField()
    #email_usuario_musica = forms.EmailField()


class Buscar_Musica_Form(forms.Form):
    nombre_artista_musica = forms.CharField(max_length=50)
    nombre_disco_musica = forms.CharField(max_length=50)
    anio_lanzamiento_musica = forms.IntegerField()


class Cine_Form(forms.Form):
    nombre_pelicula_cine = forms.CharField(max_length=50)
    nombre_director_cine = forms.CharField(max_length=50)
    anio_lanzamiento_cine = forms.IntegerField()
    #email_usuario_cine = forms.EmailField()


class Buscar_Cine_Form(forms.Form):
    nombre_pelicula_cine = forms.CharField(max_length=50)
    nombre_director_cine = forms.CharField(max_length=50)
    anio_lanzamiento_cine = forms.IntegerField()
