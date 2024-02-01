onload=inicio;
let mc;
let ctx;
let ancho;
let largo;
let turno = 2;
let tablero = [" "," "," "," "," "," "," "," "," "];
let partidaFin = false;
let nFich = 0;

function inicio() {
	mc = document.getElementById('miCanvas');
	ancho = mc.width
	largo = mc.height;
	ctx = mc.getContext("2d");
	pintaTablero();
	//añadir un evento para capturar los clicks en el canvas
	mc.addEventListener('click',function(event) {jugada(event)});
}

function pintaTablero(){	
	//crear un rectangulo relleno color gris
	// dos primeros parametros son las coordenadas de la esquina arriba-izquierda
	// dos ultimos parametros son el ancho y el alto del rectangulo
	ctx.fillStyle = "gray"
	ctx.fillRect(0,0,ancho,largo)

	//crear nueve circulos blancos 
	ctx.fillStyle = "white"
	for (xCentro of [100,300,500]){
		for (yCentro of [100,300,500]){
			pintaCirculo(xCentro,yCentro);	
		}
	}
}

function pintaCirculo(xCentro, yCentro){
	//crear un circulo con los parametros coordenadas del centro, radio, inicio y fin del arco
	ctx.beginPath();
	ctx.arc(xCentro, yCentro,90,0,Math.PI*2);
	ctx.closePath();
	ctx.fill();
}
function color(xCentro, yCentro, pos){
	if(tablero[pos] == " " && partidaFin === false){
		ctx.beginPath();
		ctx.arc(xCentro, yCentro,90,0,Math.PI*2);
		ctx.closePath();
		ctx.fill();
		tablero[pos] = turno;
		nFich +=1;
	}
}


function jugada(evento){
	//saca las corrdenadas de donde pinches
	let x = evento.clientX - mc.getBoundingClientRect().left;
	let y = evento.clientY - mc.getBoundingClientRect().top;
	console.log(x + " - " + y);
	
	
		if(0<x && x<200 && 0<y && y<200){
			turnos(0);
			color(100,100, 0);
		}
		else if(200<x && x<400 && 0<y && y<200){
			turnos(1);
			color(300,100, 1);

		}
		else if(400<x && x<600 && 0<y && y<200){
			turnos(2);
			color(500,100,2);

		}
		else if(0<x && x<200 && 200<y && y<400){
			turnos(3);
			color(100,300,3);

		}
		else if(200<x && x<400 && 200<y && y<400){
			turnos(4);
			color(300,300,4);

		}
		else if(400<x && x<600 && 200<y && y<400){
			turnos(5);
			color(500,300,5);

		}
		else if(0<x && x<200 && 400<y && y<600){
			turnos(6);
			color(100,500,6);
		}
		else if(200<x && x<400 && 400<y && y<600){
			turnos(7);
			color(300,500,7);

		}
		else if (400<x && x<600 && 400<y && y<600){
			turnos(8);
			color(500,500,8);
		}

	  	if(nFich>=5){
			if(hayGanador()){
				if(turno == 1){
					document.getElementById('salida').innerHTML="El ganador es el jugador Rojo!";
					partidaFin = true;
				}else if(turno == 2){
					document.getElementById('salida').innerHTML="El ganador es el jugador Azul!";
					partidaFin = true;
				}
			}else if(nFich == 9){
				document.getElementById('salida').innerHTML="Empate";
				partidaFin = true;
			}
		}
	}

function turnos(posicion) {
	if(!partidaFin && tablero[posicion] == " "){
		if(turno==2){
			ctx.fillStyle = "red";
			turno = 1;
		}else{
			ctx.fillStyle="blue";
			turno = 2;
		}
	}
}

function hayGanador(){
	//fila arriba
	if(tablero[0]!= " " && tablero[0]==tablero[1] && tablero[1]==tablero[2]){
		return true;	
	}
	//fila medio
	if(tablero[3]!= " " && tablero[3]==tablero[4] && tablero[4]==tablero[5]){
		return true;	
	}
	//fila abajo
	if(tablero[6]!= " " && tablero[6]==tablero[7] && tablero[7]==tablero[8]){
		return true;	
	}
	//vertical izquierda
	if(tablero[0]!= " " && tablero[0]==tablero[3] && tablero[3]==tablero[6]){
		return true;	
	}
	//vertical del medio
	if(tablero[1]!= " " && tablero[1]==tablero[4] && tablero[4]==tablero[7]){
		return true;	
	}
	//vertical derecha
	if(tablero[2]!= " " && tablero[2]==tablero[5] && tablero[5]==tablero[8]){
		return true;
	}
	//diagonal del 0-8
	if(tablero[0]!= " " && tablero[0]==tablero[4] && tablero[4]==tablero[8]){
		return true;	
	}
	//diagonal 2-6
	if(tablero[2]!= " " && tablero[2]==tablero[4] && tablero[4]==tablero[6]){
		return true;	
	}
	return false;
}


