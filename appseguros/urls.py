from django.urls import path
from appseguros.views import * 


#path Inicio
urlpatterns = [
    path('', inicio, name="inicio"),
    path('about/', about, name="about"),
]

#Asegurados
asegurados = [
    path('listarAsegurados/', AseguradoListView.as_view(), name="listarAsegurados"),
    path('crearAsegurado/', AseguradoCreateView.as_view(), name="crearAsegurado"),
    path('actualizarAsegurado/<pk>/', AseguradoUpdateView.as_view(), name="actualizarAsegurado"),
    path('detalleAsegurado/<pk>/', AseguradoDetailView.as_view(), name="detalleAsegurado"),
    path('eliminarAsegurado/<pk>/', AseguradoDeleteView.as_view(), name="eliminarAsegurado"),
]

urlpatterns += asegurados


#Vehiculos
vehiculos = [
    path('listarVehiculos/', VehiculoListView.as_view(), name="listarVehiculos"),
    path('crearVehiculo/', VehiculoCreateView.as_view(), name="crearVehiculo"),
    path('actualizarVehiculo/<pk>/', VehiculoUpdateView.as_view(), name="actualizarVehiculo"),
    path('detalleVehiculo/<pk>/', VehiculoDetailView.as_view(), name="detalleVehiculo"),
    path('eliminarVehiculo/<pk>/', VehiculoDeleteView.as_view(), name="eliminarVehiculo"),
]

urlpatterns += vehiculos


#Empleados
empleados = [
    path('listarEmpleados/', EmpleadoListView.as_view(), name="listarEmpleados"),
    path('crearEmpleado/', EmpleadoCreateView.as_view(), name="crearEmpleado"),
    path('actualizarEmpleado/<pk>/', EmpleadoUpdateView.as_view(), name="actualizarEmpleado"),
    path('eliminarEmpleado/<pk>/', EmpleadoDeleteView.as_view(), name="eliminarEmpleado"),
]

urlpatterns += empleados

#Tareas
tareas = [
    path('listarTareas/', TareaListView.as_view(), name="listarTareas"),
    path('tarea/<int:pk>/actualizar_estado/', actualizar_estado_tarea, name='actualizar_estado_tarea'),
    path('crearTarea/', TareaCreateView.as_view(), name="crearTarea"),
    path('actualizarTarea/<pk>/', TareaUpdateView.as_view(), name="actualizarTarea"),
    path('eliminarTarea/<pk>/', TareaDeleteView.as_view(), name="eliminarTarea"),
    path('detalleTarea/<pk>/', TareaDetailView.as_view(), name="detalleTarea"),
]

urlpatterns += tareas

# Siniestros
siniestros = [
    path('listarSiniestros/', SiniestroListView.as_view(), name="listarSiniestros"),
    path('siniestro/<int:pk>/actualizar_estado/', actualizar_estado_siniestro, name='actualizar_estado_siniestro'),
    path('crearSiniestro/', SiniestroCreateView.as_view(), name="crearSiniestro"),
    path('actualizarSiniestro/<pk>/', SiniestroUpdateView.as_view(), name="actualizarSiniestro"),
    path('eliminarSiniestro/<pk>/', SiniestroDeleteView.as_view(), name="eliminarSiniestro"),
    path('detalleSiniestro/<pk>/', SiniestroDetailView.as_view(), name="detalleSiniestro"),
]

urlpatterns += siniestros


#polizas
polizas = [
    path('listarPolizas/', PolizaListView.as_view(), name="listarPolizas"),
    path('poliza/actualizar_estado/<int:pk>/', actualizar_estado_poliza, name='actualizar_estado_poliza'),
    path('crearPoliza/', PolizaCreateView.as_view(), name="crearPoliza"),
    path('actualizarPoliza/<pk>/', PolizaUpdateView.as_view(), name="actualizarPoliza"),
    path('detallePoliza/<pk>/', PolizaDetailView.as_view(), name="detallePoliza"),
    path('eliminarPoliza/<pk>/', PolizaDeleteView.as_view(), name="eliminarPoliza"),
]

urlpatterns += polizas

