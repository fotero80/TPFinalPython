import ctypes

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from AppTPFinal.forms import *
from AppTPFinal.models import *
from django.http import HttpResponse
from django.core.mail import send_mail


def Main(request):
    return render(request, 'AppCoder/main.html')


# --------------------------------------------------------------------------------------------------------
# Modulos de Literatura
@login_required()
def literatura_crear(request):
    lit = Literatura_Form(request.POST or None, request.FILES or None)
    username = None
    username = request.user.username
    if request.method == 'POST':
        if lit.is_valid():
            lit = Literatura(
                nombre_literatura=request.POST.get('nombre_literatura'),
                autor_literatura=request.POST.get('autor_literatura'),
                editorial_literatura=request.POST.get('editorial_literatura'),
                descripcion_literatura=request.POST.get('descripcion_literatura'),
                username_literatura=username,
            )
            lit.save()
        if 'imglit' in request.FILES:
            imagen = request.FILES["imglit"]
            img = ImagenLiteratura(id_literatura=lit, imglit=imagen)
            img.save()

        ctypes.windll.user32.MessageBoxW(0, "Los datos se han cargado con exito", "mensaje", 0)

    contexto = {
        'formulariocargarliteratura': Literatura_Form(),
    }
    return render(request, 'AppCoder/literatura/literatura.html', contexto)


@login_required()
def literatura_buscar(request):
    username = None
    username = request.user.username
    a_buscar = []
    if request.method == 'POST':
        nombre_literatura = request.POST.get('nombre_literatura')
        autor_literatura = request.POST.get('autor_literatura')
        editorial_literatura = request.POST.get('editorial_literatura')
        descripcion_literatura = request.POST.get('descripcion_literatura')
        if request.user.is_superuser:
            a_buscar = Literatura.objects.filter(nombre_literatura__icontains=nombre_literatura) & \
                       Literatura.objects.filter(autor_literatura__icontains=autor_literatura) & \
                       Literatura.objects.filter(editorial_literatura__icontains=editorial_literatura) & \
                       Literatura.objects.filter(descripcion_literatura__icontains=descripcion_literatura)
        else:
            a_buscar = Literatura.objects.filter(nombre_literatura__icontains=nombre_literatura) & \
                       Literatura.objects.filter(autor_literatura__icontains=autor_literatura) & \
                       Literatura.objects.filter(editorial_literatura__icontains=editorial_literatura) & \
                       Literatura.objects.filter(descripcion_literatura__icontains=descripcion_literatura) & \
                       Literatura.objects.filter(username_literatura=username)

    contexto = {
        'buscar_literatura': Buscar_Literatura_Form(),
        'literatura': a_buscar
    }
    return render(request, 'AppCoder/literatura/literaturabuscar.html', contexto)


def literatura_buscar_ver(request):
    a_buscar = []
    if request.method == 'POST':
        nombre_literatura = request.POST.get('nombre_literatura')
        autor_literatura = request.POST.get('autor_literatura')
        editorial_literatura = request.POST.get('editorial_literatura')
        descripcion_literatura = request.POST.get('descripcion_literatura')
        a_buscar = Literatura.objects.filter(nombre_literatura__icontains=nombre_literatura) & \
                    Literatura.objects.filter(autor_literatura__icontains=autor_literatura) & \
                    Literatura.objects.filter(editorial_literatura__icontains=editorial_literatura) & \
                    Literatura.objects.filter(descripcion_literatura__icontains=descripcion_literatura)

    contexto = {
        'buscar_literatura': Buscar_Literatura_Form(),
        'literatura': a_buscar
    }
    return render(request, 'AppCoder/literatura/literaturabuscarver.html', contexto)

@login_required()
def literatura_eliminar(request, id_literatura):
    lit = Literatura.objects.get(id_literatura=id_literatura)
    lit.delete()

    return redirect('TPFinalLiteraturaBuscar')


