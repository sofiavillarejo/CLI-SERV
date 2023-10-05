//EJERCICIO SEPARAR LETRAS EN LINEAS
function separaEnLineas() {
	//una variable para guardar el texto del input
	let texto = document.getElementById("texto").value; //me devuelve el contenido del input que mete el cliente en el html
	
	let salida = "";//para componer la salida con los parrafos y una letra en cada p
	//separar letras en lineas
	for (letra of texto){ //array (bucle) tipo for-of para recorrer el string
		console.log(letra);//con cada letra se crea un elemento p
		salida = salida + `<p>${letra}</p>`;
	}
	//se crean los elementos p del DOM dentro del div salida1
	document.getElementById("salida1").innerHTML = salida;
}
function contarLetras(){
	let texto = document.getElementById("texto").value;

	//contador para contar las letras
	let contador = 0;//asignandole un 0, le decimos que es de tipo entero porque el 0 es un nº entero
	
	//bucle for-of para recorrer cada letra
	for (letra of texto.toUpperCase()){
		if((letra >= "A") && (letra <= "Z")){//si la letra está entre A y Z, se cuenta
			contador++;
		}
	}

	document.getElementById("salida1").innerHTML = `<p>${contador}</p>`
}

function darLaVuelta(){
	//una variable para guardar el texto del input
	let texto = document.getElementById("texto").value;

	//variable que contendra la frase dada la vuelta
	let salida = "";

	//bucle para crear el texto dado la vuelta
	for (letra of texto){
		salida = letra + salida; //se concatena por delante y eso da la vuelta a la frase
	}

	document.getElementById("salida1").innerHTML = `<p>${salida}</p>`
}
function buscarPalabra() {
	//leer variable texto
	let texto = document.getElementById("texto").value;
	//variable para guardar la palabra a buscar
	let palabra = document.getElementById("palabra").value;

	//variable con el elemento p de salida
	let salida = "<p>La palabra no existe</p>";
	if(buscaP(texto,palabra)){
		salida = "<p>La palabra existe</p>";
	}
	//se crea el elemento p con el mensaje
	document.getElementById("salida1").innerHTML = salida;
}

function buscaP(t,p){
	//variable que cotiene el resultado de la busqueda
	let res = false;

	//si el resultado devuelve algo distinto de -1, es que la palabra si existe
	//el metodo indexOf devuelve -1 si la palabra no esta
	if(t.indexOf(p) != -1){
		res = true;
	}
	//si devuelve -1, la palabra no existe
	return res;//devolver el resultado
}
//contar la letra que introduzcas en palabra que hay en el texto que pongas en dato
function contarLetrasEnFrase(){
	let texto = document.getElementById("texto").value;
	//variable para guardar la palabra a buscar
	let letra = document.getElementById("letra").value;
 	let contador = 0;
 	for (l of texto.toUpperCase()){
 		if(l == letra.toUpperCase()){
 			contador++;
 		}
 	}
 	document.getElementById("salida1").innerHTML = `<p>${contador}</p>`;

}
function contarVocales(){
	let texto = document.getElementById("texto").value;
	//variable para guardar la palabra a buscar
 	let a = 0;
 	let e = 0;
 	let i = 0;
 	let o = 0;
 	let u = 0;

 	for(l of texto){
 	if(l == "a" || l == "A"){
 		a++;
 	}else if(l == "e" || l == "E"){
 		e++;

 	}else if(l == "i" || l == "I"){
 		i++;
 		
 	}else if(l == "o" || l == "O"){
 		o++;
 		
 	}else if(l == "u" || l == "U"){
 		u++;
 	}else{
 		document.getElementById("salida1").innerHTML = `<p>no hya vocales en el texto</p>`;
 	}

 	document.getElementById("salida1").innerHTML = `<p>hay ${a} as, ${e} es, ${i} is, ${o} os y ${u} us en el texto.</p>`;
 	}
}
function divideEnPalabras(t){

	res = t.split(" ");

	return res;
}

function divPal(){
	//una variable para guardar el texto del input
	let texto = document.getElementById("texto").value;

	let listaPalabras = divideEnPalabras(texto);

	document.getElementById("salida1").innerHTML = `<p>${listaPalabras}</p>`;
}