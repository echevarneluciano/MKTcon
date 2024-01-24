from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeTareas, name='homeTareas'),
    path('play/tarea/<id>', views.playTarea, name='playTarea'),
    path('pause/tarea/<id>', views.pauseTarea, name='pauseTarea'),
    path('stop/tarea/<id>', views.stopTarea, name='stopTarea'),
    path('editar/tarea/<id>', views.editarTarea, name='editarTarea'),
    path('eliminar/tarea/<id>', views.eliminarTarea, name='eliminarTarea'),
]
