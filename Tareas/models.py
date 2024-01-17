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
    DEPARTAMENTOS = (
        (1, 'POS finanzas'),
        (2, 'POS RRHH'),
        (3, 'Flamingo sistemas'),
        (4, 'Epic RRHH'),
    )
    SITIOS = (
        (1, 'San Luis'),
        (2, 'Merlo'),
        (3, 'Villa Mercedes'),
        (4, 'Nueva Galia'),
    )

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    etiqueta = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=400)
    temp_acumulado = models.IntegerField(null=True, default=0)
    responsable = models.CharField(max_length=100)
    estado = models.IntegerField(choices=ESTADOS, default=2)
    prioridad = models.IntegerField(choices=PRIORIDADES, default=1)
    categoria = models.IntegerField(choices=CATEGORIAS, default=1)
    departamento = models.IntegerField(choices=DEPARTAMENTOS, default=1)
    sitio = models.IntegerField(choices=SITIOS, default=1)
    fecha_creacion = models.DateTimeField()
    fecha_modificacion = models.DateTimeField(null=True, blank=True)
    fecha_finalizacion = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'tareas_tarea'
