from django.urls import path
from . import views

urlpatterns = [
    path('nuevo_proyecto/', views.show_proyecto_form, name='proyecto_form'),
    path('proyecto/', views.post_proyecto_form, name='post_proyecto_form'),
    path('nueva_tarea/', views.show_tarea_form, name='tarea_form'),
    path('tarea/', views.post_tarea_form, name="post_tarea_form"),
    path('nuevo_empleado/', views.show_empleado_form, name='empleado_form'),
    path('empleado/', views.post_empleado_form, name='post_empleado_form')
]
