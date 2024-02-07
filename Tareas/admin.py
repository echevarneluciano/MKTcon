from django.contrib import admin
from import_export import resources
from .models import Tarea

# Register your models here.

admin.site.register(Tarea)


class TareaResource(resources.ModelResource):
    class Meta:
        model = Tarea
        fields = (
            "id",
            "nombre",
            "etiqueta",
            "prioridad",
            "categoria",
            "sitio",
            "departamento",
            "responsable",
            "fecha_creacion",
            "fecha_modificacion",
            "fecha_finalizacion",
            "temp_acumulado",
            "estado",
            "descripcion",
        )
