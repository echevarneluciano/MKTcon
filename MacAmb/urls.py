from django.urls import path
from MacAmb import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.signout, name='logout'),
    path('login/logear', views.logear, name='logear'),
    path('signup/registrar', views.registrar, name='registrar'),
    path('agregarMac', views.agregarMac, name='agregarMac'),
    path('borrarMac/<int:id>', views.borrarMac, name='borrarMac'),
    path('editarMac/<int:id>', views.editarMac, name='editarMac'),
    path('editarMac/edicionMac', views.edicionMac, name='edicionMac'),
]
