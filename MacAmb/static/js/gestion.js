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
