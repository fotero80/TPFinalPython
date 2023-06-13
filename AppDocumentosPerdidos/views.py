from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from AppDocumentosPerdidos.forms import *
from AppDocumentosPerdidos.models import *
from django.core.mail import send_mail
from django.contrib import messages


def Main(request):
    return render(request, 'AppCoder/main.html')


# --------------------------------------------------------------------------------------------------------
# Modulos de documento
@login_required()
def documento_crear(request):
    lit = documento_Form(request.POST or None, request.FILES or None)
    username = None
    username = request.user.username
    if request.method == 'POST':
        if lit.is_valid():
            lit = documento(
                nombre_documento=request.POST.get('nombre_documento'),
                autor_documento=request.POST.get('autor_documento'),
                editorial_documento=request.POST.get('editorial_documento'),
                descripcion_documento=request.POST.get('descripcion_documento'),
                username_documento=username,
            )
            lit.save()
            if 'imglit' in request.FILES:
                imagen = request.FILES["imglit"]
                img = Imagendocumento(id_documento=lit, imglit=imagen)
                img.save()
            messages.info(request, 'Los datos se han cargado con exito!')
        else:
            messages.info(request, 'Los datos no se han cargado con exito!')

    contexto = {
        'formulariocargardocumento': documento_Form(),
    }
    return render(request, 'AppCoder/documento/documento.html', contexto)


@login_required()
def documento_buscar(request):
    username = None
    username = request.user.username
    a_buscar = []
    if request.method == 'POST':
        nombre_documento = request.POST.get('nombre_documento')
        autor_documento = request.POST.get('autor_documento')
        editorial_documento = request.POST.get('editorial_documento')
        descripcion_documento = request.POST.get('descripcion_documento')
        if request.user.is_superuser:
            a_buscar = documento.objects.filter(nombre_documento__icontains=nombre_documento) & \
                       documento.objects.filter(autor_documento__icontains=autor_documento) & \
                       documento.objects.filter(editorial_documento__icontains=editorial_documento) & \
                       documento.objects.filter(descripcion_documento__icontains=descripcion_documento)
        else:
            a_buscar = documento.objects.filter(nombre_documento__icontains=nombre_documento) & \
                       documento.objects.filter(autor_documento__icontains=autor_documento) & \
                       documento.objects.filter(editorial_documento__icontains=editorial_documento) & \
                       documento.objects.filter(descripcion_documento__icontains=descripcion_documento) & \
                       documento.objects.filter(username_documento=username)

    contexto = {
        'buscar_documento': Buscar_documento_Form(),
        'documento': a_buscar
    }
    return render(request, 'AppCoder/documento/DocumentoBuscar.html', contexto)


def documento_buscar_ver(request):
    a_buscar = []
    if request.method == 'POST':
        nombre_documento = request.POST.get('nombre_documento')
        autor_documento = request.POST.get('autor_documento')
        editorial_documento = request.POST.get('editorial_documento')
        descripcion_documento = request.POST.get('descripcion_documento')
        a_buscar = documento.objects.filter(nombre_documento__icontains=nombre_documento) & \
                    documento.objects.filter(autor_documento__icontains=autor_documento) & \
                    documento.objects.filter(editorial_documento__icontains=editorial_documento) & \
                    documento.objects.filter(descripcion_documento__icontains=descripcion_documento)

    contexto = {
        'buscar_documento': Buscar_documento_Form(),
        'documento': a_buscar
    }
    return render(request, 'AppCoder/documento/DocumentoBuscarVer.html', contexto)

@login_required()
def documento_eliminar(request, id_documento):
    lit = documento.objects.get(id_documento=id_documento)
    lit.delete()

    return redirect('DocumentoBuscar')


@login_required()
def documento_modificar(request, id_documento):
    lit = documento.objects.get(id_documento=id_documento)
    if request.method == 'POST':
        Lite = documento_Form(request.POST)
        if Lite.is_valid():
            data = Lite.cleaned_data
            lit.nombre_documento = data.get('nombre_documento')
            lit.autor_documento = data.get('autor_documento')
            lit.editorial_documento = data.get('editorial_documento')
            lit.descripcion_documento = data.get('descripcion_documento')
            lit.save()

            img = Imagendocumento.objects.filter(id_documento=lit)
            if 'imglit' in request.FILES:
                imagen = request.FILES["imglit"]
                if img.exists():
                    if imagen:
                        img = img[0]
                        img.imglit = imagen
                        img.save()

                else:
                    img = Imagendocumento(id_documento=lit, imglit=imagen)
                    img.save()
            messages.info(request, 'Los datos se han actualizado con exito!')
            return redirect('DocumentoBuscar')

    documento_form = documento_Form(initial={
        'nombre_documento': lit.nombre_documento,
        'autor_documento': lit.autor_documento,
        'editorial_documento': lit.editorial_documento,
        'descripcion_documento': lit.descripcion_documento,
        'username_documento': lit.username_documento
    }
    )
    contexto = {
        'formulariocargardocumento': documento_form,
        'documento': lit,
    }

    return render(request, 'AppCoder/documento/DocumentoModificar.html', contexto)

def documento_ver(request, id_documento):
    lit = documento.objects.get(id_documento=id_documento)
    documento_form = documento_Form(initial={
        'nombre_documento': lit.nombre_documento,
        'autor_documento': lit.autor_documento,
        'editorial_documento': lit.editorial_documento,
        'descripcion_documento': lit.descripcion_documento,
    }
    )
    contexto = {
        'formulariocargardocumento': documento_form,
        'documento': lit,
    }

    return render(request, 'AppCoder/documento/DocumentoVer.html', contexto)

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