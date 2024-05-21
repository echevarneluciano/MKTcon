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
      $("#" + valorComentario).remove();
    },
  });
});

$("button[name*='btEliminarComentario']").click(function () {
  valorComentario = $(this).val();
});

$(document).ready(function () {
  $("#btnComentar").on("click", function (e) {
    e.preventDefault();
    let formData = new FormData($("#formComentar")[0]);
    $.ajax({
      url: "/tareas/editar/tarea/agregarComentario/" + tareaId,
      type: "POST",
      data: formData,
      contentType: false,
      processData: false,
      success: function (data) {
        valorComentario = data.id;
        console.log(data);
        if (data.url) {
          url =
            "<p>" +
            "Archivo adjunto:&nbsp" +
            "<a href=/tareas/editar/tarea/descargar/" +
            data.url +
            " " +
            " > " +
            data.url +
            "</a>" +
            "</p>";
        } else {
          url = "";
        }
        $("#campoComentario").val("");
        $("#nuevoComentario").append(
          '<div class="col-12"' +
            "id=" +
            data.id +
            ">" +
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
            url +
            "</div>" +
            "</div>" +
            "</div>"
        );
      },
    });
  });
});
