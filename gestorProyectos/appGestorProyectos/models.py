from datetime import date
from django.db import models


class Empleado(models.Model):
    dni = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    telefono = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre}"


class Tarea(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    fecha_inicio = models.DateField(("Date"), default=date.today)
    fecha_fin = models.DateField(("Date"), default=date.today)
    responsable = models.ForeignKey(Empleado, on_delete=models.CASCADE, default="")
    nivel_prioridad = models.IntegerField(default=0)
    estado_tarea_choices = (
        ('', ''),
        ('abierta', 'abierta'),
        ('asignada', 'asignada'),
        ('en proceso', 'en proceso'),
        ('finalizada', 'finalizada'),
    )
    estado_tarea = models.CharField(choices=estado_tarea_choices, default='', max_length=20)

    def __str__(self):
        return f"{self.nombre}"


class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    fecha_inicio = models.DateField(("Date"), default=date.today)
    fecha_fin = models.DateField(("Date"), default=date.today)
    presupuesto = models.IntegerField(default=0)
    nombre_cliente = models.CharField(max_length=20, default="")
    apellidos_cliente = models.CharField(max_length=50, default="")
    email_cliente = models.EmailField(max_length=100, default="")
    telefono_cliente = models.IntegerField(default=0)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    responsable = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.id}"
