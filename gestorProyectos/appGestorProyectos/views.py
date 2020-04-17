from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .forms import ProyectoForm, TareaForm, EmpleadoForm

#PROYECTOS
def show_proyecto_form(request):
    form = ProyectoForm()
    return render(request, 'proyecto_form.html', {'form': form})


def post_proyecto_form(request):
    form = ProyectoForm(request.POST)
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        return HttpResponse(f"El nombre del proyecto es:  {nombre}")

#TAREAS
def show_tarea_form(request):
    form = TareaForm()
    return render(request, 'tarea_form.html', {'form': form})


def post_tarea_form(request):
    form = TareaForm(request.POST)
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        return HttpResponse(f"El nombre de la tarea es:  {nombre}")

#EMPLEADOS
def show_empleado_form(request):
    form = EmpleadoForm()
    return render(request, 'empleado_form.html', {'form': form})


def post_empleado_form(request):
    form = EmpleadoForm(request.POST)
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        return HttpResponse(f"El nombre del empleado es:  {nombre}")
