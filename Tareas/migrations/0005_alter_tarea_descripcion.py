# Generated by Django 4.2.7 on 2024-01-16 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tareas', '0004_alter_tarea_estado_alter_tarea_fecha_finalizacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='descripcion',
            field=models.CharField(max_length=400),
        ),
    ]