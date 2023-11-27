// prompt
let nombre = prompt("Por favor, introduzca su nombre");
console.log(nombre);

//alert
alert(`Te llamas ${nombre}!`);

let texto = document.getElementById('salida');
texto.innerHTML = "Hola " + nombre;
texto.style.color = "red";

let miDiv = document.getElementById('miDiv');
let texto2 = document.createElement('p');
texto2.innerHTML = "holaaaa";
miDiv.appendChild(texto2);
texto2.style.color = "orange";

// let lista = document.createElement('p');
// lista.classList.add('parrafo1');
// console.log(lista.classList.contains('parrafo1')); //añadir clase al parrafo


