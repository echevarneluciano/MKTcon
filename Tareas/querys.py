from datetime import timedelta
from Tareas.models import Tarea
from django.db.models import Q, F


def comentarios_archivo(connection, id):
    cursor = connection.cursor()
    query = """SELECT tareas_comentario.tarea, tareas_comentario.usuario, 
            tareas_comentario.comentario, tareas_comentario.fecha_creacion, 
            tareas_archivo.url, tareas_comentario.id    
            FROM tareas_archivo right join tareas_comentario 
            on tareas_archivo.comentario_id = tareas_comentario.id
            WHERE tareas_comentario.tarea = %s ORDER BY tareas_comentario.fecha_creacion DESC""" % (id)
    cursor.execute(query)
    consulta = cursor.fetchall()
    comentariosArchivos = []
    for row in consulta:
        dateTime = row[3]
        diferencia = timedelta(hours=3)
        fecha = dateTime - diferencia
        comentariosArchivos.append({
            'id': row[5],
            'tarea': row[0],
            'usuario': row[1],
            'comentario': row[2],
            'fecha_creacion': fecha,
            'url': row[4]
        })
    cursor.close()
    return (comentariosArchivos)


def ultimo_orden(responsable):
    tareas_responsable = Tarea.objects.filter(
        Q(responsable=responsable) & ~Q(estado=3)).order_by('-orden')
    if (tareas_responsable.count() == 0):
        return 1
    else:
        return tareas_responsable[0].orden+1


def ordenar_tareas(responsable):
    tareas_responsable = Tarea.objects.filter(
        Q(responsable=responsable) & ~Q(estado=3)).order_by('orden')
    for (i, tarea) in enumerate(tareas_responsable):
        tarea.orden = i+1
        tarea.save()
