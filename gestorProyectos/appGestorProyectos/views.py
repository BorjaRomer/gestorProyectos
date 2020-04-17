from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .forms import ProyectoForm, TareaForm, EmpleadoForm

#PROYECTOS
from .models import Empleado, Proyecto, Tarea


class CrearProyectoView(View):

    def get(self, request, *args, **kwargs):
        form = ProyectoForm
        context = {
            'form': form,
            'titulo_pagina': 'Crear un nuevo proyecto'
        }
        return render(request, 'proyecto_form.html', context)


class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = 'proyecto.html'

    def get_context_data(self, **kwargs):
        context = super(ProyectoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del proyecto'
        return context

def post_proyecto_form(request):
    form = ProyectoForm(request.POST)
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        return HttpResponse(f"El nombre del proyecto es:  {nombre}")

#TAREAS
class CrearTareaView(View):

    def get(self, request, *args, **kwargs):
        form = TareaForm
        context = {
            'form': form,
            'titulo_pagina': 'Crear una nueva tarea'
        }
        return render(request, 'tarea_form.html', context)

class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tarea.html'

    def get_context_data(self, **kwargs):
        context = super(TareaDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles de la tarea'
        return context

def post_tarea_form(request):
    form = TareaForm(request.POST)
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        return HttpResponse(f"El nombre de la tarea es:  {nombre}")

#EMPLEADOS
class CrearEmpleadoView(View):

    def get(self, request, *args, **kwargs):
        form = EmpleadoForm
        context = {
            'form': form,
            'titulo_pagina': 'Crear un nuevo empleado'
        }
        return render(request, 'empleado_form.html', context)

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalle del empleado'
        return context


def post_empleado_form(request):
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            return HttpResponse(f"El nombre del empleado es:  {nombre}")
