document.onreadystatechange = function () {
  var state = document.readyState;
  if (state == 'interactive' || state == 'complete') {
    setTimeout(function(){
      document.getElementById('preloader').style.display = "none";
    }, 1000);
  }
};

//actualiza  imagen
function cambiarImagen() {
    var imagen = document.getElementById('imagen');
    imagen.innerHTML = '<img src="/img/iconos/logeado.png" alt="logeado" height="50" width="50">';
  }

