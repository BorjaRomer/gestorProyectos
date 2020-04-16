from django import forms

from . models import Proyecto


class DateInput(forms.DateInput):
    input_type = 'date'


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'
        widgets = {
            'fecha_inicio': DateInput(),
            'fecha_fin': DateInput()
        }
