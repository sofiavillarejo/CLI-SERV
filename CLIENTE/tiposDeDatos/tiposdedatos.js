function trataDato() {
	let dato = document.getElementById("dato").value;

	//let x1 = 34.00;
	//let x; -- undefined
	//let x = null; -- object
	

	//saca que tipo de datos es el introducido ( aunque asi saca siempre que es string)
	document.getElementById("salida").innerHTML = typeof dato;//si cambio a x1, pone number
}	