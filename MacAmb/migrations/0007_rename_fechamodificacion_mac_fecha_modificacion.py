# Generated by Django 4.2.7 on 2023-12-15 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MacAmb', '0006_rename_fecha_modificacion_mac_fechamodificacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mac',
            old_name='fechamodificacion',
            new_name='fecha_modificacion',
        ),
    ]
