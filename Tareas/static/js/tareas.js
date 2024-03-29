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
  width: "resolve",
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

  table
    .column(7)
    .search("(?:Pausada|En proceso)", true, false, true)
    .draw(false);
  $("input:checkbox").on("change", function () {
    var finalizadas = $('input:checkbox[name="Finalizadas"]:not(:checked)')
      .map(function () {
        return "^" + this.value + "$";
      })
      .get()
      .join("|");
    table
      .column(7)
      .search(
        finalizadas
          ? "(?:Pausada|En proceso)"
          : "(?:Finalizada|Pausada|En proceso)",
        true,
        false,
        true
      )
      .draw(false);
  });

  var checks = document.querySelectorAll(".form-check-input");
  var plays = document.querySelectorAll(".a-play");
  var pauses = document.querySelectorAll(".a-pause");
  var stops = document.querySelectorAll(".a-stop");
  var tareaConfirmar = document.getElementById("tareaConfirmar");
  var btnConfirmar = document.getElementById("btnConfirmar");
  var tareaPausar = document.getElementById("tareaPausar");
  var btnConfirmarPausa = document.getElementById("btnConfirmarPausa");
  var tareaStop = document.getElementById("tareaStop");
  var btnConfirmarStop = document.getElementById("btnConfirmarStop");
  let playId;
  let pauseId;
  let stopId;
  var valoresSeleccionados = new Set();

  checks.forEach((el) => {
    el.addEventListener("click", function (e) {
      valoresSeleccionados.add($(this).val());
      let val = $(this).val();
      let column = table.column(val);
      todas.checked = false;
      if (valoresSeleccionados.size < 9) {
        column.visible(!column.visible());
      } else if (val != 0) {
        limite = alert("Limite de columnas alcanzado.");
      }
    });
  });

  todas.addEventListener("click", function (e) {
    checks.forEach((e) => {
      e.checked = true;
    });
    valoresSeleccionados.forEach((el) => {
      let column2 = table.column(el);
      column2.visible(true);
    });
    valoresSeleccionados.clear();
  });

  plays.forEach((el) => {
    el.addEventListener("click", function (e) {
      playId = $(this).attr("id");
      playId = playId.split("-")[2];
      tareaConfirmar.innerHTML = $(this).attr("value");
      e.preventDefault();
      e.stopPropagation();
      btnConfirmar.addEventListener("click", function (e) {
        $("#playModal").modal("hide");
        $.ajax({
          url: "/tareas/play/tarea/" + playId,
          type: "GET",
          success: function (data) {
            var id = data[0].id;
            var estadoCambiar = document.getElementById("estado-" + id);
            var fechaMod = document.getElementById("fechaMod-" + id);
            estadoCambiar.innerHTML = "En proceso";
            var fechaSinFormato = data[0].fecha_modificacion;
            var fechaFormateada =
              moment(fechaSinFormato).format("DD MMMM YYYY HH:mm");
            fechaMod.innerHTML = fechaFormateada;
            var desactivarPlay = document.getElementById("a-play-" + id);
            var desactivarPause = document.getElementById("a-pause-" + id);
            var desactivarStop = document.getElementById("a-stop-" + id);
            desactivarPause.style.filter = "grayscale(0%)";
            desactivarPause.style.pointerEvents = "auto";
            desactivarStop.style.filter = "grayscale(0%)";
            desactivarStop.style.pointerEvents = "auto";
            desactivarPlay.style.filter = "grayscale(100%)";
            desactivarPlay.style.pointerEvents = "none";
            e.preventDefault();
            e.stopPropagation();
          },
        });
      });
    });
  });

  pauses.forEach((el) => {
    el.addEventListener("click", function (e) {
      pauseId = $(this).attr("id");
      pauseId = pauseId.split("-")[2];
      tareaPausar.innerHTML = $(this).attr("value");
      e.preventDefault();
      e.stopPropagation();
      btnConfirmarPausa.addEventListener("click", function (e) {
        $("#pauseModal").modal("hide");
        $.ajax({
          url: "/tareas/pause/tarea/" + pauseId,
          type: "GET",
          success: function (data) {
            var id = data.tarea[0].id;
            var estadoCambiar = document.getElementById("estado-" + id);
            var acumuladoCambiar = document.getElementById("acumulado-" + id);
            var fechaMod = document.getElementById("fechaMod-" + id);
            var fechaSinFormato = data.tarea[0].fecha_modificacion;
            var fechaFormateada =
              moment(fechaSinFormato).format("DD MMMM YYYY HH:mm");
            fechaMod.innerHTML = fechaFormateada;
            estadoCambiar.innerHTML = "Pausada";
            acumuladoCambiar.innerHTML = data.acumulado;
            var desactivarPlay = document.getElementById("a-play-" + id);
            var desactivarPause = document.getElementById("a-pause-" + id);
            var desactivarStop = document.getElementById("a-stop-" + id);
            desactivarStop.style.filter = "grayscale(0%)";
            desactivarStop.style.pointerEvents = "auto";
            desactivarPause.style.filter = "grayscale(100%)";
            desactivarPause.style.pointerEvents = "none";
            desactivarPlay.style.filter = "grayscale(0%)";
            desactivarPlay.style.pointerEvents = "auto";
            e.preventDefault();
            e.stopPropagation();
          },
        });
      });
    });
  });

  stops.forEach((el) => {
    el.addEventListener("click", function (e) {
      stopId = $(this).attr("id");
      stopId = stopId.split("-")[2];
      tareaStop.innerHTML = $(this).attr("value");
      e.preventDefault();
      e.stopPropagation();
      btnConfirmarStop.addEventListener("click", function (e) {
        $("#stopModal").modal("hide");
        $.ajax({
          url: "/tareas/stop/tarea/" + stopId,
          type: "GET",
          success: function (data) {
            var id = data.tarea[0].id;
            var estadoCambiar = document.getElementById("estado-" + id);
            var acumuladoCambiar = document.getElementById("acumulado-" + id);
            var fechaFin = document.getElementById("fechaCierre-" + id);
            var fechaCierreSinFormato = data.tarea[0].fecha_finalizacion;
            var fechaCierreFormateada = moment(fechaCierreSinFormato).format(
              "DD MMMM YYYY HH:mm"
            );
            fechaFin.innerHTML = fechaCierreFormateada;
            estadoCambiar.innerHTML = "Finalizada";
            acumuladoCambiar.innerHTML = data.acumulado;
            var desactivarPlay = document.getElementById("a-play-" + id);
            var desactivarPause = document.getElementById("a-pause-" + id);
            var desactivarStop = document.getElementById("a-stop-" + id);
            desactivarStop.style.filter = "grayscale(100%)";
            desactivarStop.style.pointerEvents = "none";
            desactivarPause.style.filter = "grayscale(100%)";
            desactivarPause.style.pointerEvents = "none";
            desactivarPlay.style.filter = "grayscale(100%)";
            desactivarPlay.style.pointerEvents = "none";
            e.preventDefault();
            e.stopPropagation();
          },
        });
      });
    });
  });
});
