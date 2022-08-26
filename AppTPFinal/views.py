import ctypes

from django.shortcuts import render, redirect

from AppTPFinal.forms import Usuario_Form, Literatura_Form, Musica_Form, Cine_Form, Buscar_Literatura_Form, \
    Buscar_Musica_Form, Buscar_Cine_Form
from AppTPFinal.models import Cine, Usuario, Musica, Literatura


def Main(request):
    return render(request, 'AppCoder/main.html')


def usuario_crear(request):
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
        ctypes.windll.user32.MessageBoxW(0, "Los datos se han cargado con exito", "mensaje", 0)

    contexto = {
        'formulariousuario': Usuario_Form()
    }
    return render(request, 'AppCoder/usuario/usuario.html', contexto)


def usuario_buscar(request):
    a_buscar = []
    if request.method == 'POST':
        nombre_usuario = request.POST.get('nombre_usuario')
        apellido_usuario = request.POST.get('apellido_usuario')
        fecha_nacimiento_usuario = request.POST.get('fecha_nacimiento_usuario')
        email_usuario = request.POST.get('email_usuario')
        a_buscar = Usuario.objects.filter(nombre_usuario__icontains=nombre_usuario) & \
                   Usuario.objects.filter(apellido_usuario__icontains=apellido_usuario) & \
                   Usuario.objects.filter(fecha_nacimiento_usuario__icontains=fecha_nacimiento_usuario) & \
                   Usuario.objects.filter(email_usuario__icontains=email_usuario)
    contexto = {
        'buscar_usuario': Usuario_Form(),
        'usuario': a_buscar
    }
    return render(request, 'AppCoder/usuario/usuariobuscar.html', contexto)


def usuario_eliminar(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario=id_usuario)
    usuario.delete()

    return redirect('TPFinalUsuariosBuscar')

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
    return render(request, 'AppCoder/literatura/literatura.html', contexto)


def buscar_literatura(request):
    a_buscar = []
    if request.method == 'POST':
        nombre_literatura = request.POST.get('nombre_literatura')
        autor_literatura = request.POST.get('autor_literatura')
        editorial_literatura = request.POST.get('editorial_literatura')
        anio_edicion_literatura = request.POST.get('anio_edicion_literatura')
        a_buscar = Literatura.objects.filter(nombre_literatura__icontains=nombre_literatura) & \
                   Literatura.objects.filter(autor_literatura__icontains=autor_literatura) & \
                   Literatura.objects.filter(editorial_literatura__icontains=editorial_literatura) & \
                   Literatura.objects.filter(anio_edicion_literatura__icontains=anio_edicion_literatura)

    contexto = {
        'buscar_literatura': Buscar_Literatura_Form(),
        'literatura': a_buscar
    }
    return render(request, 'AppCoder/literatura/literaturabuscar.html', contexto)


def literatura_eliminar(request, id_literatura):
    literatura = Literatura.objects.get(id_literatura=id_literatura)
    literatura.delete()

    return redirect('TPFinalLiteraturaBuscar')

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
    return render(request, 'AppCoder/musica/musica.html', contexto)

def buscar_musica(request):
    a_buscar = []
    if request.method == 'POST':
        nombre_artista_musica = request.POST.get('nombre_artista_musica')
        nombre_disco_musica = request.POST.get('nombre_disco_musica')
        anio_lanzamiento_musica = request.POST.get('anio_lanzamiento_musica')
        a_buscar = Musica.objects.filter(nombre_artista_musica__icontains=nombre_artista_musica) & \
                   Musica.objects.filter(nombre_disco_musica__icontains=nombre_disco_musica) & \
                   Musica.objects.filter(anio_lanzamiento_musica__icontains=anio_lanzamiento_musica)

    contexto = {
        'buscar_musica': Buscar_Musica_Form(),
        'musica': a_buscar
    }
    return render(request, 'AppCoder/musica/musicabuscar.html', contexto)


def musica_eliminar(request, id_musica):
    musica = Usuario.objects.get(id_musica=id_musica)
    musica.delete()

    return redirect('TPFinalMusicaBuscar')


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
    return render(request, 'AppCoder/cine/cine.html', contexto)

def buscar_cine(request):
    a_buscar = []
    if request.method == 'POST':
        nombre_pelicula_cine = request.POST.get('nombre_pelicula_cine')
        nombre_director_cine = request.POST.get('nombre_director_cine')
        anio_lanzamiento_cine = request.POST.get('anio_lanzamiento_cine')
        a_buscar = Cine.objects.filter(nombre_pelicula_cine__icontains=nombre_pelicula_cine) & \
                   Cine.objects.filter(nombre_director_cine__icontains=nombre_director_cine) & \
                   Cine.objects.filter(anio_lanzamiento_cine__icontains=anio_lanzamiento_cine)

    contexto = {
        'buscar_cine': Buscar_Cine_Form(),
        'cine': a_buscar
    }
    return render(request, 'AppCoder/cine/cinebuscar.html', contexto)

def cine_eliminar(request, id_cine):
    cine = Usuario.objects.get(id_cine=id_cine)
    cine.delete()

    return redirect('TPFinalCineBuscar')