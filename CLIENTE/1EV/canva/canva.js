onload=inicio;//mejor cargar toda la pagina antes

function inicio() {
const mc = document.getElementById('miCanvas'); //le pido al navegador que me busque con el id el objeto que es un canvas
ancho = mc.width;//ancho
largo = mc.height;//alto
const ctx = mc.getContext("2d"); //se trabaja sobre el contexto-> objeto que me permite dibujar en el canvas

//dibujar lineas diagonales
//principal
ctx.beginPath();
ctx.strokeStyle = "green";
ctx.moveTo(0, 0);
ctx.lineTo(ancho, largo);
ctx.stroke();
ctx.closePath();

//secundaria
ctx.beginPath(); //es como la funcion de un div
ctx.lineWidth = 8;//ancho de la linea
ctx.strokeStyle = "red";
ctx.moveTo(ancho, 0);
ctx.lineTo(0, largo);
ctx.stroke();
ctx.closePath();

//crear un rectangulo relleno de color gris
ctx.fillStyle= "grey";
ctx.fillRect(200,150,200,100) //coordenada de la esquina de arriba-izquierda (ancho), coordenada de la esquina de arriba-izquierda (alto), ancho de la figura a dibujar, alto de la figura a dibujar

//crear rectuangulo solo con el borde
ctx.lineWidth= 1;
ctx.strokeStyle = "yellow";
ctx.strokeRect(450, 150, 50, 100);


ctx.beginPath(); 
ctx.arc(100,100,100,0, Math.PI*2)
ctx.stroke();//dibuja el borde
ctx.fillStyle= "pink";
ctx.fill();//dibuja el contenido
ctx.closePath();

}
