document.onreadystatechange = function () {
  var state = document.readyState;
  if (state == "interactive" || state == "complete") {
    setTimeout(function () {
      document.getElementById("preloader").style.display = "none";
    }, 600);
  }
};
