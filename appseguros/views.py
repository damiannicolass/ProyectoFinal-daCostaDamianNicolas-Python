from django.shortcuts import render, redirect
from appseguros.forms import *
from .models import *
from django.views.generic import ListView 
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView, UpdateView,  DeleteView
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from django.http import HttpResponseNotAllowed
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
#Inicio
@login_required #Para ver el inicio se requiere inicio de sesion
def inicio(request):
    cantidad_tareas_pendientes = Tarea.objects.filter(estado='activa').count()
    cantidad_siniestros_pendientes = Siniestro.objects.filter(estado='activa').count() 

    return render(request, "appseguros/inicio.html", {
        'cantidad_tareas_pendientes': cantidad_tareas_pendientes,
        'cantidad_siniestros_pendientes': cantidad_siniestros_pendientes
    })

#Para todas las vistas se requiere LoginRequiredMixin

#Asegurados----------------------------------------------
#Listar asegurados
class AseguradoListView(LoginRequiredMixin,ListView):
    model = Asegurado
    context_object_name = "asegurados"
    template_name = "appseguros/asegurado/listarAsegurados.html"
    
    #Buscar un asegurado por nombre o apellido
    def get_queryset(self):
        queryset = super().get_queryset()
        buscar = self.request.GET.get("buscar")
        if buscar:
            queryset = queryset.filter(Q(nombre__icontains=buscar) | Q(apellido__icontains=buscar))
        return queryset

#Crear asegurado
class AseguradoCreateView(LoginRequiredMixin,CreateView):
    model = Asegurado
    template_name = "appseguros/asegurado/crearAsegurado.html"
    success_url = reverse_lazy("listarAsegurados")
    fields = ["nombre", "apellido", "dni", "telefono", "mail"]

#Actualizar asegurado
class AseguradoUpdateView(LoginRequiredMixin,UpdateView):
    model = Asegurado
    template_name = "appseguros/asegurado/actualizarAsegurado.html"
    fields = ["nombre", "apellido", "dni", "telefono", "mail"]
    success_url = reverse_lazy("listarAsegurados")

#Detalle Asegurado
class AseguradoDetailView(LoginRequiredMixin,DetailView):
    model = Asegurado
    template_name = 'appseguros/asegurado/detalleAsegurado.html'

#Eliminar un asegurado, solo el admin (el condicional esta en el html)
class AseguradoDeleteView(LoginRequiredMixin,DeleteView):
    model = Asegurado
    template_name = "appseguros/asegurado/eliminarAsegurado.html"
    success_url = reverse_lazy("listarAsegurados")



#Vehiculos----------------------------------------------
#Listar Vehiculos
class VehiculoListView(LoginRequiredMixin,ListView):
    model = Vehiculo
    context_object_name = "vehiculos"
    template_name = "appseguros/vehiculo/listarVehiculos.html"
    
    #Buscar vehiculo por dominio
    def get_queryset(self):
        queryset = super().get_queryset()
        buscar = self.request.GET.get("buscar")
        if buscar:
            queryset = queryset.filter(dominio__icontains=buscar)
        return queryset

#Crear vehiculo
class VehiculoCreateView(LoginRequiredMixin,CreateView):
    model = Vehiculo
    template_name = "appseguros/vehiculo/crearVehiculo.html"
    success_url = reverse_lazy("listarVehiculos")
    fields = ["tipo", "dominio", "anio", "marca", "version"]

#Actualizar vehiculo
class VehiculoUpdateView(LoginRequiredMixin,UpdateView):
    model = Vehiculo
    template_name = "appseguros/vehiculo/actualizarVehiculo.html"
    fields = ["tipo", "dominio", "anio", "marca", "version"]
    success_url = reverse_lazy("listarVehiculos")

#Detalle vehiculo
class VehiculoDetailView(LoginRequiredMixin,DetailView):
    model = Vehiculo
    template_name = 'appseguros/vehiculo/detalleVehiculo.html'

#Borrar siniestro
class VehiculoDeleteView(LoginRequiredMixin,DeleteView):
    model = Vehiculo
    template_name = 'appseguros/vehiculo/eliminarvehiculo.html'
    success_url = reverse_lazy('listarVehiculo')





