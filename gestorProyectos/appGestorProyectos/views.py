from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .forms import ProyectoForm


def show_proyecto_form(request):
    form = ProyectoForm()
    return render(request, 'proyecto_form.html', {'form': form})


def post_proyecto_form(request):
    form = ProyectoForm(request.POST)
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        return HttpResponse(f"El nombre del proyecto es:  {nombre}")
