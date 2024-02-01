// onload=principal;

// let plantilla;
// let tbodyDatos;//DONDE VOY A METER LOS DATOS

// function principal(){
	// //seleccionar elementos 
	// plantilla = document.getElementById("filaDatos");
	// tbodyDatos = document.getElementById("tablaDatos");

	// let filaTR = document.importNode(plantilla.content, true);//hago una copia del contenido de la plantilla y crea un nuevo nodo

	// filaTR.id = "vj1";//añadir id

	// let nombreTD = filaTR.querySelector("#nombre");//dentro del nodo busco el nombre
	// nombreTD.innerHTML = "AAA";//le añado contenido

	// let empresaTD = filaTR.querySelector("#empresa");
	// empresaTD.innerHTML = "BBBB";

	// tbodyDatos.appendChild(filaTR);//lo añado a la tabla

	// filaTR = document.importNode(plantilla.content, true);

	// filaTR.id = "vj2";//añadir id

	// nombreTD = filaTR.querySelector("#nombre");
	// nombreTD.innerHTML = "11111";

	// empresaTD = filaTR.querySelector("#empresa");
	// empresaTD.innerHTML = "2222";

	// let botonBorrar = filaTR.querySelector("#borrar");
	// botonBorrar.href = "www.google.com";//añadir atributo href

	// tbodyDatos.appendChild(filaTR);


	//conectarse por ajax al servidor, pedir los datos de videojuegos y rellenar la tabla
// }
////////////////////////////////////////////////////////////////////////////////
onload=principal;
let tbodyDatos;
//conectarse por ajax al servidor 
//pedir los datos de videojuegos
//rellenar la tabla

function principal(){
	//cada vez que se carga, vacia el tbody y luego vuelve a sacar los datos
	tbodyDatos = document.getElementById("tablaDatos");
	tbodyDatos.innerHTML = "";
	traerDatosServidor();

}

// cuando el servidor ejecuta el pedidatosAPI, me devuelve algo y lo convertimos en array de JS y lo devolvemos por la funcion. Entonces, se crean las filas.
function traerDatosServidor(){
	//crear el objeto para conectar al servidor
	const httprq = new XMLHttpRequest();

	//resolver la respuesta 
	//trozo de codigo que espera la respuesta del servidor
	httprq.onreadystatechange = function(){
		if(this.readyState == 4 && this.status == 200){ //si la respuesta es correcta
			console.log(this.responseText);

			let datos =  JSON.parse(this.responseText);
			creaFilas(datos);//datos es la listaVideojuegos que contiene todos los datos

		}else{ //la peticion tiene un error
			console.log("estado: "+this.readyState+", resp servidor:"+this.status);
		}
	}
	//hacer la llamada al servidor
	
	//contruir la peticion
	httprq.open("GET", "/SERVIDOR/videojuegos/pedirDatosAPI.py",true);//devuelve un array de arrays

	//ejecuto la peticion
	httprq.send();	
	
}

function creaFilas(listaVideojuegos){
	console.log(listaVideojuegos);

	const plantilla = document.getElementById("filaDatos");
	const tbodyDatos = document.getElementById("tablaDatos");

	//bucle
	for(let vj of listaVideojuegos){	

		let filaTR = document.importNode(plantilla.content, true);

		filaTR.querySelector("#fila").id = "vj"+vj[0];//cojo su id y lo cambio

		let nombreTD = filaTR.querySelector("#nombre");
		nombreTD.innerHTML = vj[1];

		let empresaTD = filaTR.querySelector("#empresa");
		empresaTD.innerHTML = vj[2];

		let tematicaTD = filaTR.querySelector("#tematica");
		tematicaTD.innerHTML = vj[3];

		let nJugTD = filaTR.querySelector("#nJug");
		nJugTD.innerHTML = vj[4];

		let publiTD = filaTR.querySelector("#publicacion");
		publiTD.innerHTML = vj[5];

		let borrarTD = filaTR.querySelector("#borrar");
		borrarTD.addEventListener("click", function(){borrar(vj[0]); });

		let modificarTD = filaTR.querySelector("#modificar");
		modificarTD.addEventListener("click", function(){modificar(vj[0]); });

		tbodyDatos.appendChild(filaTR);
	}
	//fin bucle
}

