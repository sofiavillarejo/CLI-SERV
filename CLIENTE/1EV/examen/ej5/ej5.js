
//.js que cambia el color de fondo de cada fila (he puesto como se pondría lo del borde, pero al hacer click no me lo coge)
//he modificado un poco el ejercicio porque así sé hacerlo :)

//seleccionar cada boton y añadirle el evento
let boton1 = document.getElementById('boton1');
boton1.addEventListener("click", cambiaEstiloBorde1);

let boton2 = document.getElementById('boton2');
boton2.addEventListener("click", cambiaEstiloBorde2);

let boton3 = document.getElementById('boton3');
boton3.addEventListener("click", cambiaEstiloBorde3);

//funciones que añadimos a cada boton
function cambiaEstiloBorde1() {
    let id1 = document.getElementById("fila1");
    // id1.style.border = "3px solid red";
    id1.style.backgroundColor = "red";

}
function cambiaEstiloBorde2() {
    let id2 = document.getElementById("fila2");
    // id2.style.border = "3px solid red";
    id2.style.backgroundColor = "red";

}
function cambiaEstiloBorde3() {
    let id3 = document.getElementById("fila3");
    // id3.style.border = "3px solid red";
    id3.style.backgroundColor = "blue";

}
