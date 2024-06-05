from datetime import datetime, timezone
from django.test import TestCase
from Tareas.models import Tarea, Departamento, Sitio, Comentario, Archivo

# Create your tests here.


class TareaTestCase(TestCase):
    def test_tarea(self):
        tarea_test = Tarea.objects.create(
            nombre='tarea test',
            responsable='luciano.echevarne',
            etiqueta='test',
            prioridad='1',
            categoria='1',
            sitio='1',
            departamento='1',
            estado=2,
            fecha_creacion=datetime(
                2021, 4, 10, 10, 10, 10, 10, None),
            fecha_modificacion=datetime(
                2021, 4, 10, 10, 10, 10, 10, None),
            fecha_finalizacion=None,
        )
        tarea_creada = Tarea.objects.get(id=tarea_test.id)
        self.assertEqual(tarea_creada, tarea_test)

    def test_archivo(self):
        tarea_test = Tarea.objects.create(
            nombre='tarea test',
            responsable='luciano.echevarne',
            etiqueta='test',
            prioridad='1',
            categoria='1',
            sitio='1',
            departamento='1',
            estado=2,
            fecha_creacion=datetime(
                2021, 4, 10, 10, 10, 10, 10, None),
            fecha_modificacion=datetime(
                2021, 4, 10, 10, 10, 10, 10, None),
            fecha_finalizacion=None,
        )
        archivo_test = Archivo.objects.create(
            tarea=tarea_test.id,
            url='test',
            fecha_creacion=datetime(
                2021, 4, 10, 10, 10, 10, 10, None),
        )
        archivo_creado = Archivo.objects.get(id=archivo_test.id)
        self.assertEqual(archivo_creado, archivo_test)
