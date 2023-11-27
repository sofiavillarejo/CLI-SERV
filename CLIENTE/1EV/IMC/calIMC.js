function calcula() {
	console.log("Funcion calcular IMC");

	//variable que guardará el resultado del cálculo
	let IMC = 0;

	//variables que guardan el peso y altura del cliente
	let peso = Number(document.getElementById("peso").value);
	let altura = Number(document.getElementById("altura").value);

	//operacion para calcular el IMC y se reduen los decimales a 2
	IMC = (peso / (altura*altura)).toFixed(2);
	
	//mostrar resultado en pantalla
	document.getElementById("IMC").innerHTML = IMC;
}