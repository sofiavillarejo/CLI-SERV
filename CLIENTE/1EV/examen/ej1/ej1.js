//.js que pide al usuario que introduzca 4 palabras a través de un prompt y comprueba si cada palabra tiene mas de 4 letras

//crear variables que guardan el texto que introduce el usuario en el prompt
let palabra = prompt("Introduzca una palabra");
let palabra2 = prompt("Introduzca una palabra");
let palabra3 = prompt("Introduzca una palabra");
let palabra4 = prompt("Introduzca una palabra");

//condicional que comprueba si cada palabra tiene mas de 4 caracteres y sino, saca error
//si tiene mas de 4, saca el alert con la concatenacion de cada palabra.
if (palabra.length <4){
    alert("Error: Por favor ingresa más de 4 caracteres");
}else if (palabra2.length <4){
    alert("Error: Por favor ingresa más de 4 caracteres");
}else if (palabra3.length <4){
    alert("Error: Por favor ingresa más de 4 caracteres");
}else if (palabra4.length <4){
    alert("Error: Por favor ingresa más de 4 caracteres");
}else{
    alert(`La concatenación de tu textos es:  ${palabra} ${palabra2} ${palabra3} ${palabra4}`);
}



