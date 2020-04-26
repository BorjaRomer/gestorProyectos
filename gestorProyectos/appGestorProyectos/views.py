from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .forms import ProyectoForm, TareaForm, EmpleadoForm
from .models import Empleado, Proyecto, Tarea
from django.contrib.auth.mixins import LoginRequiredMixin


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


# CLIENTE
class ClienteDetailView(DetailView):
    model = Proyecto
    template_name = 'cliente.html'

    def get_context_data(self, **kwargs):
        context = super(ClienteDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del cliente'
        return context


# PROYECTOS
class ProyectoCreateView(LoginRequiredMixin, CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'proyecto_form.html'

    def get_success_url(self):
        return reverse('proyecto_list')


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
    template_name = "proyecto_list2.html"

    def get_context_data(self, **kwargs):
        context = super(ProyectoListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de proyectos'
        return context


class ProyectoDeleteView(LoginRequiredMixin, DeleteView):
    model = Proyecto
    template_name = "proyecto_delete.html"
    success_url = reverse_lazy('proyecto_list')


class ProyectoUpdateView(LoginRequiredMixin, UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = "proyecto_update.html"
    success_url = reverse_lazy('proyecto_list')


# TAREAS
class TareaCreateView(LoginRequiredMixin, CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tarea_form.html'

    def get_success_url(self):
        return reverse('tarea_list')


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
    template_name = "tarea_list2.html"

    def get_context_data(self, **kwargs):
        context = super(TareaListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de tareas'
        return context


class TareaDeleteView(LoginRequiredMixin, DeleteView):
    model = Tarea
    template_name = "tarea_delete.html"
    success_url = reverse_lazy('tarea_list')


class TareaUpdateView(LoginRequiredMixin, UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = "tarea_update.html"
    success_url = reverse_lazy('tarea_list')


# EMPLEADOS
class EmpleadoCreateView(LoginRequiredMixin, CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado_form.html'

    def get_success_url(self):
        return reverse('empleado_list')


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
    template_name = "empleado_list2.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de empleados'
        return context


class EmpleadoDeleteView(LoginRequiredMixin, DeleteView):
    model = Empleado
    template_name = "empleado_delete.html"
    success_url = reverse_lazy('empleado_list')


class EmpleadoUpdateView(LoginRequiredMixin, UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = "empleado_update.html"
    success_url = reverse_lazy('empleado_list')
