# Generated by Django 5.0.1 on 2024-01-12 18:09

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
        migrations.AlterField(
            model_name='tarea',
            name='categoria',
            field=models.IntegerField(choices=[(1, 'En proceso'), (2, 'Pausada'), (3, 'Finalizada')], default=1),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='estado',
            field=models.IntegerField(choices=[(1, 'En proceso'), (2, 'Pausada'), (3, 'Finalizada')], default=1),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='prioridad',
            field=models.IntegerField(choices=[(1, 'En proceso'), (2, 'Pausada'), (3, 'Finalizada')], default=1),
        ),
    ]
