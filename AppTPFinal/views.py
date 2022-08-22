from datetime import datetime
import ctypes

from django.shortcuts import render

from AppTPFinal.forms import Usuario_Form, Literatura_Form, Musica_Form, Cine_Form
from AppTPFinal.models import Cine, Usuario, Musica, Literatura
import pandas as pd
import sqlite3
con = sqlite3.connect("data/portal_mammals.sqlite")
cur = con.cursor()
df = pd.read_sql_query("SELECT * from surveys", con)

def Main(request):
    return render(request, 'AppCoder/main.html')


def datos_crear_usuario(request):
    contexto = {
        'formulariousuario': Usuario_Form()
    }
    return render(request, 'AppCoder/usercrear.html', contexto)


def datos_usuario(request):
    usr = Usuario_Form(request.POST)
    if request.method == 'POST':
        if usr.is_valid():
            usr = Usuario(
                nombre_usuario=request.POST.get('nombre_usuario'),
                apellido_usuario=request.POST.get('apellido_usuario'),
                fecha_nacimiento_usuario=request.POST.get('fecha_nacimiento_usuario'),
                email_usuario=request.POST.get('email_usuario'),
            )
        usr.save()
    contexto = {
        'usuario': usr
    }
    return render(request, 'AppCoder/datosusercreado.html', contexto)


def cargar_literatura(request):
    lit = Literatura_Form(request.POST)
    if request.method == 'POST':
        if lit.is_valid():
            lit = Literatura(
                nombre_literatura=request.POST.get('nombre_literatura'),
                autor_literatura=request.POST.get('autor_literatura'),
                editorial_literatura=request.POST.get('editorial_literatura'),
                anio_edicion_literatura=request.POST.get('anio_edicion_literatura'),
                email_usuario_literatura=request.POST.get('email_usuario_literatura'),
            )
        lit.save()
        ctypes.windll.user32.MessageBoxW(0, "Los datos se han cargado con exito", "mensaje", 0)

    contexto = {
        'formulariocargarliteratura': Literatura_Form()
    }
    return render(request, 'AppCoder/literatura.html', contexto)


def mostrar_literatura(request):
    lit = Literatura_Form(request.POST)
    if request.method == 'POST':
        lit = Literatura(
            nombre_literatura=request.get('nombre_literatura'),
            autor_literatura=request.get('autor_literatura'),
            editorial_literatura=request.get('editorial_literatura'),
            anio_edicion_literatura=request.get('anio_edicion_literatura'),
            email_usuario_literatura=request.get('email_usuario_literatura'),
        )
    lit_data =
    contexto = {
        'lit_data': lit_data,
        'formularioliteratura': Literatura_Form()

    }
    return render(request, 'AppCoder/literaturabuscar.html', contexto)


def cargar_Musica(request):
    mus = Musica_Form(request.POST)
    if request.method == 'POST':
        if mus.is_valid():
            mus = Musica(
                nombre_artista_musica=request.POST.get('nombre_artista_musica'),
                nombre_disco_musica=request.POST.get('nombre_disco_musica'),
                anio_lanzamiento_musica=request.POST.get('anio_lanzamiento_musica'),
                email_usuario_musica=request.POST.get('email_usuario_musica'),
            )
        mus.save()
        ctypes.windll.user32.MessageBoxW(0, "Los datos se han cargado con exito", "mensaje", 0)

    contexto = {
        'formulariomusica': Musica_Form()
    }
    return render(request, 'AppCoder/musica.html', contexto)


def cargar_Cine(request):
    cine = Cine_Form(request.POST)
    if request.method == 'POST':
        if cine.is_valid():
            cine = Cine(
                nombre_pelicula_cine=request.POST.get('nombre_pelicula_cine'),
                nombre_director_cine=request.POST.get('nombre_director_cine'),
                anio_lanzamiento_cine=request.POST.get('anio_lanzamiento_cine'),
                email_usuario_cine=request.POST.get('email_usuario_cine'),
            )
        cine.save()
        ctypes.windll.user32.MessageBoxW(0, "Los datos se han cargado con exito", "mensaje", 0)

    contexto = {
        'formulariocine': Cine_Form()
    }
    return render(request, 'AppCoder/cine.html', contexto)