function borrar(id){
	alert(id);

	const httprq = new XMLHttpRequest();

	//resolver la respuesta 
	//trozo de codigo que espera la respuesta del servidor
	httprq.onreadystatechange = function(){
		if(this.readyState == 4 && this.status == 200){ //si la respuesta es correcta
			console.log(this.responseText);

			let borrado =  JSON.parse(this.responseText);
			if(borrado){
				let filaBorrar = document.getElementById("vj"+id);
				filaBorrar.remove();
			}else{
				alert("no se pudo borrar")
			}

		}else{ //la peticion tiene un error
			console.log("estado: "+this.readyState+", resp servidor:"+this.status);
		}
	}
	//hacer la llamada al servidor
	
	//contruir la peticion
	httprq.open("GET", "/SERVIDOR/videojuegos/borrarAPI.py?id="+id,true); //devuelve el id

	//ejecuto la peticion
	httprq.send();	
}
function modificar(id){
	alert(id);
}
function filtrar(){
	let nombre = document.getElementById("nombre").value;
	let empresa = document.getElementById("empresaForm").value;
	let tematica = document.getElementById("tematicaForm").value;
	let nJug = document.getElementById("numJugadoresForm").value;
	let anioInicial = document.getElementById("anioInicialForm").value;
	let anioFinal = document.getElementById("anioFinalForm").value;

	let filtro = ""
	if(empresa != ""){
		filtro += "empresa="+empresa;
	}
	if(tematica != ""){
		if(filtro != ""){
			filtro += "&tematica="+tematica;
		}else{
			filtro += "tematica="+tematica;
		}
	}
	if(nJug != ""){
		if(filtro != ""){
			filtro += "&numJugadores="+nJug;
		}else{
			filtro += "numJugadores="+nJug;
		}
	}
	if(anioInicial != ""){
		if(filtro != ""){
			filtro += "&anioInicial="+anioInicial;
		}else{
			filtro += "anioInicial="+anioInicial;
		}
	}	
	if(anioFinal != ""){
		if(filtro != ""){
			filtro += "&anioFinal="+anioFinal;
		}else{
			filtro += "anioFinal="+anioFinal;
		}
	}

	console.log(filtro);

	//crear el objeto para conectar al servidor
	const httprq = new XMLHttpRequest();

	//resolver la respuesta

	httprq.onreadystatechange = function(){
		if(this.readyState == 4 && this.status == 200){ //si la respuesta es correcta
			console.log(this.responseText);

			tbodyDatos = document.getElementById("tablaDatos");
			tbodyDatos.innerHTML = "";

			let datos =  JSON.parse(this.responseText);
			creaFilas(datos);

		}else{ //la peticion tiene un error
			console.log("estado: "+this.readyState+", resp servidor:"+this.status);
		}
	}

	//hacer la llamada al servidor
	//contruir la peticion
	httprq.open("GET", "/SERVIDOR/videojuegos/filtrarDatosAPI.py?"+filtro,true);

	//ejecuto la peticion
	httprq.send();
}

function insertar(){
	let nombre = document.getElementById("nombreInsertar").value;
	let empresa = document.getElementById("empresaInsertar").value;
	let tematica = document.getElementById("tematicaInsertar").value;
	let nJug = document.getElementById("numJugadoresInsertar").value;
	let publicacion = document.getElementById("anioInsertar").value;

	let insertaDatos = "";
	let datosOk = true;

	if(nombre != ""){
		insertaDatos += "nombre="+nombre;
	}else{
		datosOk = false;		
	}
	if(empresa != ""){
		insertaDatos += "&empresa="+empresa;
	}else{
		datosOk = false;		
	}
	if(tematica != ""){
		insertaDatos += "&tematica="+tematica;
	}else{
		datosOk = false;		
	}
	if(nJug != ""){
		insertaDatos += "&nJug="+nJug;
	}else{
		datosOk = false;		
	}
	if(publicacion != ""){
		insertaDatos += "&anio="+publicacion;
	}else{
		datosOk = false;		
	}	


	console.log(insertaDatos);	

	if(datosOk){
		//crear el objeto para conectar al servidor
		const httprq = new XMLHttpRequest();

		//resolver la respuesta

		httprq.onreadystatechange = function(){
			if(this.readyState == 4 && this.status == 200){ //si la respuesta es correcta
				console.log(this.responseText);
				principal();

			}else{ //la peticion tiene un error
				console.log("estado: "+this.readyState+", resp servidor:"+this.status);
			}
		}

		//hacer la llamada al servidor
		//contruir la peticion
		httprq.open("GET", "/SERVIDOR/videojuegos/insertaDatosAPI.py?"+insertaDatos,true);

		//ejecuto la peticion
		httprq.send();		
	}else{
		alert("datos incorrectos")
	}
}
