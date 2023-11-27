//variables globales, es decir, se leen en todo el codigo
let x =2;
let y = 3;

function function_name() {
//estas variables se leen solo dentro de la funcion, desde fuera no se puede acceder a ellas
	let z = 5;
	let a = 1;
	x = 4; //aquí cambio el valor de la x global
}