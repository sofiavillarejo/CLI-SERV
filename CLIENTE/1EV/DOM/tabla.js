onload=creaTabla;//cuando cargue toda la pagina, llama a funcion creartabla
let cuerpo; //variable global (se puede acceder siempre a ella)

function creaTabla() {
	//obtener el elemento body del DOM
	//devuelve un array siempre, pero si pongo el 0, le decimos que queremos el body y asi solucionamos posibles problemas
	//body solo hay 1 y está en la posicion 0
	cuerpo = document.getElementsByTagName("body")[0];
	//tabla con 2 filas y 3 celdas en cada una
	let tabla = "<table id='tablaCreada'><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>4</td><td>5</td><td>6</td></tr></table>"

	cuerpo.innerHTML = tabla;

	let tablaCreada = document.getElementById("tablaCreada");

	console.log(tablaCreada);

	//crear elementos
	let fila = document.createElement("tr");
	let celda1 = document.createElement("td");
	let celda2 = document.createElement("td");
	let celda3 = document.createElement("td");

	//rellenar los elementos celda con su contenido
	celda1.innerHTML="7"
	celda2.innerHTML="8"
	celda3.innerHTML="9"

	//añadir filas a la tabla
	fila.appendChild(celda1);
	fila.appendChild(celda2);
	fila.appendChild(celda3);

	//añadir la fila a la tabla
	tablaCreada.appendChild(fila);
}