@login_required()
def literatura_modificar(request, id_literatura):
    lit = Literatura.objects.get(id_literatura=id_literatura)
    if request.method == 'POST':
        Lite = Literatura_Form(request.POST)
        if Lite.is_valid():
            data = Lite.cleaned_data
            lit.nombre_literatura = data.get('nombre_literatura')
            lit.autor_literatura = data.get('autor_literatura')
            lit.editorial_literatura = data.get('editorial_literatura')
            lit.descripcion_literatura = data.get('descripcion_literatura')
            lit.save()

            img = ImagenLiteratura.objects.filter(id_literatura=lit)
            if 'imglit' in request.FILES:
                imagen = request.FILES["imglit"]
                if img.exists():
                    if imagen:
                        img = img[0]
                        img.imglit = imagen
                        img.save()

                else:
                    img = ImagenLiteratura(id_literatura=lit, imglit=imagen)
                    img.save()

            ctypes.windll.user32.MessageBoxW(0, "Los datos se han actualizado con exito", "mensaje", 0)
            return redirect('TPFinalLiteraturaBuscar')

    literatura_form = Literatura_Form(initial={
        'nombre_literatura': lit.nombre_literatura,
        'autor_literatura': lit.autor_literatura,
        'editorial_literatura': lit.editorial_literatura,
        'descripcion_literatura': lit.descripcion_literatura,
        'username_literatura': lit.username_literatura
    }
    )
    contexto = {
        'formulariocargarliteratura': literatura_form,
        'literatura': lit,
    }

    return render(request, 'AppCoder/literatura/literaturamodificar.html', contexto)

def literatura_ver(request, id_literatura):
    lit = Literatura.objects.get(id_literatura=id_literatura)
    literatura_form = Literatura_Form(initial={
        'nombre_literatura': lit.nombre_literatura,
        'autor_literatura': lit.autor_literatura,
        'editorial_literatura': lit.editorial_literatura,
        'descripcion_literatura': lit.descripcion_literatura,
    }
    )
    contexto = {
        'formulariocargarliteratura': literatura_form,
        'literatura': lit,
    }

    return render(request, 'AppCoder/literatura/literaturaver.html', contexto)

# --------------------------------------------------------------------------------------------------------
# Modulos de Musica
@login_required()
def musica_crear(request):
    mus = Musica_Form(request.POST)
    username = None
    username = request.user.username
    if request.method == 'POST':
        if mus.is_valid():
            mus = Musica(
                nombre_artista_musica=request.POST.get('nombre_artista_musica'),
                nombre_disco_musica=request.POST.get('nombre_disco_musica'),
                descripcion_musica=request.POST.get('descripcion_musica'),
                username_musica=username,
            )
            mus.save()
        if 'imgmus' in request.FILES:
            imagen = request.FILES["imgmus"]
            img = ImagenMusica(id_musica=mus, imgmus=imagen)
            img.save()
        ctypes.windll.user32.MessageBoxW(0, "Los datos se han cargado con exito", "mensaje", 0)

    contexto = {
        'formulariomusica': Musica_Form()
    }
    return render(request, 'AppCoder/musica/musica.html', contexto)


@login_required()
def musica_buscar(request):
    username = None
    username = request.user.username
    a_buscar = []
    if request.method == 'POST':
        nombre_artista_musica = request.POST.get('nombre_artista_musica')
        nombre_disco_musica = request.POST.get('nombre_disco_musica')
        descripcion_musica = request.POST.get('descripcion_musica')
        if request.user.is_superuser:
            a_buscar = Musica.objects.filter(nombre_artista_musica__icontains=nombre_artista_musica) & \
                       Musica.objects.filter(nombre_disco_musica__icontains=nombre_disco_musica) & \
                       Musica.objects.filter(descripcion_musica__icontains=descripcion_musica)
        else:
            a_buscar = Musica.objects.filter(nombre_artista_musica__icontains=nombre_artista_musica) & \
                       Musica.objects.filter(nombre_disco_musica__icontains=nombre_disco_musica) & \
                       Musica.objects.filter(descripcion_musica__icontains=descripcion_musica) & \
                       Musica.objects.filter(username_musica=username)
    contexto = {
        'buscar_musica': Buscar_Musica_Form(),
        'musica': a_buscar
    }
    return render(request, 'AppCoder/musica/musicabuscar.html', contexto)

