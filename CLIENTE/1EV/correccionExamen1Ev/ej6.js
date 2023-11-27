function compruebaPrimo(){
	//crear el objeto para comunicar con el servidor

	let httprq = new XMLHttpRequest();

	//la funcion que trata la respuesta

	httprq.onreadystatechange = function(){
		if(this.readyState == 4 && this.status == 200){ //si la respuesta es correcta

			let esPrimo =  JSON.parse(this.responseText);
			if(esPrimo){
				document.getElementById("salida").innerHTML="Es un numero primo";
			}else{
				document.getElementById("salida").innerHTML="No es un numero primo";
			}
		}
	}	

	//generar la peticion la servidor

	let n = parseInt(document.getElementById("numero").value);
	if (Number.isInteger(n) && n > 0 && n < 100){
		//contruir la peticion
		httprq.open("GET", "/CLIENTE/examen1eval/primos.py?numero="+n,true);

		//ejecuto la peticion
		httprq.send();		
	}else{
		alert("El numero tiene que ser entero positivo menor que 100")
	}
}

function validarEmail(){
	//crear el objeto para comunicar con el servidor

	let httprq = new XMLHttpRequest();

	//la funcion que trata la respuesta

	httprq.onreadystatechange = function(){
		if(this.readyState == 4 && this.status == 200){ //si la respuesta es correcta

			let esEmail =  JSON.parse(this.responseText);
			if(esEmail){
				document.getElementById("salida1").innerHTML="Es un correo electronico correcto.";
			}else{
				document.getElementById("salida1").innerHTML="NO es un correo electronico correcto.";
			}
		}
	}	

	//generar la peticion la servidor

	let email =document.getElementById("email").value;

	//contruir la peticion
	httprq.open("GET", "/CLIENTE/examen1eval/validar_email.py?email="+email,true);

	//ejecuto la peticion
	httprq.send();		
}