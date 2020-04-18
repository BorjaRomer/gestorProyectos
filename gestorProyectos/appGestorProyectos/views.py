from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .forms import ProyectoForm, TareaForm, EmpleadoForm
from .models import Empleado, Proyecto, Tarea


# HOME
class ProyectosListView(ListView):
    model = Proyecto
    template_name = 'home.html'
    queryset = Proyecto.objects.order_by('nombre')
    context_object_name = 'listado_proyectos'

    def get_context_data(self, **kwargs):
        context = super(ProyectosListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'TUS PROYECTOS'
        return context


# PROYECTOS
class CrearProyectoView(View):

    def get(self, request, *args, **kwargs):
        form = ProyectoForm
        context = {
            'form': form,
            'titulo_pagina': 'Crear un nuevo proyecto'
        }
        return render(request, 'proyecto_form.html', context)

    def post(self, request, *args, **kwargs):
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            # Volvemos a la lista de proyectos
            return redirect('proyecto_list')

        return render(request, 'proyecto_form.html', {'form': form})


class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = 'proyecto.html'

    def get_context_data(self, **kwargs):
        context = super(ProyectoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del proyecto'
        return context


class ProyectoListView(ListView):
    model = Proyecto
    queryset = Proyecto.objects.order_by('nombre')
    template_name = "proyecto_list.html"

    def get_context_data(self, **kwargs):
        context = super(ProyectoListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de proyectos'
        return context


class ProyectoDeleteView(DeleteView):
    model = Proyecto
    template_name = "proyecto_delete.html"
    success_url = reverse_lazy('proyecto_list')


class ProyectoUpdateView(UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = "proyecto_update.html"
    success_url = reverse_lazy('proyecto_list')


# TAREAS
class CrearTareaView(View):

    def get(self, request, *args, **kwargs):
        form = TareaForm
        context = {
            'form': form,
            'titulo_pagina': 'Crear una nueva tarea'
        }
        return render(request, 'tarea_form.html', context)

    def post(self, request, *args, **kwargs):
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            # Volvemos a la lista de tareas
            return redirect('tarea_list')

        return render(request, 'tarea_form.html', {'form': form})


class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tarea.html'

    def get_context_data(self, **kwargs):
        context = super(TareaDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles de la tarea'
        return context


class TareaListView(ListView):
    model = Tarea
    queryset = Tarea.objects.order_by('nombre')
    template_name = "tarea_list.html"

    def get_context_data(self, **kwargs):
        context = super(TareaListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de tareas'
        return context


class TareaDeleteView(DeleteView):
    model = Tarea
    template_name = "tarea_delete.html"
    success_url = reverse_lazy('tarea_list')


class TareaUpdateView(UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = "tarea_update.html"
    success_url = reverse_lazy('tarea_list')


# EMPLEADOS
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
            return redirect('empleado_list')

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


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleado_delete.html"
    success_url = reverse_lazy('empleado_list')


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = "empleado_update.html"
    success_url = reverse_lazy('empleado_list')
