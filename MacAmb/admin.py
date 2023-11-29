from django.contrib import admin
from import_export import resources
from .models import Mac

# Register your models here.
admin.site.register(Mac)


class MacResource(resources.ModelResource):
    class Meta:
        model = Mac
        fields = (
            "id",
            "mac",
            "nombre",
            "comentario",
            "fechaCreacion",
            "fechaModificacion",
        )
