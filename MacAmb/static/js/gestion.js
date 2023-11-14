(function () {
  const btEliminar = document.querySelectorAll(".btEliminar");

  btEliminar.forEach((a) => {
    a.addEventListener("click", function (e) {
      const confirmar = confirm("¿Desea borrar el dispositivo?");
      if (!confirmar) {
        e.preventDefault();
      }
    });
  });
})();

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
});
