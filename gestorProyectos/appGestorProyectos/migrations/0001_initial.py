# Generated by Django 3.0.5 on 2020-04-17 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('fecha_inicio_fin', models.DateField()),
                ('nivel_prioridad', models.IntegerField(default=0)),
                ('estado_tarea', models.CharField(choices=[('abierta', 'abierta'), ('asignada', 'asignada'), ('en proceso', 'en proceso'), ('finalizada', 'finalizada')], max_length=50)),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appGestorProyectos.Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('presupuesto', models.IntegerField(default=0)),
                ('cliente', models.CharField(max_length=50)),
                ('empleado', models.ManyToManyField(to='appGestorProyectos.Empleado')),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appGestorProyectos.Tarea')),
            ],
        ),
    ]
