from django.urls import path
from . import views

urlpatterns = [
    path('nuevo_proyecto/', views.CrearProyectoView.as_view(), name='proyecto_form'),
    path('proyecto/', views.post_proyecto_form, name='post_proyecto_form'),
    path('nueva_tarea/', views.CrearTareaView.as_view(), name='tarea_form'),
    path('tarea/', views.post_tarea_form, name="post_tarea_form"),
    path('nuevo_empleado/', views.CrearEmpleadoView.as_view(), name='empleado_form'),
    path('empleado/', views.post_empleado_form, name='post_empleado_form')
]
