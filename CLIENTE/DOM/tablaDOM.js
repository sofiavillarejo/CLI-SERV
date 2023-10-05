let cuerpo;
let fila = Number(document.getElementsById("fila")).value;
let columna = Number(document.getElementsById("columna")).value;
let color = document.getElementsById("color").value;
let borde = document.getElementsById("borde").value;

function crearTablaDOM() {

	cuerpo = document.getElementsByTagName("body")[0];
	for (var i = Things.length - 1; i >= 0; i--) {
		Things[i]
	}
	cuerpo.innerHTML = tabla;

}