from django.db import models
from macaddress.fields import MACAddressField

# Create your models here.


class Mac(models.Model):
    id = models.AutoField(primary_key=True)
    mac = MACAddressField(null=True, blank=True)
    nombre = models.CharField(max_length=50)
    comentario = models.CharField(max_length=100)
    fecha_creacion = models.DateField()
    fecha_modificacion = models.DateField()

    class Meta:
        db_table = 'mac_abm_mac'

    def __str__(self):
        return self.mac.__str__() + ', ' + self.nombre+', ' + self.comentario
