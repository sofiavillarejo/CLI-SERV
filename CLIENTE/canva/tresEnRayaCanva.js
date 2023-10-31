onload=inicio;
let mc;
let ctx;
let ancho;
let largo;
let turno = 1;
let circulosSeleccionados = [[false, false, false], [false, false, false], [false, false, false]];
let numFich = 0;
function inicio() {
	mc = document.getElementById('miCanvas');
	ancho = mc.width
	largo = mc.height;
	ctx = mc.getContext("2d");
	pintaTablero();
	//aÃ±adir un evento para capturar los clicks en el canvas
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
/*
function jugada(evento){
	//saca las corrdenadas de donde pinches
	let x = evento.clientX - mc.getBoundingClientRect().left;
	let y = evento.clientY - mc.getBoundingClientRect().top;
	console.log(x + " - " + y);
	turnos();
	if (circulosSeleccionados[fila][columna] === false){
		if(0<x && x<200 && 0<y && y<200){
			pintaCirculo(100,100);
		}
		else if(200<x && x<400 && 0<y && y<200){
			pintaCirculo(300,100);

		}
		else if(400<x && x<600 && 0<y && y<200){
			pintaCirculo(500,100);
		}
		else if(0<x && x<200 && 200<y && y<400){
			pintaCirculo(100,300);
		}
		else if(200<x && x<400 && 200<y && y<400){
			pintaCirculo(300,300);
		}
		else if(400<x && x<600 && 200<y && y<400){
			pintaCirculo(500,300);
		}
		else if(0<x && x<200 && 400<y && y<600){
			pintaCirculo(100,500);
		}
		else if(0<x && x<200 && 400<y && y<600){
			pintaCirculo(100,500);
		}
		else if(200<x && x<400 && 400<y && y<600){
			pintaCirculo(300,500);
		}
		else{
			pintaCirculo(500,500);
		}
	}else{
		circulosSeleccionados[fila][columna] = true;
	}

}
*/

function jugada(event) {
  let x = event.clientX - mc.getBoundingClientRect().left;
  let y = event.clientY - mc.getBoundingClientRect().top;

 // calcular la fila y columna en la que se hizo clic, utilizando las coordenadas x e y del clic y dividiéndolas por el tamaño de las celdas de la cuadrícula (200 píxeles)
  let fila = Math.floor(y / 200);
  let columna = Math.floor(x / 200);
  turno=1;
  numFich++;

  if (circulosSeleccionados[fila][columna] === false) {
    pintaCirculo(columna * 200 + 100, fila * 200 + 100);
    circulosSeleccionados[fila][columna] = true;

  } else if (fila === 0 && columna === 0) {
    // Si la fila y la columna son 0, pinta el primer círculo
    pintaCirculo(100, 100);
    circulosSeleccionados[0][0] = true;

  }
  console.log(circulosSeleccionados)
  console.log(numFich)

  if(numFich>=5){
	if(hayGanador()){
		document.getElementById('salida').innerHTML="El ganador es el jugador "+turno;
	}else if(numFich == 9){
		document.getElementById('salida').innerHTML="Empate";
	}
console.log(numFich)
}

function turnos() {
	if(turno ==1){
		ctx.fillStyle = "blue";
		turno = 2;
	}else{
		ctx.fillStyle="red";
		turno = 1;
	}
}

function hayGanador(){
	//fila arriba
	if(circulosSeleccionados[0][0]!= "" && circulosSeleccionados[0][0]==circulosSeleccionados[0][1] && circulosSeleccionados[0][1]==circulosSeleccionados[0][2]){
		return true;	
	}
	//fila medio
	if(circulosSeleccionados[1][0]!= "" && circulosSeleccionados[1][0]==circulosSeleccionados[1][1] && circulosSeleccionados[1][1]==circulosSeleccionados[1][2]){
		return true;	
	}
	//fila abajo
	if(circulosSeleccionados[2][0]!= "" && circulosSeleccionados[2][0]==circulosSeleccionados[2][1] && circulosSeleccionados[2][1]==circulosSeleccionados[2][2]){
		return true;	
	}
	//vertical izquierda
	if(circulosSeleccionados[0][0]!= "" && circulosSeleccionados[0][0]==circulosSeleccionados[1][0] && circulosSeleccionados[1][0]==circulosSeleccionados[2][0]){
		return true;	
	}
	//vertical del medio
	if(circulosSeleccionados[0][1]!= "" && circulosSeleccionados[0][1]==circulosSeleccionados[1][1] && circulosSeleccionados[1][1]==circulosSeleccionados[2][1]){
		return true;	
	}
	//vertical derecha
	if(circulosSeleccionados[0][2]!= "" && circulosSeleccionados[0][2]==circulosSeleccionados[1][2] && circulosSeleccionados[1][2]==circulosSeleccionados[2][2]){
		return true;
	}
	//diagonal del 0-8
	if(circulosSeleccionados[0][0]!= "" && circulosSeleccionados[0][0]==circulosSeleccionados[1][1] && circulosSeleccionados[1][1]==circulosSeleccionados[2][2]){
		return true;	
	}
	//diagonal 2-6
	if(circulosSeleccionados[0][0]!= "" && circulosSeleccionados[0][2]==circulosSeleccionados[1][1] && circulosSeleccionados[1][1]==circulosSeleccionados[2][0]){
		return true;	
	}
	return false;
}
}
