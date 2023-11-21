// A)VALIDAR TEXTO

function validaTexto() {
	let resultado = true;

	let texto = document.getElementById("texto").value;

	if(texto.length<8 || texto.length>10){
		alert("error: tiene que estar entre 8 y 10 caracteres");
		resultado = false;
	}

	if(texto.substring(0,3) != "123"){
		alert("Error: tiene que empezar por 123");
		resultado = false;
	}

	return resultado;
}

//  B) VALIDAR NUMEROS

function validaNumeros(){
	let resultado = true;

	let numero1 = parseInt(document.getElementById("numero1").value);
	let numero2 = parseInt(document.getElementById("numero2").value);

	if(!Number.isInteger(numero1)){
		alert("Error: Entero no valido");
		resultado=false;
	}
	if(!Number.isInteger(numero2)){
		alert("Error: Entero no valido");
		resultado=false;
	}

	if(numero1>numero2){
		alert("Error: el numero 1 tiene que ser mas pequeño que el numero 2");
		resultado=false;	
	}

	return resultado;
}