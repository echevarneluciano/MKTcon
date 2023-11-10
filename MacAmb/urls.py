from django.urls import path
from MacAmb import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agregarMac', views.agregarMac, name='agregarMac'),
    path('borrarMac/<int:id>', views.borrarMac, name='borrarMac'),
    path('editarMac/<int:id>', views.editarMac, name='editarMac'),
    path('editarMac/edicionMac', views.edicionMac, name='edicionMac'),
]
