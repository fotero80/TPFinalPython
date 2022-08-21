from datetime import datetime

from django.shortcuts import render

from AppTPFinal.forms import Usuario_Form
from AppTPFinal.models import Cine, Usuario, Musica, Literatura


def cargar_Literatura(request):
    if (request.method == 'POST'):
        lit = Literatura(
            nombre_literatura=request.POST.get("nombre_literatura"),
            autor_literatura=request.POST.get(autor_literatura),
            editorial_literatura=request.POST.get(editorial_literatura),
            anio_edicion_literatura=request.POST.get(anio_edicion_literatura),
            email_usuario_literatura=request.POST.get(email_usuario_literatura)
        )
        lit.save()
    contexto = {
        "nombre_literatura": lit.nombre_literatura,
        "autor_literatura": lit.autor_literatura,
        "editorial_literatura": lit.editorial_literatura,
        "anio_edicion_literatura": lit.anio_edicion_literatura,
        "email_usuario_literatura": lit.email_usuario_literatura,
        "fecha_creacion_literatura": datetime.now()
    }
    return render(request, 'literatura.html', contexto)


def cargar_Musica(request, nombre_artista_musica, nombre_disco_musica, anio_lanzamiento_musica, email_usuario_musica):
    mus = Musica(nombre_artista_musica=nombre_artista_musica, nombre_disco_musica=nombre_disco_musica,
                 anio_lanzamiento_musica=anio_lanzamiento_musica, email_usuario_musica=email_usuario_musica)
    mus.save()
    contexto = {
        "nombre_artista_musica": mus.nombre_artista_musica,
        "nombre_disco_musica": mus.nombre_disco_musica,
        "anio_lanzamiento_musica": mus.anio_lanzamiento_musica,
        "email_usuario_musica": mus.email_usuario_musica,
        "fecha_creacion_musica": datetime.now()
    }
    return render(request, 'templateAutores.html', contexto)


def cargar_Cine(request, nombre_pelicula_cine, nombre_director_cine, anio_lanzamiento_cine, email_usuario_cine):
    edi = Cine(nombre_pelicula_cine=nombre_pelicula_cine, nombre_director_cine=nombre_director_cine,
               anio_lanzamiento_cine=anio_lanzamiento_cine, email_usuario_cine=email_usuario_cine)
    edi.save()
    contexto = {
        "nombre_pelicula_cine": nombre_pelicula_cine,
        "nombre_director_cine": nombre_director_cine,
        "anio_lanzamiento_cine": anio_lanzamiento_cine,
        "email_usuario_cine": email_usuario_cine,
        "fecha_crecion_cine": datetime.now()
    }
    return render(request, 'templateEditoriales.html', contexto)


def datos_Usuario(request):
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
        'formulariousuario': Usuario_Form()
    }
    return render(request, 'AppCoder/datosusercreado.html', contexto)


def Main(request):
    return render(request, 'AppCoder/main.html')


def datos_crear_usuario(request):
    contexto = {
        'formulariousuario': Usuario_Form()
    }
    return render(request, 'AppCoder/usercrear.html', contexto)
