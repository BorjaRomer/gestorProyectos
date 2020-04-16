from django.db import models


# Aqui vamos a poner nuestro modelo de datos que esta en el Drive. Es un ejemplo de momento y habrá que extenderlo.
# Voy a poner los atributos que vienen en el pdf del reto.
# Hay que darle una vuelta todavia o preguntarle a el porque no estoy seguro.
# Aun no he creado la BBDD con makemigrations porque le tendremos que hacer cambios y pensarlo bien.

"""
class Empleado(models.Model):
    dni = models.CharField
    nombre = models.CharField
    apellidos = models.CharField
    # Esto lo he visto en la web de django y verifica que el email existe.
    email = models.EmailField(max_length=254)
    telefono = models.IntegerField


class Tarea(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)
    fecha_inicio_fin = models.DateField
    # Tarea tiene una relacion muchas a uno, tiene un empleado por tarea, pero un empleado puede tener varias tareas.
    responsable = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    nivel_prioridad = models.IntegerField()
    # Esto lo he cogido de la web de django: https://docs.djangoproject.com/en/3.0/ref/models/fields/ , es para darle unos valores fijos y que no puedan ser otros. Vienen en el pdf.
    estado_tarea_choices = (
        ('--------', '--------'),
        ('abierta', 'abierta'),
        ('asignada', 'asignada'),
        ('en proceso', 'en proceso'),
        ('finalizada', 'finalizada'),
    )
    estado_tarea = models.CharField(choices=estado_tarea_choices, default='--------', max_length=100)
"""

class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.IntegerField()
    nombre_cliente = models.CharField(max_length=40)
    apellidos_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    telefono_cliente = models.IntegerField()
    # Proyecto tiene una relacion uno a muchos, tiene varias tareas.
    #tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    # Proyecto tiene una relacion muchos a muchos, tiene varios empleados y un empleado, puede tener varios proyectos.
    #empleado = models.ManyToManyField(Empleado)
