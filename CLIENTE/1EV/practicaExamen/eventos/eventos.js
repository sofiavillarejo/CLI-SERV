onload = alCargar

//evento onchange
function cambio() {
    // Código que se ejecutará cuando el valor del campo cambie
    let input = document.getElementById("input").value;
    console.log("Nuevo valor: " + input);
    let texto = document.getElementById('salida1');
    texto.innerHTML = "Evento onchange-> cada vez qe se mete algo nuevo en el input ---->" + input;
}
//evento onclick
function hacerClick() {
    let texto2 = document.getElementById("salida2");
    texto2.style.backgroundColor = "red";
}
//evento onmouseover
function ratonEncima() {
    let text3 = document.getElementById("salida3");
    text3.style.backgroundColor = "yellow";
}
//evento onmouseout
function ratonFuera() {
    let texto4 = document.getElementById("salida4");
    texto4.style.backgroundColor = "pink";
}

//evento onload
function alCargar() {
    let texto6 = document.getElementById("salida6");
    texto6.style.backgroundColor = "orange";
}