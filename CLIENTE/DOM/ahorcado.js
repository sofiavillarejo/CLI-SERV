onload = inicio;

const dirImagenes = "imagenes/"

const palabras = ["PERRO","GATO","ORNITORRINCO","TIBURON"];

let palJugada = "";

let contadorAhorcado = 1;

function inicio(){
	palJugada= palabras[Math.floor(Math.random()*4)];

	document.getElementById('imagen').src=dirImagenes+"ahorcado"+contadorAhorcado+".png";	

	redibujaLineas(); 
}

function redibujaLineas(){
	let divLineas = document.getElementById("lineas");
	let numLetras = palJugada.length;
	for (var i = 0; i < numLetras; i++) {
		//let linea = document.createElement("<div class='col' id='linea"+i+"'><p>_</p></div>");
		let linea = document.createElement("div");
		linea.className="col";
		linea.id="linea"+i;
		let parrafo = document.createElement("p");
		parrafo.className="display-6"
		parrafo.innerHTML="_";
		linea.appendChild(parrafo);
		divLineas.appendChild(linea);
	}
}

function nuevoJuego() {
	//activar todos los botones
	document.getElementById('b_A').disabled = false;
	document.getElementById('b_A').style.background = "white";
	document.getElementById('b_B').disabled = false;
	document.getElementById('b_B').style.background = "white";
	document.getElementById('b_C').disabled = false;
	document.getElementById('b_C').style.background = "white";
	document.getElementById('b_D').disabled = false;
	document.getElementById('b_D').style.background = "white";
	document.getElementById('b_E').disabled = false;
	document.getElementById('b_E').style.background = "white";
	document.getElementById('b_F').disabled = false;
	document.getElementById('b_F').style.background = "white";
	document.getElementById('b_G').disabled = false;
	document.getElementById('b_G').style.background = "white";
	document.getElementById('b_H').disabled = false;
	document.getElementById('b_H').style.background = "white";
	document.getElementById('b_I').disabled = false;
	document.getElementById('b_I').style.background = "white";
	document.getElementById('b_J').disabled = false;
	document.getElementById('b_J').style.background = "white";
	document.getElementById('b_K').disabled = false;
	document.getElementById('b_K').style.background = "white";
	document.getElementById('b_L').disabled = false;
	document.getElementById('b_L').style.background = "white";
	document.getElementById('b_M').disabled = false;
	document.getElementById('b_M').style.background = "white";
	document.getElementById('b_N').disabled = false;
	document.getElementById('b_N').style.background = "white";
	document.getElementById('b_O').disabled = false;
	document.getElementById('b_O').style.background = "white";
	document.getElementById('b_P').disabled = false;
	document.getElementById('b_P').style.background = "white";
	document.getElementById('b_Q').disabled = false;
	document.getElementById('b_Q').style.background = "white";
	document.getElementById('b_R').disabled = false;
	document.getElementById('b_R').style.background = "white";
	document.getElementById('b_S').disabled = false;
	document.getElementById('b_S').style.background = "white";
	document.getElementById('b_T').disabled = false;
	document.getElementById('b_T').style.background = "white";
	document.getElementById('b_U').disabled = false;
	document.getElementById('b_U').style.background = "white";
	document.getElementById('b_V').disabled = false;
	document.getElementById('b_V').style.background = "white";
	document.getElementById('b_W').disabled = false;
	document.getElementById('b_W').style.background = "white";
	document.getElementById('b_X').disabled = false;
	document.getElementById('b_X').style.background = "white";
	document.getElementById('b_Y').disabled = false;
	document.getElementById('b_Y').style.background = "white";
	document.getElementById('b_Z').disabled = false;
	document.getElementById('b_Z').style.background = "white";
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
		for (var i = posLetra; i < numLetras; i++) {
			if(letra == palJugada.charAt(i)){
				let linea = document.getElementById("linea"+i);
				linea.innerHTML=letra;
				letrasAcertadas++;
			}
		}
alert(letrasAcertadas);
alert(numLetras);
		if(letrasAcertadas == numLetras){
			alert("Acertaste la palabra");
			nuevoJuego();			
		}
	}

}