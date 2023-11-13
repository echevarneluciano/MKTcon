from django.shortcuts import render, redirect
from .models import Mac
from django.contrib import messages
from .devices import radius

# Create your views here.


def home(request):
    macs = Mac.objects.all()
    return render(request, 'gestion.html',   {'macs': macs})


def agregarMac(request):
    mac = request.POST['mac']
    nombre = request.POST['nombre']
    comentario = request.POST['comentario']
    radius.agregarMac(mac, nombre, comentario)
    messages.success(request, 'Dispositivo agregado')
    return redirect('/')


def borrarMac(request, id):
    mac = Mac.objects.get(id=id)
    mac.delete()
    messages.success(request, 'Dispositivo borrado')
    return redirect('/')


def editarMac(request, id):
    mac = Mac.objects.get(id=id)
    return render(request, 'editarMac.html', {'mac': mac})


def edicionMac(request):
    mac = request.POST['mac']
    nombre = request.POST['nombre']
    comentario = request.POST['comentario']
    Mac.objects.filter(id=request.POST['id']).update(
        mac=mac,
        nombre=nombre,
        comentario=comentario
    )
    messages.success(request, 'Dispositivo editado')
    return redirect('/')
