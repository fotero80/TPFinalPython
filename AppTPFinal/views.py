import ctypes

from django.shortcuts import render, redirect

from AppTPFinal.forms import Usuario_Form, Literatura_Form, Musica_Form, Cine_Form, Buscar_Literatura_Form, \
    Buscar_Musica_Form, Buscar_Cine_Form
from AppTPFinal.models import Cine, Usuario, Musica, Literatura


def Main(request):
    return render(request, 'AppCoder/main.html')

#--------------------------------------------------------------------------------------------------------
#Modulos de Usuarios
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


def usuario_modificar(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario=id_usuario)

    if request.method == 'POST':
        usr = Usuario_Form(request.POST)
        if usr.is_valid():
            data = usr.cleaned_data

            usuario.nombre_usuario= data.get('nombre_usuario')
            usuario.apellido_usuario= data.get('apellido_usuario')
            usuario.fecha_nacimiento_usuario= data.get('fecha_nacimiento_usuario')
            usuario.email_usuario= data.get('email_usuario')

            usuario.save()
            ctypes.windll.user32.MessageBoxW(0, "Los datos se han actualizado con exito", "mensaje", 0)
            return redirect('TPFinalUsuariosBuscar')


    usuario_form = Usuario_Form(initial={
                'nombre_usuario': usuario.nombre_usuario,
                'apellido_usuario': usuario.apellido_usuario,
                'fecha_nacimiento_usuario': usuario.fecha_nacimiento_usuario,
                'email_usuario': usuario.email_usuario
                }
             )
    contexto = {
        'formulariousuario' : usuario_form
    }

    return render(request, 'AppCoder/usuario/usuariomodificar.html', contexto)


#--------------------------------------------------------------------------------------------------------
#Modulos de Literatura
def literatura_crear(request):
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


def literatura_buscar(request):
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
    lit = Literatura.objects.get(id_literatura=id_literatura)
    lit.delete()

    return redirect('TPFinalLiteraturaBuscar')


def literatura_modificar(request, id_literatura):
    lit = Literatura.objects.get(id_literatura=id_literatura)

    if request.method == 'POST':
        Lite = Literatura_Form(request.POST)
        if Lite.is_valid():
            data = Lite.cleaned_data

            lit.nombre_literatura= data.get('nombre_literatura')
            lit.autor_literatura= data.get('autor_literatura')
            lit.editorial_literatura= data.get('editorial_literatura')
            lit.anio_edicion_literatura= data.get('anio_edicion_literatura')
            lit.email_usuario_literatura = data.get('email_usuario_literatura')

            lit.save()
            ctypes.windll.user32.MessageBoxW(0, "Los datos se han actualizado con exito", "mensaje", 0)
            return redirect('TPFinalLiteraturaBuscar')


    literatura_form = Literatura_Form(initial={
                'nombre_literatura': lit.nombre_literatura,
                'autor_literatura': lit.autor_literatura,
                'editorial_literatura': lit.editorial_literatura,
                'anio_edicion_literatura': lit.anio_edicion_literatura,
                'email_usuario_literatura': lit.email_usuario_literatura
                }
             )
    contexto = {
        'formulariocargarliteratura': literatura_form
    }

    return render(request, 'AppCoder/literatura/literaturamodificar.html', contexto)

#--------------------------------------------------------------------------------------------------------
#Modulos de Musica
def musica_crear(request):
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

def musica_buscar(request):
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
    musica = Musica.objects.get(id_musica=id_musica)
    musica.delete()

    return redirect('TPFinalMusicaBuscar')


def musica_modificar(request, id_musica):
    mus = Musica.objects.get(id_musica=id_musica)

    if request.method == 'POST':
        Musi = Musica_Form(request.POST)
        if Musi.is_valid():
            data = Musi.cleaned_data

            mus.nombre_artista_musica= data.get('nombre_artista_musica')
            mus.nombre_disco_musica= data.get('nombre_disco_musica')
            mus.anio_lanzamiento_musica= data.get('anio_lanzamiento_musica')
            mus.email_usuario_musica= data.get('email_usuario_musica')

            mus.save()
            ctypes.windll.user32.MessageBoxW(0, "Los datos se han actualizado con exito", "mensaje", 0)
            return redirect('TPFinalLiteraturaBuscar')


    musica_form = Musica_Form(initial={
                'nombre_artista_musica': mus.nombre_artista_musica,
                'nombre_disco_musica': mus.nombre_disco_musica,
                'anio_lanzamiento_musica': mus.anio_lanzamiento_musica,
                'email_usuario_musica': mus.email_usuario_musica,
                }
             )
    contexto = {
        'formulariomusica': musica_form
    }

    return render(request, 'AppCoder/musica/musicamodificar.html', contexto)

#--------------------------------------------------------------------------------------------------------
#Modulos de Cine
def cine_crear(request):
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

def cine_buscar(request):
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
    cine = Cine.objects.get(id_cine=id_cine)
    cine.delete()

    return redirect('TPFinalCineBuscar')

def cine_modificar(request, id_cine):
    cine = Cine.objects.get(id_cine=id_cine)

    if request.method == 'POST':
        cine_temp = Cine_Form(request.POST)
        if cine_temp.is_valid():
            data = cine_temp.cleaned_data

            cine.nombre_pelicula_cine= data.get('nombre_pelicula_cine')
            cine.nombre_director_cine= data.get('nombre_director_cine')
            cine.anio_lanzamiento_cine= data.get('anio_lanzamiento_cine')
            cine.email_usuario_cine= data.get('email_usuario_cine')

            cine.save()
            ctypes.windll.user32.MessageBoxW(0, "Los datos se han actualizado con exito", "mensaje", 0)
            return redirect('TPFinalCineBuscar')


    cine_form = Cine_Form(initial={
                'nombre_pelicula_cine': cine.nombre_pelicula_cine,
                'nombre_director_cine': cine.nombre_director_cine,
                'anio_lanzamiento_cine': cine.anio_lanzamiento_cine,
                'email_usuario_cine': cine.email_usuario_cine,
                }
             )
    contexto = {
        'formulariocine': cine_form
    }

    return render(request, 'AppCoder/cine/cinemodificar.html', contexto)