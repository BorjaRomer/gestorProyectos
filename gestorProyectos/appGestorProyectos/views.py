from django.http import HttpResponse
from django.shortcuts import render, redirect
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



#EMPLEADOS
class CrearEmpleadoView(View):

    def get(self, request, *args, **kwargs):
        form = EmpleadoForm
        context = {
            'form': form,
            'titulo_pagina': 'Crear un nuevo empleado'
        }
        return render(request, 'empleado_form.html', context)

    def post(self, request, *args, **kwargs):
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            # Volvemos a la lista de empleados
            return redirect('empleado')

        return render(request, 'empleado_form.html', {'form': form})

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalle del empleado'
        return context

class EmpleadoListView(ListView):
    model = Empleado
    queryset = Empleado.objects.order_by('nombre')
    template_name = "empleado_list.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de empleados'
        return context

