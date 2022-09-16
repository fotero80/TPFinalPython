from django import forms
from ckeditor.widgets import CKEditorWidget

class DateImput(forms.DateInput):
    input_type = 'date'


class Mensajes_Form(forms.Form):
    mensaje = forms.CharField(widget=CKEditorWidget())

class Buscar_Mensajes_Form(forms.Form):
    usuario_origen = forms.CharField(max_length=50)
    usuario_destino = forms.CharField(max_length=50)
    mensaje = forms.CharField(max_length=50)

