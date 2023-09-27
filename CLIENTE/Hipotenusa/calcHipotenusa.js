//creamos función calcula
function calcula() {
	console.log("Función calcula");
	//creamos variable para mostrar el resultado
	let resultado = 0;
	//crear variables para guardar los dos numeros que son el cateto 1 y el cateto 2
	let c1 = Number(document.getElementById("cat1").value);
	let c2 = Number(document.getElementById("cat2").value);

	//asignamos a resultado la operacion (raiz cuadrada de la suma de los catetos)
	resultado = Math.sqrt(c1*c1+c2*c2)
	//mostramos en la consola el resultado
	console.log(resultado);
	//mostramos el resultado por pantalla
	document.getElementById("salida").innerHTML = resultado;
}
