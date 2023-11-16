from django.shortcuts import render, redirect
from .models import Mac
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .devices import radius

# Create your views here.


def signup(request):
    return render(request, 'signup.html')


def signout(request):
    logout(request)
    return redirect('/login')


def login(request):
    return render(request, 'login.html')


def logear(request):
    try:
        nombre1 = request.POST['nombre']
        password1 = request.POST['password']
        user = authenticate(request, username=nombre1, password=password1)
        if (user is not None):
            login(request, user)
            messages.success(request, 'Cuenta logeada')
            return redirect('/')
        else:
            messages.error(request, 'Error, en iniciar sesion')
            return redirect('/login')
    except:
        messages.error(request, 'Error, en iniciar sesion')
        return redirect('/login')


def registrar(request):
    try:
        nombre = request.POST['nombre']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(
                username=nombre, password=password1)
            user.save()
        print(user)
        login(request, user)
        messages.success(request, 'Cuenta creada')
        return redirect('/')
    except:
        messages.error(
            request, 'Error, en registrar cuenta o cuenta existente')
        return redirect('/signup')


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
