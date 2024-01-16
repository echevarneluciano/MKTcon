import datetime
from django.shortcuts import redirect, render
from django.contrib import messages
from Tareas.models import Tarea

# Create your views here.


def homeTareas(request):
    if request.method == 'GET':
        tareas = Tarea.objects.all()
        tarea = Tarea()
        etiquetas = Tarea.objects.all().values_list('etiqueta', flat=True).distinct()
        estados = tarea.ESTADOS
        prioridades = tarea.PRIORIDADES
        categorias = tarea.CATEGORIAS
        sitios = tarea.SITIOS
        departamentos = tarea.DEPARTAMENTOS
        return render(request, 'homeTareas.html', {'tareas': tareas, 'estados': estados, 'etiquetas': etiquetas, 'prioridades': prioridades, 'categorias': categorias, 'sitios': sitios, 'departamentos': departamentos})
    else:
        creada = Tarea.objects.create(
            nombre=request.POST['nombre'],
            etiqueta=request.POST['etiqueta'],
            prioridad=request.POST['prioridad'].split("(")[1].split(",")[0],
            categoria=request.POST['categoria'].split("(")[1].split(",")[0],
            sitio=request.POST['sitio'].split("(")[1].split(",")[0],
            departamento=request.POST['departamento'].split(
                "(")[1].split(",")[0],
            descripcion=request.POST['descripcion'],
            fecha_creacion=datetime.datetime.now(),
            fecha_modificacion=datetime.datetime.now(),
            responsable=request.user.__str__(),
        )
        if (creada):
            messages.success(request, 'Tarea agregada',
                             extra_tags='alert-success')
        else:
            messages.error(request, 'Error, al agregar tarea',
                           extra_tags='alert-danger')
        return redirect('homeTareas')
