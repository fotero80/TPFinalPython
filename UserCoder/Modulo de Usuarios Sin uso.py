#--------------------------------------------------------------------------------------------------------
#Modulos de Usuarios
@user_passes_test(lambda u: u.is_superuser)
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
    return render(request, 'UserCoder/usuario.html', contexto)

@user_passes_test(lambda u: u.is_superuser)
def usuario_buscar(request):
    a_buscar = []
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
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
    return render(request, 'UserCoder/usuariobuscar.html', contexto)

@user_passes_test(lambda u: u.is_superuser)
def usuario_eliminar(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario=id_usuario)
    usuario.delete()

    return redirect('TPFinalUsuariosBuscar')

@user_passes_test(lambda u: u.is_superuser)
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

    return render(request, 'UserCoder/usuariomodificar.html', contexto)