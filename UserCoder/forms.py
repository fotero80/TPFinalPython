from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class DateImput(forms.DateInput):
    input_type = 'date'


class userRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    # username = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


class User_Form(forms.Form):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
