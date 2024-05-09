$("#etiqueta2").select2({
  tags: true,
});

var btnConfirmarEliminar = document.getElementById("btnConfirmarEliminar");
var btnConfirmarEliminar2 = document.getElementById("btnConfirmarEliminar2");
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

var valorComentario;

btnConfirmarEliminar2.addEventListener("click", function (e) {
  $("#eliminarModal2").modal("hide");
  $.ajax({
    url: "/tareas/editar/tarea/eliminarComentario/" + valorComentario,
    type: "GET",
    success: function () {
      window.location.href = "/tareas/editar/tarea/" + tareaId;
    },
  });
});

$("button[name*='btEliminarComentario']").click(function () {
  valorComentario = $(this).val();
});

$(document).ready(function () {
  $("#btnComentar").on("click", function (e) {
    e.preventDefault();
    $.ajax({
      url: "/tareas/editar/tarea/agregarComentario/" + tareaId,
      type: "POST",
      data: $("#formComentar").serialize(),
      success: function (data) {
        valorComentario = data.id;
        $("#campoComentario").val("");
        $("#nuevoComentario").append(
          '<div class="col-12"' +
            data.id +
            '">' +
            '<div class="card">' +
            '<div class="card-body">' +
            "<h5 >" +
            data.usuario +
            ":&nbsp</h5>" +
            data.comentario +
            '<div class="d-flex bd-highlight">' +
            '<p class=" w-100 bd-highlight">Ahora</p>' +
            '<button class="btn btn-danger  flex-shrink-1 bd-highlight" id="btnEliminar" data-bs-toggle="modal" data-bs-target="#eliminarModal2" type="button">Eliminar</button>' +
            "</div>" +
            "</div>" +
            "</div>" +
            "</div>"
        );
      },
    });
  });
});
