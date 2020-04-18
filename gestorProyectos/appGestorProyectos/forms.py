from django import forms
from django.forms import ModelForm
from .models import Proyecto, Tarea, Empleado


class DateInput(forms.DateInput):
    input_type = 'date'


class ProyectoForm(ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'
        widgets = {
            'fecha_inicio': DateInput(),
            'fecha_fin': DateInput()
        }


class TareaForm(ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'
        widgets = {
            'fecha_inicio': DateInput(),
            'fecha_fin': DateInput()
        }


class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
        }
