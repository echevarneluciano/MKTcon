# Generated by Django 4.2.7 on 2023-11-09 19:17

from django.db import migrations
import macaddress.fields


class Migration(migrations.Migration):

    dependencies = [
        ('MacAmb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mac',
            name='nombre',
            field=macaddress.fields.MACAddressField(blank=True, integer=True, null=True),
        ),
    ]
