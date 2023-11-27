// a)EJERCICIO CON NUMEROS

let num1 = parseInt(prompt("Introduce el primer numero"));
let num2 = parseInt(prompt("Introduce el segundo numero"));
let num3 = parseInt(prompt("Introduce el tercero numero"));
let num4 = parseInt(prompt("Introduce el cuarto numero"));

let error = false;

if(!Number.isInteger(num1)){
	error=true;
}
if(!Number.isInteger(num2)){
	error=true;
}
if(!Number.isInteger(num3)){
	error=true;
}
if(!Number.isInteger(num4)){
	error=true;
}


if(error){
	alert("Error: por favor ingresa numeros enteros");
}else{
	let media = (num1+num2+num3+num4)/4;
	alert("La media es " + media);
}

// B)EJERCICIO CON PALABRAS

// let pal1 = prompt("Introduce la primera palabra");
// let pal2 = prompt("Introduce la segunda palabra");
// let pal3 = prompt("Introduce la tercera palabra");
// let pal4 = prompt("Introduce la cuarta palabra");


// let error2 = false;

// if(pal1.length<4 || pal2.length<4 || pal3.length<4 || pal4.length<4){
// 	error2=true;
// }

// if(error2){
// 	alert("Las palabras tienen que tener mas de 4 caracteres");
// }else{
// 	alert("La concatenacion de palabras es: " + pal1 + pal2 + pal3 + pal4)
// }

