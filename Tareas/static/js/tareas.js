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
          const columnas = [5, 6, 7, 8, 9, 10];
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
  });

  document.querySelectorAll("a.toggle-vis").forEach((el) => {
    el.addEventListener("click", function (e) {
      e.preventDefault();

      let columnIdx = e.target.getAttribute("data-column");
      let column = table.column(columnIdx);

      if (columnIdx == 0) {
        table.columns().visible(true);
      }

      if (columnIdx == 1) {
        table.columns().visible(false);
      }

      // Toggle the visibility
      column.visible(!column.visible());
    });
  });
});
