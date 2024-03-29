from django.db import models

# Create your models here.


class Tarea(models.Model):

    ESTADOS = (
        (1, 'En proceso'),
        (2, 'Pausada'),
        (3, 'Finalizada'),
    )
    PRIORIDADES = (
        (1, 'Baja'),
        (2, 'Media'),
        (3, 'Alta'),
    )
    CATEGORIAS = (
        (1, 'General'),
        (2, 'Redes'),
        (3, 'Soporte'),
    )

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    etiqueta = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=400)
    temp_acumulado = models.DecimalField(
        max_digits=20, decimal_places=6, null=True, blank=True, default=0)
    responsable = models.CharField(max_length=100)
    estado = models.IntegerField(choices=ESTADOS, default=2)
    prioridad = models.IntegerField(choices=PRIORIDADES, default=1)
    categoria = models.IntegerField(choices=CATEGORIAS, default=1)
    departamento = models.IntegerField(default=0)
    sitio = models.IntegerField(default=0)
    fecha_creacion = models.DateTimeField()
    fecha_modificacion = models.DateTimeField(null=True, blank=True)
    fecha_finalizacion = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'tareas_tarea'


class Departamento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'tareas_departamento'


class Sitio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'tareas_sitio'
