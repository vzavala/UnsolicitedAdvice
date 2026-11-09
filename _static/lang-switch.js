// Adds a flag button next to the light/dark mode button that opens the
// same page in the other edition (English at the site root, Spanish under es/).
document.addEventListener("DOMContentLoaded", function () {
  var base = "/UnsolicitedAdvice/";
  var path = window.location.pathname;
  var i = path.indexOf(base);
  var root = i >= 0 ? path.slice(0, i + base.length) : "/";
  var rest = path.slice(root.length);
  var inSpanish = rest.indexOf("es/") === 0;
  var target = inSpanish ? root + rest.slice(3) : root + "es/" + rest;
  if (target.endsWith("/")) target += "intro.html";

  var label = inSpanish ? "Read in English" : "Leer en español";
  var flag = inSpanish ? "🇺🇸" : "🇪🇸";

  document.querySelectorAll(".theme-switch-button").forEach(function (btn) {
    var a = document.createElement("a");
    a.href = target;
    a.className = "btn btn-sm lang-switch-button";
    a.title = label;
    a.setAttribute("aria-label", label);
    a.textContent = flag;
    btn.parentNode.insertBefore(a, btn);
  });
});
