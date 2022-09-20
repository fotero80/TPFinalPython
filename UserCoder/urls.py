from django.contrib.auth.views import LogoutView
from django.urls import path
from django.contrib.auth import views as auth_views

from UserCoder.views import *

urlpatterns = [
    path('Login/', user_login, name='UserCoderLogin'),
    path('Logon/', user_logon, name='UserCoderLogon'),
    path('Logout/', LogoutView.as_view(template_name='UserCoder/logout.html'), name='UserCoderLogOut'),
    path('Usuario/Crear/', user_logon, name='TPFinalUsuariosCrear'),
    path('Usuario/Buscar/', usuario_buscar, name='TPFinalUsuariosBuscar'),
    path('Usuario/Eliminar/<str:username>', usuario_eliminar, name='TPFinalUsuariosEliminar'),
    path('Usuario/Modificar/<str:username>', usuario_modificar, name='TPFinalUsuariosModificar'),
    path('Usuario/CambiarPass/', ChangePasswordView.as_view(), name='TPFinalUsuariosModificarPass'),
# Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='UserCoder/password_reset.html',
             subject_template_name='UserCoder/password_reset_subject.txt',
             email_template_name='UserCoder/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='UserCoder/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='UserCoder/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='UserCoder/password_reset_complete.html'
         ),
         name='password_reset_complete'),

]

