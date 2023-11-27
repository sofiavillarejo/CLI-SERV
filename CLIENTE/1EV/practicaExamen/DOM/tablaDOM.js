onload = inicio
//variables globales de tabla y el div del html
let miDiv = document.getElementById('miTabla');
//crear tabla
let tabla = document.createElement('table');
//dar estilo css a la tabla (atributos)
tabla.style.border = "1px solid black";
tabla.style.backgroundColor = "lightcoral";
tabla.style.borderCollapse = "collapse";

//coger el boton del html y crear un evento que al hacer click, saque los datos en la tabla
let boton = document.getElementById('boton');
boton.addEventListener("click", creaTabla);

//funcion que se hace nada mas entrar a la pagina
function inicio() {
    //crear fila
    let fila = document.createElement('tr');
    //crear encabezados de tabla
    let titulo1 = document.createElement('th');
    let titulo2 = document.createElement('th');
    //añadir titulo de los encabezados
    titulo1.innerHTML = "Producto";
    titulo2.innerHTML = "Precio";
    //atributos css
    titulo1.style.fontFamily = "sans-serif";
    titulo2.style.fontFamily = "sans-serif";
    //añadir los titulos a la fila
    fila.append(titulo1,titulo2);
    //añadir la fila a la tabla
    tabla.appendChild(fila);
    //añadir tabla al div del html
    miDiv.appendChild(tabla);
    
}
     
function creaTabla() {
    //leer datos del formulario y coger valores
    let producto = document.getElementById("producto").value;
    let precio = document.getElementById("precio").value;

    //crear fila contenedora de los valores de los inputs
    let filaContenido = document.createElement("tr");
    //crear las celdas de los dos valores
    let celdaProd = document.createElement("td");
    let celdaPrecio = document.createElement("td");
    //añadimos a las celdas, el texto sacado de los inputs
    celdaProd.innerHTML = producto;
    celdaPrecio.innerHTML = precio;
    //atributos css a las celdas
    celdaProd.style.border = "1px solid black";
    celdaProd.style.backgroundColor = "lightyellow";
    celdaPrecio.style.backgroundColor = "lightblue";
    celdaPrecio.style.border = "1px solid black";

    //añadir a la fila horizontal de la tabla, las dos celdas
    filaContenido.append(celdaProd, celdaPrecio);
    //añadir a la tabla, la fila con los datos
    tabla.appendChild(filaContenido);


}