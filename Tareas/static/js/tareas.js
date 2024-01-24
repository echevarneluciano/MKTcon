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
$("#etiqueta2").select2({
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
      let playId = $(this).attr("id");
      playId = playId.split("-")[2];
      tareaConfirmar.innerHTML = $(this).attr("value");
      btnConfirmar.addEventListener("click", function (e) {
        $("#playModal").modal("hide");
        $.ajax({
          url: "http://127.0.0.1:8000/tareas/play/tarea/" + playId,
          type: "GET",
          success: function (data) {
            var id = data[0].id;
            var estadoCambiar = document.getElementById("estado-" + id);
            var fechaMod = document.getElementById("fechaMod-" + id);
            estadoCambiar.innerHTML = "(1, 'En proceso')";
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
          },
        });
      });
    });
  });

  pauses.forEach((el) => {
    el.addEventListener("click", function (e) {
      let pauseId = $(this).attr("id");
      pauseId = pauseId.split("-")[2];
      tareaPausar.innerHTML = $(this).attr("value");
      btnConfirmarPausa.addEventListener("click", function (e) {
        $("#pauseModal").modal("hide");
        $.ajax({
          url: "http://127.0.0.1:8000/tareas/pause/tarea/" + pauseId,
          type: "GET",
          success: function (data) {
            var id = data[0].id;
            var estadoCambiar = document.getElementById("estado-" + id);
            var acumuladoCambiar = document.getElementById("acumulado-" + id);
            var fechaMod = document.getElementById("fechaMod-" + id);
            var fechaSinFormato = data[0].fecha_modificacion;
            var fechaFormateada =
              moment(fechaSinFormato).format("DD MMMM YYYY HH:mm");
            fechaMod.innerHTML = fechaFormateada;
            estadoCambiar.innerHTML = "(2, 'Pausada')";
            acumuladoCambiar.innerHTML = data[0].temp_acumulado;
            var desactivarPlay = document.getElementById("a-play-" + id);
            var desactivarPause = document.getElementById("a-pause-" + id);
            var desactivarStop = document.getElementById("a-stop-" + id);
            desactivarStop.style.filter = "grayscale(0%)";
            desactivarStop.style.pointerEvents = "auto";
            desactivarPause.style.filter = "grayscale(100%)";
            desactivarPause.style.pointerEvents = "none";
            desactivarPlay.style.filter = "grayscale(0%)";
            desactivarPlay.style.pointerEvents = "auto";
          },
        });
      });
    });
  });

  stops.forEach((el) => {
    el.addEventListener("click", function (e) {
      let stopId = $(this).attr("id");
      stopId = stopId.split("-")[2];
      tareaStop.innerHTML = $(this).attr("value");
      btnConfirmarStop.addEventListener("click", function (e) {
        $("#stopModal").modal("hide");
        $.ajax({
          url: "http://127.0.0.1:8000/tareas/stop/tarea/" + stopId,
          type: "GET",
          success: function (data) {
            var id = data[0].id;
            var estadoCambiar = document.getElementById("estado-" + id);
            var acumuladoCambiar = document.getElementById("acumulado-" + id);
            var fechaFin = document.getElementById("fechaCierre-" + id);
            var fechaCierreSinFormato = data[0].fecha_finalizacion;
            var fechaCierreFormateada = moment(fechaCierreSinFormato).format(
              "DD MMMM YYYY HH:mm"
            );
            fechaFin.innerHTML = fechaCierreFormateada;
            estadoCambiar.innerHTML = "(3, 'Finalizada')";
            acumuladoCambiar.innerHTML = data[0].temp_acumulado;
            var desactivarPlay = document.getElementById("a-play-" + id);
            var desactivarPause = document.getElementById("a-pause-" + id);
            var desactivarStop = document.getElementById("a-stop-" + id);
            desactivarStop.style.filter = "grayscale(100%)";
            desactivarStop.style.pointerEvents = "none";
            desactivarPause.style.filter = "grayscale(100%)";
            desactivarPause.style.pointerEvents = "none";
            desactivarPlay.style.filter = "grayscale(100%)";
            desactivarPlay.style.pointerEvents = "none";
          },
        });
      });
    });
  });
});
