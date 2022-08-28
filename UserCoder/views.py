import ctypes
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

from UserCoder.forms import userRegisterForm, User_Form


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)
                messages.info(request, 'Inicio de sesion satisfactorio!')
            else:
                messages.info(request, 'Inicio de sesion fallido!')
        else:
            messages.info(request, 'Inicio de sesion fallido!')
        return redirect('TPFinalMain')

    contexto = {
        'form': AuthenticationForm(),
        'name_submit': 'LogIn',
        'tittle': 'Ingrese su nombre de usuario y contraseña para ingresar.'
    }
    return render(request, 'UserCoder/login.html', contexto)


def user_logon(request):
    if request.method == 'POST':
        form = userRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            ctypes.windll.user32.MessageBoxW(0, "Tu usuario fue registrado satisfactoriamente!", "mensaje", 0)
        else:
            ctypes.windll.user32.MessageBoxW(0, "Tu usuario no pudo ser registrado!", "mensaje", 0)
            return redirect('TPFinalMain')

    contexto = {
        'form': userRegisterForm(),
        'name_submit': 'Registrarse',
        'tittle': 'Ingrese sus datos para crear su usuario.'
    }
    return render(request, 'UserCoder/login.html', contexto)


@user_passes_test(lambda u: u.is_superuser)
def usuario_buscar(request):
    a_buscar = []
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        a_buscar = User.objects.filter(username__icontains=username) & \
                   User.objects.filter(first_name__icontains=first_name) & \
                   User.objects.filter(last_name__icontains=last_name) & \
                   User.objects.filter(email__icontains=email)
    contexto = {
        'buscar_usuario': User_Form(),
        'usuario': a_buscar
    }
    return render(request, 'UserCoder/usuariobuscar.html', contexto)


#@user_passes_test(lambda u: u.is_superuser)
def usuario_eliminar(request, username):
    usuario = User.objects.get(username=username)
    usuario.delete()

    return redirect('TPFinalUsuariosBuscar')

#@user_passes_test(lambda u: u.is_superuser)
def usuario_modificar(request, username):
    usuario = User.objects.get(username=username)

    if request.method == 'POST':
        usr = User_Form(request.POST)
        if usr.is_valid():
            data = usr.cleaned_data
            usuario.username= data.get('username')
            usuario.first_name= data.get('first_name')
            usuario.last_name= data.get('last_name')
            usuario.email= data.get('email')
            usuario.save()
            ctypes.windll.user32.MessageBoxW(0, "Los datos se han actualizado con exito", "mensaje", 0)
            return redirect('TPFinalUsuariosBuscar')

    usuario_form = User_Form(initial={
                'username': usuario.username,
                'first_name': usuario.first_name,
                'last_name': usuario.last_name,
                'email': usuario.email
                }
             )
    contexto = {
        'formulariousuario' : usuario_form
    }

    return render(request, 'UserCoder/usuariomodificar.html', contexto)