from django.db import models

# Create your models here.


class Mac(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=16)
    comentario = models.CharField(max_length=50)
    fechaCreacion = models.DateField(auto_now_add=True)
    fehcaModificacion = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre + ' ' + self.comentario
