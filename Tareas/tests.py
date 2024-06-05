import datetime
from django.test import TestCase
from .models import Tarea, Departamento, Sitio, Comentario, Archivo

# Create your tests here.


class TareaTestCase(TestCase):
    def setUp(self):
        tarea_test = Tarea.objects.create(
            nombre="Tarea de prueba",
            etiqueta="Etiqueta de prueba",
            prioridad=1,
            categoria=1,
            sitio=1,
            responsable=1,
            fecha_creacion=datetime.now(),
            fecha_modificacion=datetime.now(),
        )
        tarea_creada = Tarea.objects.get(id=tarea_test.id)
        self.assertEqual(tarea_creada, tarea_test)
