$("#etiqueta2").select2({
  tags: true,
});

var btnConfirmarEliminar = document.getElementById("btnConfirmarEliminar");
var tareaId = $("[name='id']").val();

btnConfirmarEliminar.addEventListener("click", function (e) {
  $("#eliminarModal").modal("hide");
  $.ajax({
    url: "/tareas/eliminar/tarea/" + tareaId,
    type: "GET",
    success: function () {
      window.location.href = "/tareas";
    },
  });
});
