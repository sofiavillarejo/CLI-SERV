//objeto que contiene la información de la partida
// tablero -> array
// turno -> int
// numero de fichas jugadas -> int

let juego = {
	tablero:["","","","","","","","",""],
	turno:1,
	numFich:0,
	partidaFinalizada:false
}


//funcion que desarrolla una jugada
function jugar(btn,pos){

	//aumentar el numero de fichas jugadas
	juego.numFich++;


	//poner la ficha en el tablero
	if(juego.turno==1){
		//turno de X 
		btn.innerHTML = "X";
		juego.tablero[pos] = "X";
	}else{
		//turno de O 
		btn.innerHTML = "O";
		juego.tablero[pos] ="O";
	}


	//deshabilitar el boton jugado
	btn.disabled=true;

	// Guardar el estado actual del juego en el historial
	juego.tablero.push(JSON.parse(JSON.stringify(juego)));

	//evaluar si en la jugada se hizo el tres en raya
	//se comprueba a partir de la quinta ficha jugada
	
	estaFinalizada();

	//comprobar que la partida está finalizada
	if(!juego.partidaFinalizada){
		//si no se acabo se cambia de turno
		if(juego.turno==1){
			//cambiar de turno al jugador 2
			juego.turno=2;
		}else{
			//cambiar de turno al jugador 1
			juego.turno=1;
		}
	}

	console.log(juego.numFich);

	//guardar estado del juego
	localStorage.setItem("juego", JSON.stringify(juego));

	localStorage.setItem("jugada"+juego.numFich, JSON.stringify(juego));
	
}

function reiniciar(){
	juego.tablero = ["", "", "", "", "", "", "", "", ""];
    juego.turno = 1;
    juego.numFich = 0;
    juego.partidaFinalizada = false;

	document.getElementById('retroceder').style.display = "none";
    document.getElementById('avanzar').style.display = "none";
	document.getElementById('salida').innerHTML="";

	
	for(b of document.getElementsByClassName('boton')){
		b.innerHTML = "";
		b.disabled=false;
	}
	localStorage.clear();
}

function hayGanador(){
	if(juego.tablero[0]!= "" && juego.tablero[0]==juego.tablero[1] && juego.tablero[1]==juego.tablero[2]){
		return true;	
	}
	if(juego.tablero[3]!= "" && juego.tablero[3]==juego.tablero[4] && juego.tablero[4]==juego.tablero[5]){
		return true;	
	}
	if(juego.tablero[6]!= "" && juego.tablero[6]==juego.tablero[7] && juego.tablero[7]==juego.tablero[8]){
		return true;	
	}
	if(juego.tablero[0]!= "" && juego.tablero[0]==juego.tablero[3] && juego.tablero[3]==juego.tablero[6]){
		return true;	
	}
	if(juego.tablero[1]!= "" && juego.tablero[1]==juego.tablero[4] && juego.tablero[4]==juego.tablero[7]){
		return true;	
	}
	if(juego.tablero[2]!= "" && juego.tablero[2]==juego.tablero[5] && juego.tablero[5]==juego.tablero[8]){
		return true;	
	}
	if(juego.tablero[0]!= "" && juego.tablero[0]==juego.tablero[4] && juego.tablero[4]==juego.tablero[8]){
		return true;	
	}
	if(juego.tablero[0]!= "" && juego.tablero[2]==juego.tablero[4] && juego.tablero[4]==juego.tablero[6]){
		return true;	
	}

	return false;
}

//cargar el DOM totalmente antess de ejecutar la funcion
document.addEventListener("DOMContentLoaded", function() {
    // Verificar si hay juego almacenado en localStorage
    const juegoGuardado = localStorage.getItem("juego");
    if (juegoGuardado) {
        // Restaurar el estado del juego desde localStorage
        juego = JSON.parse(juegoGuardado);
		const mensajeSalida = document.getElementById('salida');
		if (juego.partidaFinalizada) {
			if (hayGanador()) {
				mensajeSalida.innerHTML = "El ganador es el jugador " + juego.turno;
				document.getElementById('retroceder').style.display = "inline";
				document.getElementById('avanzar').style.display = "inline";
			} else {
				mensajeSalida.innerHTML = "Empate";
			}
		} else {
			mensajeSalida.innerHTML = "";
		}
		
        // Actualizar la interfaz gráfica
		estaFinalizada();
        actualizarInterfaz();
		
    }
});

function actualizarInterfaz() {
    // Actualizar los botones en el tablero
    for (let i = 0; i < juego.tablero.length; i++) {
        const btn = document.getElementById('btn' + i); //obtener los botones con su id unico (i)--> btn0, btn1 (como en el html le heos dados el id unico a cada uno)
        btn.innerHTML = juego.tablero[i]; // coloca X, O o vacío en el boton
        btn.disabled = juego.tablero[i] !== ""; //desactiva el boton si ya ha sido pulsado
    }
	
    // Actualizar el mensaje de salida
    const mensajeSalida = document.getElementById('salida');
    if (juego.partidaFinalizada) {
        if (hayGanador()) {
            mensajeSalida.innerHTML = "El ganador es el jugador " + juego.turno;
        } else {
            mensajeSalida.innerHTML = "Empate";
        }
    } else {
        mensajeSalida.innerHTML = "";
    }
}

function estaFinalizada(){
	if(juego.numFich>=5){
		if(hayGanador()){
			document.getElementById('retroceder').style.display = "inline";
			document.getElementById('avanzar').style.display = "inline";
			document.getElementById('salida').innerHTML="El ganador es el jugador "+juego.turno;
			juego.partidaFinalizada=true;
			jugadaFinal = juego.numFich;
			for(b of document.getElementsByClassName('boton')){
				b.disabled=true;
			}
		}else if(juego.numFich == 9){
			document.getElementById('salida').innerHTML="Empate";
			juego.partidaFinalizada=true;
			jugadaFinal = juego.numFich;
			for(b of document.getElementsByClassName('boton')){
				b.disabled=true;
			}
		}
	}
}

// Función de retroceso
function retroceder() {
	if(juego.numFich >1){
		let jugada = juego.numFich -1;
		let datosarray = JSON.parse(localStorage.getItem("jugada"+ jugada));
		juego = datosarray;
		actualizarInterfaz();
	}else{
		alert("No hay más jugadas anteriores!")
		document.getElementById('retroceder').style.display = "none";
	}
}

// Función de avance
function avanzar() {
	if(juego.numFich < jugadaFinal){
		let jugada = juego.numFich +1;
		let datosarray = JSON.parse(localStorage.getItem("jugada"+ jugada));
		juego = datosarray;
		actualizarInterfaz();
	}else{
		alert("Es la última jugada!");
		document.getElementById('avanzar').style.display = "none";

	}
}



