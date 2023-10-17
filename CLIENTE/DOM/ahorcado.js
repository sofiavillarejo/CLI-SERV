onload = inicio;

const dirImagenes = "imagenes/"

const palabras = ["PERRO","GATO","ORNITORRINCO","TIBURON"];

let palJugada = "";

let numLetras = 0;
let letrasAcertadas = 0;

let contadorAhorcado = 1;

function inicio(){
	palJugada= palabras[Math.floor(Math.random()*4)];
	numLetras = palJugada.length;
	letrasAcertadas = 0;
	contadorAhorcado = 1;
	document.getElementById('imagen').src=dirImagenes+"ahorcado"+contadorAhorcado+".png";	
	redibujaLineas(); 
}

function redibujaLineas(){
	let divLineas = document.getElementById("lineas");

	divLineas.innerHTML = "";
	
	for (var i = 0; i < numLetras; i++) {
		let linea = document.createElement("div");
		linea.className="col";
		let parrafo = document.createElement("p");
		parrafo.id="linea"+i;
		parrafo.className="display-6"
		parrafo.innerHTML="_";
		linea.appendChild(parrafo);
		divLineas.appendChild(linea);
		
	}
}

function nuevoJuego() {
	let listaBotones = document.getElementsByClassName("btn");
	for (boton of listaBotones){
		boton.disabled = false;	
		boton.className = "btn btn-secondary";
	}

	inicio();
}

function letraJugada(letra) {
	let posLetra=palJugada.indexOf(letra);
	if(posLetra==-1){
		document.getElementById('b_'+letra).disabled = true;
		document.getElementById('b_'+letra).className = "btn btn-danger";
		contadorAhorcado++;
		document.getElementById('imagen').src=dirImagenes+"ahorcado"+contadorAhorcado+".png";	
		if(contadorAhorcado==7){
			alert("Has perdido");
			nuevoJuego();
		}
	}else{
		document.getElementById('b_'+letra).disabled = true;
		document.getElementById('b_'+letra).className = "btn btn-success";
		//poner la letra en la linea de juego

		let linea = document.getElementById("linea"+posLetra);
		linea.innerHTML=letra;
		letrasAcertadas++;
		for (var i = posLetra+1; i < numLetras; i++) {
			if(letra == palJugada.charAt(i)){
				let linea = document.getElementById("linea"+i);
				linea.innerHTML=letra;
				letrasAcertadas++;
			}
		}

	}
	if(letrasAcertadas == numLetras){
		alert("Acertaste la palabra");
		nuevoJuego();			
	}
}