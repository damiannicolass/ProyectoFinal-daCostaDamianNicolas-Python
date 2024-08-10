from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from users.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

# Create your views here.
#Login
def login_request(request):

    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return redirect('inicio')
        
        msg_login = "Usuario o contraseña incorrectos"
    
    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})

#Registro
def register(request):
    
    msg_register = ""
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        
        msg_register = "Error en los datos ingresados"
    
    form = UserRegisterForm()
    return render(request,"users/registro.html", {"form":form, "msg_register": msg_register})


@login_required #Solo lo ven usuarios logueados
#Editar Perfil
def editar_perfil(request):
    usuario = request.user
    
    if request.method == "POST":
        mi_formulario = UserEditForm(request.POST, instance=usuario)
        if mi_formulario.is_valid():
            mi_formulario.save()
            return redirect('inicio')
    else:
        mi_formulario = UserEditForm(instance=usuario)
    
    return render(request, "users/editarPerfil.html", {"form": mi_formulario})

#Cambiar contraseña
class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/editarPass.html"
    success_url = reverse_lazy("editarPerfil")