# Generated by Django 4.2.7 on 2024-01-12 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('duenio', models.CharField(max_length=100)),
                ('estado', models.IntegerField()),
                ('prioridad', models.IntegerField()),
                ('categoria', models.IntegerField()),
                ('etiqueta', models.CharField(max_length=50)),
                ('sitio', models.CharField(max_length=50)),
                ('departamento', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateField()),
                ('fecha_modificacion', models.DateField()),
                ('fecha_finalizacion', models.DateField()),
            ],
            options={
                'db_table': 'tareas_tarea',
            },
        ),
    ]
