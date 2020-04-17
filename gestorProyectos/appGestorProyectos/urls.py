from django.urls import path
from . import views

urlpatterns = [
    path('nuevo_proyecto/', views.CrearProyectoView.as_view(), name='proyecto_form'),
    path('proyectos/<int:pk>/', views.ProyectoDetailView.as_view(), name='proyecto'),
    path('nueva_tarea/', views.CrearTareaView.as_view(), name='tarea_form'),
    path('tareas/<int:pk>/', views.TareaDetailView.as_view(), name='tarea'),
    path('nuevo_empleado/', views.CrearEmpleadoView.as_view(), name='empleado_form'),
    path('empleados/', views.EmpleadoListView.as_view(), name='empleado'),
    path('empleados/<int:pk>/', views.EmpleadoDetailView.as_view(), name='empleado')
]
