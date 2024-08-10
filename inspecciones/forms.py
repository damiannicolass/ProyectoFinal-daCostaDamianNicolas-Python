from django import forms
from .models import Inspeccion

class InspeccionForm(forms.ModelForm):
    class Meta:
        model = Inspeccion
        fields = ['asegurado', 'dominio']

class FotoForm(forms.ModelForm):
    class Meta:
        model = Inspeccion
        fields = [
            'foto_frente', 'foto_trasera', 'foto_lateral_derecho',
            'foto_lateral_izquierdo', 'dni_frente', 'dni_dorso',
            'cedula_verde_frente', 'cedula_verde_dorso'
        ]
        widgets = {
            'foto_frente': forms.FileInput(attrs={'accept': 'image/*'}),
            'foto_trasera': forms.FileInput(attrs={'accept': 'image/*'}),
            'foto_lateral_derecho': forms.FileInput(attrs={'accept': 'image/*'}),
            'foto_lateral_izquierdo': forms.FileInput(attrs={'accept': 'image/*'}),
            'dni_frente': forms.FileInput(attrs={'accept': 'image/*'}),
            'dni_dorso': forms.FileInput(attrs={'accept': 'image/*'}),
            'cedula_verde_frente': forms.FileInput(attrs={'accept': 'image/*'}),
            'cedula_verde_dorso': forms.FileInput(attrs={'accept': 'image/*'}),
        }
