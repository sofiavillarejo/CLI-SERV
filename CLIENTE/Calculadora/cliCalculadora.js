function calcula() {
	console.log("Funcion calcula");

	let resultado = 0; //variable para el calculo

	//leer datos del formulario (numeros)
	let n1 = Number(document.getElementById("num1").value); //obtener el valor del elemento a través del id
	let n2 = Number(document.getElementById("num2").value);

	console.log(n1);//imprime en consola los numeros que ha introducido el cliente 
	console.log(typeof(n2));

	//leer la operacion que queremos hacer
	let suma = document.getElementById("suma").checked;
	let resta = document.getElementById("resta").checked;
	let multi = document.getElementById("multi").checked;
	let divi = document.getElementById("divi").checked;

	console.log(suma);
	console.log(resta);
	console.log(multi);
	console.log(divi);


	//realizar operacion
	if(suma){
		resultado = n1 + n2;
	}
	if(resta){
		resultado = n1 - n2;
	}
	if(multi){
		resultado = n1 * n2;
	}
	if(divi){
		resultado = n1 / n2;
	}

	console.log(resultado);

	//mostrar el resultado
	document.getElementById("salida").innerHTML = resultado; //resultado tiene el calculo que acabo de hacer y con esto, se busca algo que su id es salida
	//y con el innerHTML (que es el contenido del parrafo) se mete el resultado obtenido
}