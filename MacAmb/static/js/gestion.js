$(document).ready(function () {
  $("#dTable").DataTable({
    language: {
      url: "https://cdn.datatables.net/plug-ins/1.13.7/i18n/es-ES.json",
    },
    responsive: true,
    columnDefs: [
      {
        targets: [6, 7],
        orderable: false,
      },
    ],
  });

  var btnConfirmarEliminar = document.getElementById("btnConfirmarEliminar");
  var btnEliminar = $(".btn.btn-danger");

  btnEliminar.on("click", function (e) {
    var macId = $(this).attr("value");
    btnConfirmarEliminar.addEventListener("click", function (e) {
      $("#eliminarModal").modal("hide");
      $.ajax({
        url: "/macamb/borrarMac/" + macId,
        type: "GET",
        success: function () {
          window.location.href = "/macamb";
        },
      });
    });
  });
});
