import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Mac
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .admin import MacResource
from django.http import JsonResponse
from .devices import radius


# Create your views here.


@login_required
def home(request):
    try:
        statusPos = radius.status('10.11.20.238').find('timeout')
        statusValle = radius.status('10.12.11.36').find('timeout')
        macs = Mac.objects.all()
        return render(request, 'gestion.html',   {'macs': macs, 'statusPos': statusPos, 'statusValle': statusValle})
    except:
        messages.error(
            request, 'Error de conexion con el servidor radius', extra_tags='alert-danger')
        return redirect('/macamb')


@login_required
def agregarMac(request):
    try:
        mac = request.POST['mac']
        nombre = request.POST['nombre']
        buscar = Mac.objects.filter(mac=mac)
        if (len(buscar) > 0):
            messages.error(
                request, 'Error, el dispositivo ya existe', extra_tags='alert-warning')
            return redirect('/macamb')
        radius.agregarMac(mac, nombre)
        Mac.objects.create(mac=mac, nombre=nombre,
                           comentario=request.user.__str__(), fecha_creacion=datetime.datetime.now(), fecha_modificacion=datetime.datetime.now())
        messages.success(request, 'Dispositivo agregado',
                         extra_tags='alert-success')
    except:
        messages.error(request, 'Error, al agregar dispositivo',
                       extra_tags='alert-danger')
    return redirect('/macamb')


@login_required
def borrarMac(request, id):
    try:
        mac = Mac.objects.get(id=id)
        radius.borrarMac(mac.mac)
        mac.delete()
        messages.success(request, 'Dispositivo borrado',
                         extra_tags='alert-success')
        return JsonResponse({'success': True})
    except:
        messages.error(
            request, 'Error, el dispositivo no fue borrado', extra_tags='alert-danger')
    return redirect('/macamb')


@login_required
def editarMac(request, id):
    if request.method == 'GET':
        mac = Mac.objects.get(id=id)
        return render(request, 'editarMac.html', {'mac': mac})
    else:
        try:
            macVieja = request.POST['macVieja']
            mac = request.POST['mac']
            nombre = request.POST['nombre']
            comentario = request.user.__str__()
            radius.modificarMac(macVieja, mac, nombre)
            Mac.objects.filter(id=request.POST['id']).update(
                mac=mac,
                nombre=nombre,
                comentario=comentario,
                fecha_modificacion=datetime.datetime.now()
            )
            messages.success(request, 'Dispositivo editado',
                             extra_tags='alert-success')
        except Exception as e:
            print(e)
            messages.error(
                request, 'Error, el dispositivo no fue editado', extra_tags='alert-danger')
        return redirect('/macamb')


@login_required
def sincronizar(request):
    try:
        radius.sincronizar()
        messages.success(request, 'Sincronizado', extra_tags='alert-success')
        return redirect('/')
    except Exception as e:
        print(e)
        messages.error(request, 'Error, no se pudo sincronizar',
                       extra_tags='alert-danger')
        return redirect('/')


@login_required
def exportarMac(request):
    try:
        resource = MacResource()
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
