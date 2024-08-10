from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Empleado
class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

#Asegurado
class Asegurado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()
    telefono = models.CharField(max_length=18, blank=True, null=True)  
    mail = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} ({self.dni})'  

#Vehiculo
class Vehiculo(models.Model):
    TIPO_CHOICES = [
        ('auto', 'Auto'),
        ('moto', 'Moto'),
        ('camion', 'Camión'),
    ]
    
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='auto')
    dominio = models.CharField(max_length=7)
    anio = models.IntegerField()
    marca = models.CharField(max_length=30, blank=True, null=True)
    version = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.get_tipo_display()} {self.dominio} - {self.marca} {self.version} ({self.anio})'


#Compañias
class Compania(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre


#Polizas
class Poliza(models.Model):
    TIPO_SEGURO_CHOICES = [
        ('moto', 'Moto'),
        ('auto', 'Auto'),
        ('bici', 'Bicicleta'),
        ('camion', 'Camión'),
        ('combinado_familiar', 'Combinado Familiar'),
        ('otros', 'Otros'),
    ]

    ESTADO_POLIZA_CHOICES = [
        ('vigente', 'Vigente'),
        ('anulada', 'Anulada'),
        ('vencida', 'Vencida'),
    ]

    numero_poliza = models.CharField(max_length=20)
    tipo_seguro = models.CharField(max_length=20, choices=TIPO_SEGURO_CHOICES)
    ramo_otros = models.CharField(max_length=50, blank=True, null=True)
    asegurado = models.ForeignKey(Asegurado, on_delete=models.CASCADE)
    compania = models.ForeignKey(Compania, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    estado_poliza = models.CharField(max_length=20, choices=ESTADO_POLIZA_CHOICES, default='vigente')
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, blank=True, null=True)
    informacion_adicional = models.TextField(blank=True, null=True)

# Tareas
class Tarea(models.Model):
    ESTADO_CHOICES = [
        ('activa', 'Activa'),
        ('terminada', 'Terminada'),
    ]

    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=5000, blank=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='activa') 
    created_at = models.DateTimeField(auto_now_add=True)

# Comentarios de tarea
class Comentario(models.Model):
    tarea = models.ForeignKey(Tarea, related_name='comentarios', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, related_name='comentarios_tareas', on_delete=models.CASCADE) 
    texto = models.CharField(max_length=2000)
    creado_en = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.usuario.username}: {self.texto[:50]}...'

# Siniestro
class Siniestro(models.Model):
    ESTADO_CHOICES = [
        ('activa', 'Activa'),
        ('terminada', 'Terminada'),
    ]
    
    numero_siniestro = models.CharField(max_length=30)
    asegurado = models.ForeignKey(Asegurado, on_delete=models.PROTECT)
    informacion = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='activa')

# Comentarios de siniestros
class ComentarioSiniestro(models.Model):
    siniestro = models.ForeignKey(Siniestro, related_name='comentarios', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, related_name='comentarios_siniestros', on_delete=models.CASCADE) 
    texto = models.CharField(max_length=2000)
    creado_en = models.DateTimeField(auto_now_add=True)