def musica_buscar_ver(request):
    a_buscar = []
    if request.method == 'POST':
        nombre_artista_musica = request.POST.get('nombre_artista_musica')
        nombre_disco_musica = request.POST.get('nombre_disco_musica')
        descripcion_musica = request.POST.get('descripcion_musica')
        a_buscar = Musica.objects.filter(nombre_artista_musica__icontains=nombre_artista_musica) & \
                    Musica.objects.filter(nombre_disco_musica__icontains=nombre_disco_musica) & \
                    Musica.objects.filter(descripcion_musica__icontains=descripcion_musica)
    contexto = {
        'buscar_musica': Buscar_Musica_Form(),
        'musica': a_buscar
    }
    return render(request, 'AppCoder/musica/musicabuscarver.html', contexto)


@login_required()
def musica_eliminar(request, id_musica):
    musica = Musica.objects.get(id_musica=id_musica)
    musica.delete()

    return redirect('TPFinalMusicaBuscar')


@login_required()
def musica_modificar(request, id_musica):
    mus = Musica.objects.get(id_musica=id_musica)

    if request.method == 'POST':
        Musi = Musica_Form(request.POST)
        if Musi.is_valid():
            data = Musi.cleaned_data
            mus.nombre_artista_musica = data.get('nombre_artista_musica')
            mus.nombre_disco_musica = data.get('nombre_disco_musica')
            mus.descripcion_musica = data.get('descripcion_musica')
            mus.save()

            img = ImagenMusica.objects.filter(id_musica=mus)
            if 'imgmus' in request.FILES:
                imagen = request.FILES["imgmus"]
                if img.exists():
                    if imagen:
                        img = img[0]
                        img.imgmus = imagen
                        img.save()

                else:
                    img = ImagenMusica(id_musica=mus, imgmus=imagen)
                    img.save()

            ctypes.windll.user32.MessageBoxW(0, "Los datos se han actualizado con exito", "mensaje", 0)
            return redirect('TPFinalMusicaBuscar')

    musica_form = Musica_Form(initial={
        'nombre_artista_musica': mus.nombre_artista_musica,
        'nombre_disco_musica': mus.nombre_disco_musica,
        'descripcion_musica': mus.descripcion_musica,
        'username_musica': mus.username_musica,
    }
    )
    contexto = {
        'formulariomusica': musica_form,
        'musica': mus,
    }

    return render(request, 'AppCoder/musica/musicamodificar.html', contexto)

def musica_ver(request, id_musica):
    mus = Musica.objects.get(id_musica=id_musica)
    musica_form = Musica_Form(initial={
        'nombre_artista_musica': mus.nombre_artista_musica,
        'nombre_disco_musica': mus.nombre_disco_musica,
        'descripcion_musica': mus.descripcion_musica,
    }
    )
    contexto = {
        'formulariomusica': musica_form,
        'musica': mus,
    }

    return render(request, 'AppCoder/musica/musicaver.html', contexto)

# --------------------------------------------------------------------------------------------------------
# Modulos de Cine
@login_required()
def cine_crear(request):
    cine = Cine_Form(request.POST)
    username = None
    username = request.user.username
    if request.method == 'POST':
        if cine.is_valid():
            cine = Cine(
                nombre_pelicula_cine=request.POST.get('nombre_pelicula_cine'),
                nombre_director_cine=request.POST.get('nombre_director_cine'),
                descripcion_cine=request.POST.get('descripcion_cine'),
                username_cine=username,
            )
            cine.save()
        if 'imgcin' in request.FILES:
            imagen = request.FILES["imgcin"]
            img = ImagenCine(id_cine=cine, imgcin=imagen)
            img.save()
        ctypes.windll.user32.MessageBoxW(0, "Los datos se han cargado con exito", "mensaje", 0)
    contexto = {
        'formulariocine': Cine_Form()
    }
    return render(request, 'AppCoder/cine/cine.html', contexto)


