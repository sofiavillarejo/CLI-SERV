function validar() {
	let respuesta = false;


	let param1 = document.getElementById("parametro1");

	if (param1.value == "Hola"){
		respuesta=true;
	}else{
		param1.style.background = "red"
	}

	return respuesta
}