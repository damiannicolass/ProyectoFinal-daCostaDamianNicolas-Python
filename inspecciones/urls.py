from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('lista_inspecciones/', lista_inspecciones, name='lista_inspecciones'),
    path('crear_inspeccion/', CrearInspeccionView.as_view(), name='crear_inspeccion'),
    path('subir-fotos/<int:pk>/', SubirFotosView.as_view(), name='subir_fotos'),
    path('enlace-inspeccion/<uuid:enlace>/', EnlaceInspeccionView.as_view(), name='enlace_inspeccion'),
    path('exito/', TemplateView.as_view(template_name='inspecciones/exito.html'), name='exito'),
    path('eliminar_inspeccion/<pk>/', InspeccionDeleteView.as_view(), name="eliminar_inspeccion"),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)