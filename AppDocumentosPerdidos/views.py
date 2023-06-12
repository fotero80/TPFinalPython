from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from AppDocumentosPerdidos.forms import *
from AppDocumentosPerdidos.models import *
from django.core.mail import send_mail
from django.contrib import messages


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
            messages.info(request, 'Los datos se han cargado con exito!')
        else:
            messages.info(request, 'Los datos no se han cargado con exito!')

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

    return redirect('LiteraturaBuscar')


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
            messages.info(request, 'Los datos se han actualizado con exito!')
            return redirect('LiteraturaBuscar')

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
        messages.info(request, 'Su mensaje se ha enviado con exito!')
        return redirect('DocumentosPerdidosMain')

    return render(request,'AppCoder/main.html',{})