from django import forms
from .models import *

#Formulario Empleado
class EmpleadoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)

#Formulario Asegurado
class AseguradoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=3000)
    dni = forms.IntegerField()
    telefono = models.CharField(max_length=18, blank=True, null=True)  
    mail = models.EmailField(blank=True, null=True)

#Formulario vehiculos
class VehiculoFormulario(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['dominio', 'anio', 'marca', 'version', 'tipo']

#Formulario Tarea
class TareaFormulario(forms.Form):
    ESTADO_CHOICES = [
        ('activa', 'Activa'),
        ('terminada', 'Terminada'),
    ]
    
    titulo = forms.CharField(max_length=30)
    subtitulo = forms.CharField(max_length=3000)
    estado = forms.ChoiceField(choices=ESTADO_CHOICES, initial='activa')

#Formularios de los comentarios de cada tarea
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']


# Formulario para crear o actualizar un Siniestro
class SiniestroFormulario(forms.ModelForm):
    ESTADO_CHOICES = [
        ('activa', 'Activa'),
        ('terminada', 'Terminada'),
    ]
    
    estado = forms.ChoiceField(choices=ESTADO_CHOICES, initial='activa')

    class Meta:
        model = Siniestro
        fields = ['numero_siniestro', 'asegurado', 'informacion', 'estado']

# Formulario para comentarios en un Siniestro
class ComentarioSiniestroForm(forms.ModelForm):
    class Meta:
        model = ComentarioSiniestro
        fields = ['texto']


# Polizas
class PolizaFormulario(forms.ModelForm):
    class Meta:
        model = Poliza
        fields = ['numero_poliza', 'tipo_seguro', 'ramo_otros', 'asegurado', 'compania', 'fecha_inicio', 'fecha_finalizacion', 'vehiculo', 'informacion_adicional']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_finalizacion': forms.DateInput(attrs={'type': 'date'}),
        }
