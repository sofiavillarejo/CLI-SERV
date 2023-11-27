//al ponerlo asi, creamos funcion para que se ejecute después de cargar la página. ES UN EVENTO--> algo que sucede dentro de la página.

// se quita esta funcion para que funcione lo de document onload=inicio;//le decimos al evento onload que hay una funcion que se llama inicio y que cuando la encuentre, la ejecute.
//onload=inicio(); no es lo mismo que lo anterior--> esto es ejecutar la función

let suma = 0;
suma = 2 + 5;
console.log(suma);

function inicio(frase) {
	//alert("Esto es un alert");
	console.log("esto es una salida por consola de desarrollo"); //esto se ve en el avegador fn+12
	console.log(suma);
	console.log(frase);

	document.getElementById("parrafo").innerHTML = "adios";
}
function nuevaVentana() {
	window.open();
}


