# Generated by Django 5.0.1 on 2024-01-12 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tareas', '0002_rename_duenio_tarea_responsable_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='categoria',
            field=models.IntegerField(choices=[(1, 'General'), (2, 'Redes'), (3, 'Soporte')], default=1),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='departamento',
            field=models.IntegerField(choices=[(1, 'POS finanzas'), (2, 'POS RRHH'), (3, 'Flamingo sistemas'), (4, 'Epic RRHH')], default=1),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='prioridad',
            field=models.IntegerField(choices=[(1, 'Baja'), (2, 'Media'), (3, 'Alta')], default=1),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='sitio',
            field=models.IntegerField(choices=[(1, 'San Luis'), (2, 'Merlo'), (3, 'Villa Mercedes'), (4, 'Nueva Galia')], default=1),
        ),
    ]
