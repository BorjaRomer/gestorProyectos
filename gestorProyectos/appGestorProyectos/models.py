from django.db import models


class Empleado(models.Model):
    dni = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    telefono = models.IntegerField(default=0)


class Tarea(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    fecha_inicio_fin = models.DateField()
    responsable = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    nivel_prioridad = models.IntegerField(default=0)
    # https://docs.djangoproject.com/en/3.0/ref/models/fields/
    estado_tarea_choices = (
        ('abierta', 'abierta'),
        ('asignada', 'asignada'),
        ('en proceso', 'en proceso'),
        ('finalizada', 'finalizada'),
    )
    estado_tarea = models.CharField(choices=estado_tarea_choices, max_length=50)


class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.IntegerField(default=0)
    cliente = models.CharField(max_length=50)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    empleado = models.ManyToManyField(Empleado)
