onload=inicio;
let mc;
let ctx;
let ancho;
let largo;
let turno = 1;

function inicio(argument) {
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

function jugada(evento){
	//saca las corrdenadas de donde pinches
	let x = evento.clientX - mc.getBoundingClientRect().left;
	let y = evento.clientY - mc.getBoundingClientRect().top;
	console.log(x + " - " + y);
	turnos();

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

