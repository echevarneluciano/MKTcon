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


def signup(request):
    return render(request, 'signup.html')


def signout(request):
    logout(request)
    return redirect('login')


def logear(request):
    try:
        nombre1 = request.POST['nombre'].lower()
        password1 = request.POST['password']
        user1 = authenticate(username=nombre1, password=password1)
        if (user1.is_staff is False):
            messages.error(
                request, 'Error, usuario no autorizado, solicite permisos al administrador')
            return redirect('/login')
        if (user1 is not None):
            login(request, user1)
            messages.success(request, 'Usuario logeado')
            return redirect('/')
        else:
            messages.error(request, 'Error, al iniciar sesion')
            return redirect('/login')
    except Exception as e:
        print(e)
        messages.error(
            request, 'Error, el usuario no se encuentra en el dominio')
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
            messages.success(request, 'Cuenta creada')
            return redirect('/login')
        else:
            messages.error(
                request, 'Error, las contraseñas no coinciden')
            return redirect('/signup')
    except:
        messages.error(
            request, 'Error, en registrar cuenta o cuenta existente')
        return redirect('/signup')


@login_required
def home(request):
    try:
        macs = Mac.objects.all()
        return render(request, 'gestion.html',   {'macs': macs})
    except:
        messages.error(request, 'Error de conexion con el servidor radius')
        return redirect('/')


@login_required
def agregarMac(request):
    try:
        mac = request.POST['mac']
        nombre = request.POST['nombre']
        buscar = Mac.objects.filter(mac=mac)
        if (len(buscar) > 0):
            messages.error(request, 'Error, el dispositivo ya existe')
            return redirect('/')
        Mac.objects.create(mac=mac, nombre=nombre,
                           comentario=request.user.__str__())
        radius.agregarMac(mac, nombre)
        messages.success(request, 'Dispositivo agregado')
    except:
        messages.error(request, 'Error, en listar dispositivos')
    return redirect('/')


@login_required
def borrarMac(request, id):
    try:
        mac = Mac.objects.get(id=id)
        mac.delete()
        radius.borrarMac(mac.mac)
        messages.success(request, 'Dispositivo borrado')
    except:
        messages.error(request, 'Error, el dispositivo no fue borrado')
    return redirect('/')


@login_required
def editarMac(request, id):
    mac = Mac.objects.get(id=id)
    return render(request, 'editarMac.html', {'mac': mac})


@login_required
def edicionMac(request):
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
    return redirect('/')


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
