from django.urls import path
from MacAmb import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sincro', views.sincronizar, name='sincronizar'),
    path('agregarMac', views.agregarMac, name='agregarMac'),
    path('borrarMac/<int:id>', views.borrarMac, name='borrarMac'),
    path('editarMac/<int:id>', views.editarMac, name='editarMac'),
    path('exportarMac', views.exportarMac, name='exportarMac'),
]
