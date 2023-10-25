//objeto que contiene la información de la partida
// tablero -> array
// turno -> int
// numero de fichas jugadas -> int
const juego = {
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

	//evaluar si en la jugada se hizo el tres en raya
	//se comprueba a partir de la quinta ficha jugada
	if(juego.numFich>=5){
		if(hayGanador()){
			document.getElementById('salida').innerHTML="El ganador es el jugador "+juego.turno;
			juego.partidaFinalizada=true;
		}else if(juego.numFich == 9){
			document.getElementById('salida').innerHTML="Empate";
			juego.partidaFinalizada=true;
		}
	}

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
}

function reiniciar(){
	juego.tablero = ["","","","","","","","",""];
	juego.turno = 1;
	juego.numFich = 0;
	juego.partidaFinalizada=false;

	document.getElementById('salida').innerHTML="";

	
	for(b of document.getElementsByClassName('boton')){
		b.innerHTML = "";
		b.disabled=false;
	}
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