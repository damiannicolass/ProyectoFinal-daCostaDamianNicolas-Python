from django.urls import path
from django.contrib.auth.views import LogoutView
from users import views

urlpatterns = [
    path('login/', views.login_request, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('editarPerfil/', views.editar_perfil, name="editarPerfil"),
    path("cambiarContrasenia", views.CambiarContrasenia.as_view(), name="cambiarContrasenia"),
]