#Empleados--------------------------------------------------
#Listar empleados
class EmpleadoListView(LoginRequiredMixin,ListView):
    model = Empleado
    context_object_name = "empleados"
    template_name = "appseguros/empleado/listarEmpleados.html"

#Actualizar Empleados
class EmpleadoUpdateView(LoginRequiredMixin,UpdateView):
    model = Empleado
    template_name = "appseguros/empleado/actualizarEmpleado.html"
    fields = ["nombre", "apellido"]
    success_url = reverse_lazy("listarEmpleados")

#Crear empleado
class EmpleadoCreateView(LoginRequiredMixin,CreateView):
    model = Empleado
    template_name = "appseguros/empleado/crearEmpleado.html"
    success_url = reverse_lazy("listarEmpleados")
    fields = ["nombre", "apellido"]

#Eliminar un asegurado, solo el admin (el condicional esta en el html)
class EmpleadoDeleteView(LoginRequiredMixin,DeleteView):
    model = Empleado
    template_name = "appseguros/empleado/eliminarEmpleado.html"
    success_url = reverse_lazy("listarEmpleados")



#Tareas------------------------------------------------
#Listar Tareas
class TareaListView(LoginRequiredMixin,ListView):
    model = Tarea
    context_object_name = "tareas"
    template_name = "appseguros/tarea/listarTareas.html"
    
    #Buscar tarea por el titulo
    def get_queryset(self):
        queryset = super().get_queryset()
        buscar = self.request.GET.get("buscar")
        if buscar:
            queryset = queryset.filter(titulo__icontains=buscar)
        return queryset

#Cambiar el estado de la tarea, si esta "activa" o "terminada"
def actualizar_estado_tarea(request, pk):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    try:
        tarea = Tarea.objects.get(pk=pk)
    except Tarea.DoesNotExist:
        return redirect(reverse('listarTareas')) 

    nuevo_estado = request.POST.get('estado')

    if nuevo_estado and nuevo_estado != tarea.estado:
        tarea.estado = nuevo_estado
        tarea.save()

    return redirect(reverse('listarTareas'))

#Crear una tarea nueva
class TareaCreateView(LoginRequiredMixin,CreateView):
    model = Tarea
    template_name = "appseguros/tarea/crearTarea.html"
    success_url = reverse_lazy("listarTareas")
    fields = ["titulo", "subtitulo"]

#Actualizar una tarea
class TareaUpdateView(LoginRequiredMixin,UpdateView):
    model = Tarea
    template_name = "appseguros/tarea/actualizarTarea.html"
    fields = ["titulo", "subtitulo"]
    success_url = reverse_lazy("listarTareas")
    
#Eliminar una tarea, solo el admin (el condicional esta en el html)
class TareaDeleteView(LoginRequiredMixin,DeleteView):
    model = Tarea
    template_name = "appseguros/tarea/eliminarTarea.html"
    success_url = reverse_lazy("listarTareas")

#Detalle de la tarea
class TareaDetailView(LoginRequiredMixin,DetailView):
    model = Tarea
    template_name = "appseguros/tarea/detalleTarea.html"
    
    #Trae los comentarios que ya estan en detalle de tarea
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        if self.request.POST:
            contexto['formulario_comentario'] = ComentarioForm(self.request.POST)
        else:
            contexto['formulario_comentario'] = ComentarioForm()
        return contexto

    #Agrega nuevos comentarios
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        formulario = ComentarioForm(request.POST)
        if formulario.is_valid():
            comentario = formulario.save(commit=False)
            comentario.tarea = self.object
            comentario.usuario = request.user
            comentario.save()
            return redirect('detalleTarea', pk=self.object.pk)
        return self.get(request, *args, **kwargs)



# Siniestos --------------------------------------------
#Listamos Siniestros
class SiniestroListView(LoginRequiredMixin,ListView):
    model = Siniestro
    context_object_name = 'siniestros'
    template_name = 'appseguros/siniestro/listarSiniestros.html'
    
    #Buscamos Siniestros
    def get_queryset(self):
        queryset = super().get_queryset()
        buscar = self.request.GET.get("buscar")
        if buscar:
            queryset = queryset.filter(
                Q(asegurado__nombre__icontains=buscar) | Q(asegurado__apellido__icontains=buscar)
            )
        return queryset

