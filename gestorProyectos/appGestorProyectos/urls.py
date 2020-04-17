from django.urls import path
from . import views

urlpatterns = [
    #HOME
    path('home/', views.ProyectosListView.as_view(), name='index'),
    #PROYECTOS
    path('nuevo_proyecto/', views.CrearProyectoView.as_view(), name='proyecto_form'),
    path('proyectos/', views.ProyectoListView.as_view(), name='proyectos'),
    path('proyecto/<int:pk>/', views.ProyectoDetailView.as_view(), name='proyecto'),
    #TAREAS
    path('nueva_tarea/', views.CrearTareaView.as_view(), name='tarea_form'),
    path('tareas/', views.TareaListView.as_view(), name='tareas'),
    path('tarea/<int:pk>/', views.TareaDetailView.as_view(), name='tarea'),
    #EMPLEADOS
    path('nuevo_empleado/', views.CrearEmpleadoView.as_view(), name='empleado_form'),
    path('empleados/', views.EmpleadoListView.as_view(), name='empleado_list'),
    path('empleado/<int:pk>/', views.EmpleadoDetailView.as_view(), name='empleado'),
]
