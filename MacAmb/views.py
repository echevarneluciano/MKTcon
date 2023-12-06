import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Mac
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .admin import MacResource
from .devices import radius


# Create your views here.


@login_required
def home(request):
    try:
        macs = Mac.objects.all()
        return render(request, 'gestion.html',   {'macs': macs})
    except:
        messages.error(request, 'Error de conexion con el servidor radius')
        return redirect('/macamb')


@login_required
def agregarMac(request):
    try:
        mac = request.POST['mac']
        nombre = request.POST['nombre']
        buscar = Mac.objects.filter(mac=mac)
        if (len(buscar) > 0):
            messages.error(request, 'Error, el dispositivo ya existe')
            return redirect('/macamb')
        Mac.objects.create(mac=mac, nombre=nombre,
                           comentario=request.user.__str__())
        radius.agregarMac(mac, nombre)
        messages.success(request, 'Dispositivo agregado')
    except:
        messages.error(request, 'Error, en listar dispositivos')
    return redirect('/macamb')


@login_required
def borrarMac(request, id):
    try:
        mac = Mac.objects.get(id=id)
        mac.delete()
        radius.borrarMac(mac.mac)
        messages.success(request, 'Dispositivo borrado')
    except:
        messages.error(request, 'Error, el dispositivo no fue borrado')
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
            messages.success(request, 'Dispositivo editado')
        except Exception as e:
            print(e)
            messages.error(request, 'Error, el dispositivo no fue editado')
        return redirect('/macamb')


@login_required
def sincronizar(request):
    try:
        radius.sincronizar()
        messages.success(request, 'Sincronizado')
        return redirect('/')
    except Exception as e:
        print(e)
        messages.error(request, 'Error, no se pudo sincronizar')
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
        messages.error(request, 'Error, no se pudo exportar')
        return redirect('/')
