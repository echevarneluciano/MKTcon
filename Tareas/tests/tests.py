from datetime import datetime
from django.test import TestCase
from Tareas.models import Tarea, Departamento, Sitio, Comentario, Archivo
from django.contrib.auth.models import User

# Create your tests here.


class TareaModelsTestCase(TestCase):

    def test_tarea(self):
        tarea_test = creaTarea()
        tarea_creada = Tarea.objects.get(id=tarea_test.id)
        self.assertEqual(tarea_creada, tarea_test)

    def test_archivo(self):
        tarea_test = creaTarea()
        comentario_test = creaComentario()
        archivo_test = Archivo.objects.create(
            tarea=tarea_test,
            comentario=comentario_test,
            url='test',
            fecha_creacion=datetime(
                2021, 4, 10, 10, 10, 10, 10, None),
        )
        archivo_creado = Archivo.objects.get(id=archivo_test.id)
        self.assertEqual(archivo_creado, archivo_test)

    def test_sitio(self):
        sitio_test = Sitio.objects.create(
            nombre='sitio test',
        )
        sitio_creado = Sitio.objects.get(id=sitio_test.id)
        self.assertEqual(sitio_creado, sitio_test)

    def test_departamento(self):
        departamento_test = Departamento.objects.create(
            nombre='departamento test',
        )
        departamento_creado = Departamento.objects.get(id=departamento_test.id)
        self.assertEqual(departamento_creado, departamento_test)


def creaTarea():
    tarea = Tarea.objects.create(
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
    return tarea


def creaComentario():
    comentario = Comentario.objects.create(
        tarea=creaTarea().id,
        usuario='luciano.echevarne',
        comentario='test',
        fecha_creacion=datetime(
            2021, 4, 10, 10, 10, 10, 10, None),
    )
    return comentario


class TareaViewsTestCase(TestCase):

    def test_home(self):
        self.credential = {
            'username': 'usuario_test', 'password': 'pass_test'
        }
        usuario = User.objects.create_user(**self.credential)
        response = self.client.get('/tareas/', follow=True, user=usuario)
        self.assertEqual(response.status_code, 200)
