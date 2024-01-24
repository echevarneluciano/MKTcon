import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from Tareas.models import Tarea
from datetime import datetime

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
            fecha_creacion=datetime.now(),
            fecha_modificacion=datetime.now(),
            responsable=request.user.__str__(),
        )
        if (creada):
            messages.success(request, 'Tarea agregada',
                             extra_tags='alert-success')
        else:
            messages.error(request, 'Error, al agregar tarea',
                           extra_tags='alert-danger')
        return redirect('homeTareas')


def playTarea(request, id):
    buscada = Tarea.objects.filter(id=id)
    if (buscada[0].estado == 2):
        Tarea.objects.filter(id=id).update(
            estado=1,
            fecha_modificacion=datetime.now(),
        )
        tarea = list(Tarea.objects.filter(id=id).values())
        return JsonResponse(tarea, safe=False)
    else:
        messages.error(request, 'Error, la tarea no se puede iniciar',
                       extra_tags='alert-danger')
        return redirect('homeTareas')


def pauseTarea(request, id):
    buscada = Tarea.objects.filter(id=id)
    if (buscada[0].estado == 1):
        actualizaAcumulado(id)
        Tarea.objects.filter(id=id).update(
            estado=2,
            fecha_modificacion=datetime.now(),
        )
        tarea = list(buscada.values())
        return JsonResponse(tarea, safe=False)
    else:
        messages.error(request, 'Error, la tarea no se puede pausar',
                       extra_tags='alert-danger')
        return redirect('/homeTareas')


def stopTarea(request, id):
    buscada = Tarea.objects.filter(id=id)
    if (buscada[0].fecha_creacion == buscada[0].fecha_modificacion):
        Tarea.objects.filter(id=id).update(
            estado=3,
            temp_acumulado='00:00:00',
            fecha_finalizacion=datetime.now(),
        )
        tarea = list(buscada.values())
        return JsonResponse(tarea, safe=False)
    if (buscada[0] != 3):
        Tarea.objects.filter(id=id).update(
            estado=3,
            fecha_finalizacion=datetime.now(),
        )
        actualizaAcumulado(id)
        tarea = list(Tarea.objects.filter(id=id).values())
        return JsonResponse(tarea, safe=False)
    else:
        messages.error(request, 'Error, la tarea no se puede finalizar',
                       extra_tags='alert-danger')
        return redirect('homeTareas')


def actualizaAcumulado(id):
    tarea = Tarea.objects.filter(id=id)
    tiempoAcumulado = datetime.strptime(
        tarea[0].temp_acumulado.__str__(), '%H:%M:%S')
    tiempoAhora = datetime.now()
    tiempoMod = datetime.fromtimestamp(
        tarea[0].fecha_modificacion.timestamp())
    tiempo = (tiempoAhora - tiempoMod)+(tiempoAcumulado-datetime(1900, 1, 1))

    tarea.update(temp_acumulado=tiempo.__str__())


def editarTarea(request, id):
    if request.method == 'GET':
        tarea = Tarea()
        etiquetas = Tarea.objects.all().values_list('etiqueta', flat=True).distinct()
        prioridades = tarea.PRIORIDADES
        categorias = tarea.CATEGORIAS
        sitios = tarea.SITIOS
        departamentos = tarea.DEPARTAMENTOS
        tareaEditar = Tarea.objects.get(id=id)
        return render(request, 'editarTarea.html', {'tarea': tareaEditar, 'etiquetas': etiquetas, 'prioridades': prioridades, 'categorias': categorias, 'sitios': sitios, 'departamentos': departamentos})
    else:
        tarea = Tarea.objects.get(id=id)
        tarea.nombre = request.POST['nombre']
        tarea.etiqueta = request.POST['etiqueta']
        tarea.prioridad = request.POST['prioridad'].split("(")[1].split(",")[0]
        tarea.categoria = request.POST['categoria'].split("(")[1].split(",")[0]
        tarea.sitio = request.POST['sitio'].split("(")[1].split(",")[0]
        tarea.departamento = request.POST['departamento'].split(
            "(")[1].split(",")[0]
        tarea.descripcion = request.POST['descripcion']
        tarea.save()
        messages.success(request, 'Tarea actualizada',
                         extra_tags='alert-success')
        return redirect('homeTareas')


def eliminarTarea(request, id):
    Tarea.objects.filter(id=id).delete()
    messages.success(request, 'Tarea eliminada', extra_tags='alert-success')
    return JsonResponse({'ok': True})
