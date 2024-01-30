# Generated by Django 5.0.1 on 2024-01-19 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tareas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarea',
            old_name='duenio',
            new_name='responsable',
        ),
        migrations.AddField(
            model_name='tarea',
            name='temp_acumulado',
            field=models.TimeField(default='00:00:00'),
        ),
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
            name='descripcion',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='estado',
            field=models.IntegerField(choices=[(1, 'En proceso'), (2, 'Pausada'), (3, 'Finalizada')], default=2),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='fecha_creacion',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='fecha_finalizacion',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='fecha_modificacion',
            field=models.DateTimeField(blank=True, null=True),
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