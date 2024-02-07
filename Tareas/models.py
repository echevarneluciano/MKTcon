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
        (5, 'Sistemas'),
        (6, 'Arenas administracion'),
        (7, 'Arenas alimentos y bebidas'),
        (8, 'Arenas arenas play'),
        (9, 'Arenas casino'),
        (10, 'Arenas cctv'),
        (11, 'Arenas compras y distribucion'),
        (12, 'Arenas contabilidad'),
        (13, 'Arenas gerencia'),
        (14, 'Arenas hipodromo'),
        (15, 'Arenas hotel'),
        (16, 'Arenas mantenimiento'),
        (17, 'Arenas marketing'),
        (18, 'Arenas rrhh'),
        (19, 'Arenas servicios generales'),
        (20, 'Arenas tesoreria'),
        (21, 'Tropicana'),
        (22, 'Golden'),
        (23, 'POS compras y distribucion'),
        (24, 'POS contabilidad'),
        (25, 'POS gerencia'),
        (26, 'POS control'),
    )
    SITIOS = (
        (1, 'San Luis'),
        (2, 'Merlo'),
        (3, 'Villa Mercedes'),
        (4, 'Nueva Galia'),
        (5, 'Buena Esperanza'),
        (6, 'La Punta'),
        (7, 'Necochea'),
        (8, 'San Isidro'),
        (9, 'Concaran'),
        (10, 'Naschel'),
        (11, 'La Toma'),
        (12, 'Tilisarao'),
        (13, 'Santa Rosa'),
        (14, 'El Volcan'),
        (15, 'Potrero de los Funes'),
        (16, 'La Matanza'),
        (17, 'Union'),
        (18, 'San Francisco'),
        (19, 'Lujan'),
        (20, 'Candelaria'),
        (21, 'Quines'),
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
    departamento = models.IntegerField(choices=DEPARTAMENTOS, default=1)
    sitio = models.IntegerField(choices=SITIOS, default=1)
    fecha_creacion = models.DateTimeField()
    fecha_modificacion = models.DateTimeField(null=True, blank=True)
    fecha_finalizacion = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'tareas_tarea'
