from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

#Formulario para registrarse
class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_text = {k: "" for k in fields}

#formulario de editar usuario
class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Ingresa tu mail")
    last_name = forms.CharField(label="Apellido", required=False)
    first_name = forms.CharField(label="Nombre", required=False)
    #imagen = forms.ImageField(required=False) #Agrego pero no es requerido para el funcionamiento de mi pagina
    
    class Meta:
        model = User
        fields = ["email", "last_name", "first_name"]
