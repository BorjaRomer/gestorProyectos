from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class ProyectoForm(forms.Form):
    nombre = forms.CharField(label="Nombre del proyecto", max_length=100)
    descripcion = forms.CharField(label="Descripción del proyecto", max_length=300)
    fecha_inicio = forms.DateField(widget=DateInput)
    fecha_fin = forms.DateField(widget=DateInput)
    presupuesto = forms.IntegerField(label="Presupuesto del proyecto")
    nombre_cliente = forms.CharField(label="Nombre del cliente", max_length=40)
    apellidos_cliente = forms.CharField(label="Apellidos del cliente", max_length=100)
    email_cliente = forms.EmailField(label="Email del cliente")
    telefono_cliente = forms.IntegerField(label="Teléfono del cliente")
