function creaTabla() {


	//obtener entradas del usuario
	let filas = document.getElementById('filas').value; // filas de la tablas
	let columnas = document.getElementById('columnas').value; // columnas de la tablas

	let cBorde = document.getElementById('conBorde').checked; //si tiene borde es true

	let color = document.getElementById('color').value; //color en formato #rrggbb

	//valores obtenidos de los parametros
	console.log(filas);
	console.log(columnas);
	console.log(cBorde);
	console.log(color);

	//obtener el div que va a contener la tabla
	let divTabla = document.getElementById('resultado');

	//borrar la tabla anterior si existe
	divTabla.firstChild.remove();

	//crear la tabla y el cuerpo de la tabla
	let tabla = document.createElement('table');
	let tbody = document.createElement('tbody');

	//añadir el cuerpo a la tabla y la tabla al div
	tabla.appendChild(tbody);
	divTabla.appendChild(tabla);

	//si está seleccionado el borde se pone con su color
	if (cBorde) {
		tabla.style.border = "5px solid "+color;
	}

	//bucle para crear las filas
	for (var i = 0; i < filas; i++) {
		//crear la fila
		let tr = document.createElement('tr');
		//si está seleccionado el borde se pone con su color
		if (cBorde) {
			tr.style.border = "3px solid "+color;
		}
		//se añade la fila al cuerpo
		tbody.appendChild(tr);
		//bucle para crear las columnas
		for (var j = 0; j < columnas; j++) {
			//crear una celda
			let td = document.createElement('td');
			//si está seleccionado el borde se pone con su color
			if (cBorde) {
				td.style.border = "1px solid "+color;
			}
			//se añade contenido a la celda, en este caso sus coordenadas en fila-columna
			td.innerHTML = i+'-'+j;
			//se añade la celda a la fila
			tr.appendChild(td);
		}		
	}
}