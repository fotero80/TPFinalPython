
from django import forms
from ckeditor.widgets import CKEditorWidget



class DateImput(forms.DateInput):
    input_type = 'date'


class documento_Form(forms.Form):
    nombre_documento = forms.CharField(max_length=50)
    autor_documento = forms.CharField(max_length=50)
    editorial_documento = forms.CharField(max_length=50)
    descripcion_documento = forms.CharField(widget=CKEditorWidget())
    imglit = forms.ImageField(required=False)


class Buscar_documento_Form(forms.Form):
    nombre_documento = forms.CharField(max_length=50)
    autor_documento = forms.CharField(max_length=50)
    editorial_documento = forms.CharField(max_length=50)
    descripcion_documento = forms.CharField(max_length=50)