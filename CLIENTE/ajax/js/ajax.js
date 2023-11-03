function llamadaAjax() {
	/*****************
	 * configurar el objeto para la petición al servidor
	 * ***************/
	//objeto para hacer peticiones al servidor -> XMLHttpRequest()
	let httprq = new XMLHttpRequest();//se usa el new porque es un objeto y se usa eso para construirlo

	/***********
	 * registrar la funcion que trata la respuesta del servidor
	 * 
	 * se hace mediante el evento onreadystatechange-> el evento se dispara cuando 
	 * se completa la respuesta del servidor
	 * *************/
	httprq.onreadystatechange = function () {
	//esta linea siempre es asi
		if(this.readyState == 4 && this.status == 200){ //si la respuesta es correcta, se ejecuta este codigo
			//para ver la diferencia entre texto normal y  el json
			console.log(this.responseText);
			//console.log(JSON.parse(this.responseText));//texto que me envia el servidor y que tengo que convertir en objeto de json
			let datos = JSON.parse(this.responseText);
			crearSalida(datos); //creo una funcion que contiene todo lo que me ha enviado el servidor
		} else{ // la peticion tiene un error
			console.log("estado: " +this.readyState+", respuesta servidor: "+this.status);
		}
	}

	/*************
	 * peticion al servidor
	***********/
	//construir peticion
	httprq.open("GET", "/SERVIDOR/ajaxServ/pedirdatos.py", true) //tiene 3 parametros: tipo de petición, que quiero pedir y ejecucion sincrona o asincrona

	//ejecuto la peticion
	httprq.send();
}

function crearSalida(datos) {
	/*
	let listaHtml = "<ul>"; //declaramos que esta variable va a abrir la lista
	for (d of datos){ //recorremos los datos
		listaHtml += "<li>" + d + "</li>" //añadimos a la variable de la lista la apertura de la lista y ademas, cada elemento + los datos
	}
 	listaHtml += "</ul>"
 	*/
 	let tablaHTML = "<table border='1px solid black'>";
 	for (d of datos){ //recorremos los datos
		tablaHTML += "<tr>"; 
		for (elem of d){
			tablaHTML += "<td>" +elem+ "</td>";
		}
		tablaHTML += "</tr>"; //añadimos a la variable de la lista la apertura de la lista y ademas, cada elemento + los datos
	}
 	tablaHTML += "</table>";
 	document.getElementById('salida').innerHTML = tablaHTML;
}

function insertaAjax() {
	//sacamos los valores de los campos del formulario qu eenvie el cliente
	let txt = document.getElementById("texto").value;
	let num = document.getElementById("numero").value;

	console.log(txt + ":" + num)

	let httprq = new XMLHttpRequest();

	let peticion = "/SERVIDOR/ajaxServ/pedirdatos.py?texto="+txt+"&numero="+num

	httprq.onreadystatechange = function () {
	//esta linea siempre es asi
		if(this.readyState == 4 && this.status == 200){ //si la respuesta es correcta, se ejecuta este codigo
			//para ver la diferencia entre texto normal y  el json
			console.log(this.responseText);
			//console.log(JSON.parse(this.responseText));//texto que me envia el servidor y que tengo que convertir en objeto de json
			let datos = JSON.parse(this.responseText);
			alert(datos); //creo una funcion que contiene todo lo que me ha enviado el servidor
		} else{ // la peticion tiene un error
			console.log("estado: " +this.readyState+", respuesta servidor: "+this.status);
		}
	}

	//construir peticion
	httprq.open("GET", peticion, true) //tiene 3 parametros: tipo de petición, que quiero pedir y ejecucion sincrona o asincrona

	//ejecuto la peticion
	httprq.send();
}