#Actualizamos el esta del siniestro
def actualizar_estado_siniestro(request, pk):
    siniestro = Siniestro.objects.get(pk=pk)
    
    if request.method == 'POST':
        if siniestro.estado == 'activa':
            siniestro.estado = 'terminada'
        else:
            siniestro.estado = 'activa'
        siniestro.save()
    
    return redirect('listarSiniestros')


#Crear siniestro
class SiniestroCreateView(LoginRequiredMixin,CreateView):
    model = Siniestro
    form_class = SiniestroFormulario
    template_name = 'appseguros/siniestro/crearSiniestro.html'
    success_url = reverse_lazy('listarSiniestros')


#Actualizar siniestro
class SiniestroUpdateView(LoginRequiredMixin,UpdateView):
    model = Siniestro
    template_name = 'appseguros/siniestro/actualizarSiniestro.html'
    form_class = SiniestroFormulario
    success_url = reverse_lazy('listarSiniestros')

#Borrar siniestro
class SiniestroDeleteView(LoginRequiredMixin,DeleteView):
    model = Siniestro
    template_name = 'appseguros/siniestro/eliminarSiniestro.html'
    success_url = reverse_lazy('listarSiniestros')

class SiniestroDetailView(LoginRequiredMixin, DetailView):
    model = Siniestro
    template_name = 'appseguros/siniestro/detalleSiniestro.html'
    
    # Trae los comentarios si hay
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formulario_comentario'] = ComentarioSiniestroForm(self.request.POST)
        else:
            context['formulario_comentario'] = ComentarioSiniestroForm()
        return context
    
    # Agrego nuevos comentarios al siniestro
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        formulario = ComentarioSiniestroForm(request.POST)
        if formulario.is_valid():
            comentario = formulario.save(commit=False)
            comentario.siniestro = self.object
            comentario.usuario = request.user  #agrego el usuario autenticado al comentario
            comentario.save()
            return redirect('detalleSiniestro', pk=self.object.pk)
        return self.get(request, *args, **kwargs)



#Polizas-------------------------------------------------------
#listar polizas
class PolizaListView(LoginRequiredMixin,ListView):
    model = Poliza
    template_name = 'appseguros/poliza/listarPolizas.html'
    
    #Buscamos poliza por nombre o por apellido
    def get_queryset(self):
        queryset = super().get_queryset()
        buscar = self.request.GET.get("buscar")
        if buscar:
            queryset = queryset.filter(
                Q(asegurado__nombre__icontains=buscar) | 
                Q(asegurado__apellido__icontains=buscar)
            )
        return queryset

#actualizar estado de la poliza
def actualizar_estado_poliza(request, pk):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    try:
        poliza = Poliza.objects.get(pk=pk)
    except Poliza.DoesNotExist:
        return redirect(reverse('listarPolizas'))

    nuevo_estado = request.POST.get('estado')

    if nuevo_estado and nuevo_estado != poliza.estado_poliza:
        poliza.estado_poliza = nuevo_estado
        poliza.save()

    return redirect(reverse('listarPolizas'))

#Crear poliza
class PolizaCreateView(LoginRequiredMixin,CreateView):
    model = Poliza
    form_class = PolizaFormulario
    template_name = 'appseguros/poliza/crearPoliza.html'
    success_url = reverse_lazy('listarPolizas')

#actualizar poliza
class PolizaUpdateView(LoginRequiredMixin,UpdateView):
    model = Poliza
    form_class = PolizaFormulario
    template_name = 'appseguros/poliza/actualizarPoliza.html'
    success_url = reverse_lazy('listarPolizas')

#detalle poliza
class PolizaDetailView(LoginRequiredMixin,DetailView):
    model = Poliza
    template_name = 'appseguros/poliza/detallePoliza.html'

#Eliminar una poliza, solo el admin (el condicional esta en el html)
class PolizaDeleteView(LoginRequiredMixin,DeleteView):
    model = Poliza
    template_name = "appseguros/poliza/eliminarPoliza.html"
    success_url = reverse_lazy("listarPolizas")




def about(request):
    return render(request, 'appseguros/about.html')