from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, TemplateView, DetailView, View, DeleteView
from .models import Inspeccion
from .forms import *
from django.urls import reverse_lazy, reverse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

#Creo una inspeccion nueva
class CrearInspeccionView(LoginRequiredMixin,CreateView):
    model = Inspeccion
    form_class = InspeccionForm
    template_name = 'inspecciones/crear_inspeccion.html'
    success_url = reverse_lazy('lista_inspecciones')

    def form_valid(self, form):
        response = super().form_valid(form)
        enlace_unico = self.object.enlace_unico
        # Redirige a la vista que muestra el enlace
        return redirect('enlace_inspeccion', enlace=enlace_unico)


#Me lleva a otro url para crear el enlace para enviar al asegurado
class EnlaceInspeccionView(LoginRequiredMixin,TemplateView):
    template_name = 'inspecciones/enlace_inspeccion.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        enlace_unico = kwargs['enlace']
        context['enlace'] = self.request.build_absolute_uri(reverse('subir_fotos', kwargs={'pk': Inspeccion.objects.get(enlace_unico=enlace_unico).pk}))
        return context


#Logica para la parte de subir las fotos 
#Como hago para que solamente ese usuario pueda entrar a ese link y no me manipule la url para entrar a otra inspeccion? 
#No pude hacerlo funcionar con drive/no se si se puede  
class SubirFotosView(View):
    template_name = 'inspecciones/subir_fotos.html'

    def get(self, request, *args, **kwargs):
        inspeccion = get_object_or_404(Inspeccion, pk=self.kwargs['pk'])
        if inspeccion.fotos_subidas:
            return HttpResponseForbidden("Las fotos ya han sido subidas.") #Verifica si las fotos ya se subieron
        
        user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
        if 'mobile' not in user_agent and 'android' not in user_agent and 'iphone' not in user_agent:
            return HttpResponseForbidden("Acceso no permitido. Solo desde dispositivos móviles.") #verifico si se abrio en un celular
        
        form = FotoForm(instance=inspeccion)
        return render(request, self.template_name, {'form': form, 'inspeccion': inspeccion}) #sino devolvemos el formulario

    def post(self, request, *args, **kwargs): #mandamos las fotos
        inspeccion = get_object_or_404(Inspeccion, pk=self.kwargs['pk'])
        if inspeccion.fotos_subidas:
            return HttpResponseForbidden("Las fotos ya han sido subidas.")
        
        form = FotoForm(request.POST, request.FILES, instance=inspeccion)
        if form.is_valid():
            inspeccion = form.save(commit=False)
            fotos = {
                'foto_frente': request.FILES.get('foto_frente'),
                'foto_trasera': request.FILES.get('foto_trasera'),
                'foto_lateral_derecho': request.FILES.get('foto_lateral_derecho'),
                'foto_lateral_izquierdo': request.FILES.get('foto_lateral_izquierdo'),
                'dni_frente': request.FILES.get('dni_frente'),
                'dni_dorso': request.FILES.get('dni_dorso'),
                'cedula_verde_frente': request.FILES.get('cedula_verde_frente'),
                'cedula_verde_dorso': request.FILES.get('cedula_verde_dorso'),
            }
            
            for nombre_foto, archivo in fotos.items():
                if archivo:
                    # Guardar el archivo en el almacenamiento
                    file_path = default_storage.save(archivo.name, ContentFile(archivo.read()))
                    # Crear la URL del archivo para almacenar en el modelo
                    foto_url = default_storage.url(file_path)
                    setattr(inspeccion, nombre_foto, foto_url)
            
            inspeccion.fotos_subidas = True
            inspeccion.save()
            return redirect('exito')  # Redirigir a una página de éxito
        return render(request, self.template_name, {'form': form, 'inspeccion': inspeccion})


#Listamos las inspecciones que creamos
@login_required
def lista_inspecciones(request):
    inspecciones = Inspeccion.objects.all()
    return render(request, 'inspecciones/lista_inspecciones.html', {'inspecciones': inspecciones})


#Eliminar un asegurado, solo el admin (el condicional esta en el html)
class InspeccionDeleteView(LoginRequiredMixin,DeleteView):
    model = Inspeccion
    template_name = "inspecciones/eliminar_inspeccion.html"
    success_url = reverse_lazy("lista_inspecciones")



