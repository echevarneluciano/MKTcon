(function () {
  const btEliminar = document.querySelectorAll(".btEliminar");

  btEliminar.forEach((a) => {
    a.addEventListener("click", function (e) {
      const confirmar = confirm("¿Desea borrar la tarea?");
      if (!confirmar) {
        e.preventDefault();
      }
    });
  });
})();

$("#etiqueta").select2({
  tags: true,
});
$("#prioridad").select2({});

$(document).ready(function () {
  table = $("#dTable").DataTable({
    initComplete: function () {
      this.api()
        .columns()
        .every(function () {
          let column = this;
          const columnas = [6, 7, 9, 10, 11, 12];
          // Create select element
          let select = document.createElement("select");
          if (columnas.includes(column.index())) {
            select.add(new Option(""));
            column.footer().replaceChildren(select);
          }

          // Apply listener for user change in value
          select.addEventListener("change", function () {
            var val = DataTable.util.escapeRegex(select.value);

            column.search(val ? "^" + val + "$" : "", true, false).draw();
          });

          // Add list of options
          column
            .data()
            .unique()
            .sort()
            .each(function (d, j) {
              select.add(new Option(d));
            });
        });
    },
    language: {
      url: "https://cdn.datatables.net/plug-ins/1.13.7/i18n/es-ES.json",
    },
    responsive: true,
    scrollX: true,
  });

  var todas = document.querySelector("#todas");
  var checks = document.querySelectorAll(".form-check-input");
  var valoresSeleccionados = [];

  checks.forEach((el) => {
    el.addEventListener("click", function (e) {
      valoresSeleccionados.push($(this).val());
      let val = $(this).val();
      let column = table.column(val);
      todas.checked = false;
      column.visible(!column.visible());
    });
  });

  todas.addEventListener("click", function (e) {
    checks.forEach((e) => {
      e.checked = true;
    });
    valoresSeleccionados.forEach((el) => {
      let column2 = table.column(el);
      column2.visible(!column2.visible());
    });
    valoresSeleccionados = [];
  });
});
