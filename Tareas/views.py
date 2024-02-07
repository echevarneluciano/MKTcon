import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from Tareas.admin import TareaResource
from Tareas.models import Tarea
from datetime import datetime, timedelta
from babel.dates import format_timedelta

# Create your views here.


def homeTareas(request):
    try:
        if request.method == 'GET':
            tareas = Tarea.objects.filter(responsable=request.user).filter(
                fecha_creacion__gte=datetime.now() - timedelta(days=30)).order_by('-fecha_creacion')
            tarea = Tarea()
            etiquetas = Tarea.objects.all().values_list('etiqueta', flat=True).distinct()
            estados = tarea.ESTADOS
            for t in tareas:
                acumulado = timedelta(seconds=float(t.temp_acumulado))
                t.temp_acumulado = format_timedelta(
                    acumulado, threshold=1, locale='es'
                )
            prioridades = tarea.PRIORIDADES
            categorias = tarea.CATEGORIAS
            sitios = tarea.SITIOS
            departamentos = tarea.DEPARTAMENTOS
            return render(request, 'homeTareas.html', {'tareas': tareas, 'estados': estados, 'etiquetas': etiquetas, 'prioridades': prioridades, 'categorias': categorias, 'sitios': sitios, 'departamentos': departamentos})
        else:
            creada = Tarea.objects.create(
                nombre=request.POST['nombre'],
                etiqueta=request.POST['etiqueta'],
                prioridad=request.POST['prioridad'],
                categoria=request.POST['categoria'],
                sitio=request.POST['sitio'],
                departamento=request.POST['departamento'],
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
    except Exception as e:
        messages.error(request, 'Error, al cargar tareas.',
                       extra_tags='alert-danger')
        return redirect('homeTareas')


def playTarea(request, id):
    try:
        buscada = Tarea.objects.filter(id=id)
        if (buscada[0].estado == 2):
            Tarea.objects.filter(id=id).update(
                estado=1,
                fecha_modificacion=datetime.now(),
            )
            tarea = list(Tarea.objects.filter(id=id).values())
            return JsonResponse(tarea, safe=False)
        else:
            return redirect('homeTareas')
    except Exception as e:
        return redirect('homeTareas')


def pauseTarea(request, id):
    try:
        buscada = Tarea.objects.filter(id=id)
        if (buscada[0].estado == 1):
            actualizaAcumulado(id)
            Tarea.objects.filter(id=id).update(
                estado=2,
                fecha_modificacion=datetime.now(),
            )
            acumulado = timedelta(seconds=float(buscada[0].temp_acumulado))
            acumulado_esp = format_timedelta(
                acumulado, threshold=1, locale='es'
            )
            tarea = list(buscada.values())
            tarea_acumulado = {'acumulado': acumulado_esp, 'tarea': tarea}
            return JsonResponse(tarea_acumulado, safe=False)
        else:
            return redirect('/homeTareas')
    except Exception as e:
        return redirect('/homeTareas')


def stopTarea(request, id):
    try:
        buscada = Tarea.objects.filter(id=id)
        if (buscada[0].fecha_creacion == buscada[0].fecha_modificacion):
            Tarea.objects.filter(id=id).update(
                estado=3,
                temp_acumulado='0',
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
            acumulado = timedelta(seconds=float(buscada[0].temp_acumulado))
            acumulado_esp = format_timedelta(
                acumulado, threshold=1, locale='es'
            )
            tarea = list(buscada.values())
            tarea_acumulado = {'acumulado': acumulado_esp, 'tarea': tarea}
            return JsonResponse(tarea_acumulado, safe=False)
        else:
            return redirect('homeTareas')
    except Exception as e:
        return redirect('homeTareas')


def actualizaAcumulado(id):
    try:
        tarea = Tarea.objects.filter(id=id)
        tiempoAcumulado = timedelta(
            seconds=float(tarea[0].temp_acumulado)
        )
        tiempoAhora = datetime.now()
        tiempoMod = datetime.fromtimestamp(
            tarea[0].fecha_modificacion.timestamp())
        tiempo = (tiempoAhora - tiempoMod)
        tarea.update(temp_acumulado=tiempo.total_seconds() +
                     tiempoAcumulado.total_seconds())
    except Exception as e:
        print(e)


def editarTarea(request, id):
    try:
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
            tarea.prioridad = request.POST['prioridad']
            tarea.categoria = request.POST['categoria']
            tarea.sitio = request.POST['sitio']
            tarea.departamento = request.POST['departamento']
            tarea.descripcion = request.POST['descripcion']
            tarea.save()
            messages.success(request, 'Tarea actualizada',
                             extra_tags='alert-success')
            return redirect('homeTareas')
    except Exception as e:
        messages.error(request, 'Error, no se pudo actualizar',
                       extra_tags='alert-danger')
        return redirect('homeTareas')


def eliminarTarea(request, id):
    try:
        Tarea.objects.filter(id=id).delete()
        messages.success(request, 'Tarea eliminada',
                         extra_tags='alert-success')
        return JsonResponse({'ok': True})
    except Exception as e:
        messages.error(request, 'Error, no se pudo eliminar',
                       extra_tags='alert-danger')
        return JsonResponse({'ok': False})


def exportarTareas(request):
    try:
        resource = TareaResource()
        dataset = resource.export()
        response = HttpResponse(
            dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="macs.csv"'
        return response
    except Exception as e:
        print(e)
        messages.error(request, 'Error, no se pudo exportar',
                       extra_tags='alert-danger')
        return redirect('/')
