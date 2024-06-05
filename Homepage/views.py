from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Create your views here.


def loginPage(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        try:
            nombre1 = request.POST['nombre'].lower()
            password1 = request.POST['password']
            user1 = authenticate(username=nombre1, password=password1)
            if (user1.is_staff is False):
                messages.error(
                    request, 'Error, usuario no autorizado, solicite permisos al administrador', extra_tags='alert-warning')
                return redirect('/login')
            if (user1 is not None):
                login(request, user1)
                messages.success(request, 'Usuario logeado',
                                 extra_tags='alert-success')
                return redirect('/tareas')
            else:
                messages.error(request, 'Error, al iniciar sesion',
                               extra_tags='alert-danger')
                return redirect('/login')
        except Exception as e:
            print(e)
            messages.error(
                request, 'Error, el usuario no se encuentra en el dominio', extra_tags='alert-danger')
            return redirect('/login')


def signout(request):
    logout(request)
    messages.success(request, 'Sesion cerrada', extra_tags='alert-success')
    return redirect('/login')
