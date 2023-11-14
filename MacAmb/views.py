from django.shortcuts import render, redirect
from .models import Mac
from django.contrib import messages
from .devices import radius

# Create your views here.


def home(request):
    macs = Mac.objects.all()
    return render(request, 'gestion.html',   {'macs': macs})


def agregarMac(request):
    try:
        mac = request.POST['mac']
        nombre = request.POST['nombre']
        comentario = request.POST['comentario']
        radius.agregarMac(mac, nombre)
        Mac.objects.create(mac=mac, nombre=nombre, comentario=comentario)
        messages.success(request, 'Dispositivo agregado')
    except:
        messages.error(request, 'Error, en listar dispositivos')
    return redirect('/')


def borrarMac(request, id):
    try:
        mac = Mac.objects.get(id=id)
        radius.borrarMac(mac.mac)
        mac.delete()
        messages.success(request, 'Dispositivo borrado')
    except:
        messages.error(request, 'Error, el dispositivo no fue borrado')
    return redirect('/')


def editarMac(request, id):
    mac = Mac.objects.get(id=id)
    return render(request, 'editarMac.html', {'mac': mac})


def edicionMac(request):
    try:
        macVieja = request.POST['macVieja']
        mac = request.POST['mac']
        nombre = request.POST['nombre']
        comentario = request.POST['comentario']
        radius.modificarMac(macVieja, mac, nombre)
        Mac.objects.filter(id=request.POST['id']).update(
            mac=mac,
            nombre=nombre,
            comentario=comentario
        )
        messages.success(request, 'Dispositivo editado')
    except:
        messages.error(request, 'Error, el dispositivo no fue editado')
    return redirect('/')
