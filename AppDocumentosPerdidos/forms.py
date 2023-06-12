
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