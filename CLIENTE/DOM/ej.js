let tamlista = 0;
function crearParrafo() {
	let texto = document.getElementById("entradaTexto").value;
	let parrafo = document.createElement('p');

	parrafo.innerHTML = texto;
	document.getElementById("miDiv").appendChild(parrafo);

}
function lista() {
	let li = document.createElement('li');
	tamlista++;

	li.innerHTML = "elemento de lista" +tamlista;
	document.getElementById("lista").appendChild(li);
}

function enlace(){
	let enlace = document.createElement('a');
	enlace.innerHTML =  "Visitar W3School";
	enlace.setAttribute('href', "https://www.w3schools.com/");
	document.getElementById("miDiv").appendChild(enlace);
}
function cambiaColor(){
	let elemento =document.getElementById("miElemento");
	const hexad = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"];
			
			let r = hexad[Math.floor(Math.random() * 16)]+hexad[Math.floor(Math.random() * 16)];
			let g = hexad[Math.floor(Math.random() * 16)]+hexad[Math.floor(Math.random() * 16)];
			let b = hexad[Math.floor(Math.random() * 16)]+hexad[Math.floor(Math.random() * 16)];

			let color = "#"+r+g+b

			console.log(color);

			elemento.style.background = color;

}

let tamActual = 0;

function cambiarTexto(){
	let miTexto = document.getElementById("miTexto");
	let nuevoTam= [10,20,30];

	tamActual++;
	if (tamActual == 3){
		tamActual= 0;
	}
	miTexto.style.fontSize = nuevoTam[tamActual]+'px';

}
//variable global
let opac = -1;
function ocultarElem(){

    let elementoOculto = document.getElementById("elementoOculto");
    let opacidades= ["0%","100%"];
    opac++;    
    if (opac == 2){
        opac= 0;
    }
    
    elementoOculto.style.opacity=opacidades[opac];  
}

function textoCambiante1() {
	let textCam = document.getElementById("textoCambiante");
	textCam.style.color="BlueViolet";
}
function textoCambiante2() {
	let textCam = document.getElementById("textoCambiante");
	textCam.style.color="maroon";
}
