
from datetime import timedelta


def comentarios_archivo(connection, id):
    cursor = connection.cursor()
    query = """SELECT tareas_comentario.tarea, tareas_comentario.usuario, 
            tareas_comentario.comentario, tareas_comentario.fecha_creacion, 
            tareas_archivo.url   
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
            'tarea': row[0],
            'usuario': row[1],
            'comentario': row[2],
            'fecha_creacion': fecha,
            'url': row[4]
        })
    cursor.close()
    return (comentariosArchivos)
