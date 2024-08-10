from django.db import models
import uuid

# Create your models here.

#Modelo de la inspeccion
class Inspeccion(models.Model):
    asegurado = models.CharField(max_length=100)  # Nombre o identificador del asegurado
    dominio = models.CharField(max_length=100)  # Patente del vehículo
    foto_frente = models.URLField(blank=True, null=True)
    foto_trasera = models.URLField(blank=True, null=True)
    foto_lateral_derecho = models.URLField(blank=True, null=True)
    foto_lateral_izquierdo = models.URLField(blank=True, null=True)
    dni_frente = models.URLField(blank=True, null=True)
    dni_dorso = models.URLField(blank=True, null=True)
    cedula_verde_frente = models.URLField(blank=True, null=True)
    cedula_verde_dorso = models.URLField(blank=True, null=True)
    enlace_unico = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    fotos_subidas = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.asegurado} - {self.dominio}"