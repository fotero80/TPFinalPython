from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Mensajes.forms import Mensajes_Form, Buscar_Mensajes_Form
from Mensajes.models import Mensajes
from django.contrib import messages


@login_required()
def mensaje_crear(request, username):
    mensaje = Mensajes_Form(request.POST)
    usernameOrigen = request.user.username
    if request.method == 'POST':
        if mensaje.is_valid():
            mensaje = Mensajes(
                usuario_origen=usernameOrigen,
                usuario_destino=username,
                mensaje=request.POST.get('mensaje'),
            )
            mensaje.save()
            messages.info(request, 'El mensaje se ha enviado con exito!')
        else:
            messages.info(request, 'El mensaje no se ha enviado con exito!')

    contexto = {
        'formularioenviarmensaje': Mensajes_Form(),
        'usuariodestino': username,
    }
    return render(request, 'Mensajes/mensajeenviar.html', contexto)

@login_required()
def mensaje_buscar_ver(request):
    a_buscar = []
    if request.method == 'POST':
        usuarioLogueado = request.user.username
        usuarioorigen = request.POST.get('usuario_origen')
        usuariodestino= request.POST.get('usuario_destino')
        mensaje = request.POST.get('mensaje')

        a_buscar = (Mensajes.objects.filter(usuario_origen=usuarioLogueado) | \
                   Mensajes.objects.filter(usuario_destino=usuarioLogueado)) & \
                   Mensajes.objects.filter(mensaje__icontains=mensaje) & \
                   Mensajes.objects.filter(usuario_origen__icontains=usuarioorigen) & \
                   Mensajes.objects.filter(usuario_destino__icontains=usuariodestino)

    contexto = {
        'buscar_mensaje': Buscar_Mensajes_Form(),
        'mensaje': a_buscar,
    }
    return render(request, 'Mensajes/mensajebuscarver.html', contexto)

@login_required()
def mensaje_ver(request, id_mensaje):
    mensaje = Mensajes.objects.get(id_mensaje=id_mensaje)
    mensaje_form = Mensajes_Form(initial={
        'usuario_origen': mensaje.usuario_origen,
        'usuario_destino': mensaje.usuario_destino,
        'mensaje': mensaje.mensaje,
        'fecha_creacion_mensaje': mensaje.fecha_creacion_mensaje,
    }
    )
    contexto = {
        'formulariomostrarmensaje': mensaje_form,
        'mensaje': mensaje,
    }

    return render(request, 'Mensajes/mensajever.html', contexto)