@login_required()
def cine_buscar(request):
    username = None
    username = request.user.username
    a_buscar = []
    if request.method == 'POST':
        nombre_pelicula_cine = request.POST.get('nombre_pelicula_cine')
        nombre_director_cine = request.POST.get('nombre_director_cine')
        descripcion_cine = request.POST.get('descripcion_cine')
        if request.user.is_superuser:
            a_buscar = Cine.objects.filter(nombre_pelicula_cine__icontains=nombre_pelicula_cine) & \
                       Cine.objects.filter(nombre_director_cine__icontains=nombre_director_cine) & \
                       Cine.objects.filter(descripcion_cine__icontains=descripcion_cine)
        else:
            a_buscar = Cine.objects.filter(nombre_pelicula_cine__icontains=nombre_pelicula_cine) & \
                       Cine.objects.filter(nombre_director_cine__icontains=nombre_director_cine) & \
                       Cine.objects.filter(descripcion_cine__icontains=descripcion_cine) & \
                       Cine.objects.filter(username_cine=username)

    contexto = {
        'buscar_cine': Buscar_Cine_Form(),
        'cine': a_buscar
    }
    return render(request, 'AppCoder/cine/cinebuscar.html', contexto)


def cine_buscar_ver(request):
    a_buscar = []
    if request.method == 'POST':
        nombre_pelicula_cine = request.POST.get('nombre_pelicula_cine')
        nombre_director_cine = request.POST.get('nombre_director_cine')
        descripcion_cine = request.POST.get('descripcion_cine')
        a_buscar = Cine.objects.filter(nombre_pelicula_cine__icontains=nombre_pelicula_cine) & \
                    Cine.objects.filter(nombre_director_cine__icontains=nombre_director_cine) & \
                    Cine.objects.filter(descripcion_cine__icontains=descripcion_cine)

    contexto = {
        'buscar_cine': Buscar_Cine_Form(),
        'cine': a_buscar
    }
    return render(request, 'AppCoder/cine/cinebuscarver.html', contexto)

@login_required()
def cine_eliminar(request, id_cine):
    cine = Cine.objects.get(id_cine=id_cine)
    cine.delete()

    return redirect('TPFinalCineBuscar')


@login_required()
def cine_modificar(request, id_cine):
    cine = Cine.objects.get(id_cine=id_cine)

    if request.method == 'POST':
        cine_temp = Cine_Form(request.POST)
        if cine_temp.is_valid():
            data = cine_temp.cleaned_data
            cine.nombre_pelicula_cine = data.get('nombre_pelicula_cine')
            cine.nombre_director_cine = data.get('nombre_director_cine')
            cine.descripcion_cine = data.get('descripcion_cine')
            cine.save()

            img = ImagenCine.objects.filter(id_cine=cine)
            if 'imgcin' in request.FILES:
                imagen = request.FILES["imgcin"]
                if img.exists():
                    if imagen:
                        img = img[0]
                        img.imgcin = imagen
                        img.save()

                else:
                    img = ImagenCine(id_cine=cine, imgcin=imagen)
                    img.save()

            ctypes.windll.user32.MessageBoxW(0, "Los datos se han actualizado con exito", "mensaje", 0)
            return redirect('TPFinalCineBuscar')

    cine_form = Cine_Form(initial={
        'nombre_pelicula_cine': cine.nombre_pelicula_cine,
        'nombre_director_cine': cine.nombre_director_cine,
        'descripcion_cine': cine.descripcion_cine,
        'username_cine': cine.username_cine,
    }
    )
    contexto = {
        'formulariocine': cine_form,
        'cine': cine,
    }

    return render(request, 'AppCoder/cine/cinemodificar.html', contexto)

def cine_ver(request, id_cine):
    cine = Cine.objects.get(id_cine=id_cine)
    cine_form = Cine_Form(initial={
        'nombre_pelicula_cine': cine.nombre_pelicula_cine,
        'nombre_director_cine': cine.nombre_director_cine,
        'descripcion_cine': cine.descripcion_cine,
    }
    )
    contexto = {
        'formulariocine': cine_form,
        'cine': cine,
    }

    return render(request, 'AppCoder/cine/cinever.html', contexto)

# --------------------------------------------------------------------------------------------------------
# Envio de email
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        subject= request.POST.get('Subject')
        message = request.POST.get('Message')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }
        message = '''
        New messege: {}
        
        From: {}
        '''.format(data['message'],data['email'])
        send_mail(data['subject'], message, '',['tpfinalpython@gmail.com'])
        ctypes.windll.user32.MessageBoxW(0, "Su mensaje se ha enviado con exito", "mensaje", 0)
        return redirect('TPFinalMain')

    return render(request,'AppCoder/main.html',{})