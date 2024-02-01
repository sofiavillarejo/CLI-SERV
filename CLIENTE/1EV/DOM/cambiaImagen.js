let dibujo = 1;
function cambiaImagen() {
	console.log("cambia la imagen");
	dibujo++;
	//dibujo > 7 ? dibujo = 1:dibujo=dibujo;//operador ternario 
	//el op.termanrio es igual que el if
	if(dibujo > 7){
		dibujo=1;
	}
	document.getElementById.src="imagenes/ahorcado"+dibujo+".png";

}