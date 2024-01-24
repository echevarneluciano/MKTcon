$("#etiqueta2").select2({
  tags: true,
});
$("#prioridad").select2({});

var btnConfirmarEliminar = document.getElementById("btnConfirmarEliminar");
var tareaId = $("[name='id']").val();

btnConfirmarEliminar.addEventListener("click", function (e) {
  $("#eliminarModal").modal("hide");
  $.ajax({
    url: "http://127.0.0.1:8000/tareas/eliminar/tarea/" + tareaId,
    type: "GET",
    success: function () {
      window.location.href = "http://127.0.0.1:8000/tareas";
    },
  });
});
