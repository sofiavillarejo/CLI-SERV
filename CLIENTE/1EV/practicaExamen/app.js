//seleccionar el div toppings del html y mostrar lo seleccionado en consola
// OBTENER ELEMENTOS POR EL ID
let divToppings = document.getElementById('toppings');
console.log(divToppings);
console.log("Ejemplo .innerHTML -->" + divToppings.innerHTML); //.innerHTML --> acceder al contenido que tenga dentro el id seleccionado
console.log(typeof divToppings);
console.log(divToppings.innerText);//devuelve todo el texto que tenga dentro
console.log(divToppings.tagName) //saca el tipo de etiqueta que sea (DIV)

//OBTENER ELEMENTOS POR LA CLASE
const toppings = document.getElementsByClassName('topping');
console.log(toppings.length); //total de elementos
console.log("Id primera posición: "+ toppings[0].id +"\nNombre de la clase de la segunda posición: " +toppings[1].className);

//AÑADIR OTRO LI A LA LISTA NO ORDENADA
let lista = document.createElement('li');
lista.innerHTML = "Champiñones";
document.getElementById('lista-toppings').appendChild(lista);

const misToppings = document.getElementsByTagName('li'); //seleccionar todos los li del html
console.log(misToppings);

//COMBINAR SELECTORES
//sacar el primer topping de la lista que tenga la clase topping y el ide aceitunas
const primerToppingClaseIdAceitunas = document.querySelector('.topping#aceitunas');
console.log(primerToppingClaseIdAceitunas);

const variosElementos = document.querySelectorAll('.topping#albahaca,#cebolla');
console.log(variosElementos);

// RESUMEN -->
//     -.getElementById()
//     -.getElementsByClassName()
//     -.querySelector()
//     -.querySelectorAll()

////////////////////////////////////////////////////////////
//CAMBIAR EL ESTILO DE LOS ELEMENTOS EN EL DOM
let cambioColor = document.getElementById('aceitunas');
cambioColor.style.color="red";

let cambioTamLetra = document.getElementById('albahaca');
cambioTamLetra.style.fontSize="25px";

let cambioBackgColor = document.getElementById('cebolla');
cambioBackgColor.style.backgroundColor="orange";
cambioBackgColor.style.textTransform="uppercase";

/////////////////////////////////////////////////////////////////////
//TEXTO EN EL DOM///////////////////////////////////////

const listaToppings = document.getElementById('lista-toppings');
console.log(listaToppings.innerText); //sacar el texto que contenga
console.log(listaToppings.textContent); //sacar el texto que contenga pero de la misma forma que esta en el html (con espacios y todo)
console.log(listaToppings.innerHTML); //retorna la estrucutra interna del html del elemento seleccionado

//MODIFICAR TEXTO EN EL DOM
let texto = document.getElementById('titulo');
texto.innerHTML = "Nuevo titulo modificado"; //se cambia el titulo a traves del DOM

//MODIFICAR ATRIBUTOS EN EL DOM
const enlaces = document.getElementsByTagName('a');
console.log(enlaces[0].getAttribute('href')); //saca lo que contiene el atributo
console.log(enlaces[0].removeAttribute('href'));//borrar el atributo
console.log(enlaces[0].setAttribute('href', 'https://www.abrirllave.com/html/ejercicio-grupo-de-musica-queen.php'))//cambiar el contenido del atributo (atributo, valor_nuevo)

//MODIFICAR CLASES
const primerTopping = document.querySelector('.topping'); //seleccionamos el primer elemento con la clase topping que encuentre
console.log(primerTopping); //saca el li aceitunas
console.log(primerTopping.classList); //saca la lista de todas las clases que tiene asignadas

//AGREGAR UNA CLASE AL ELEMENTO
primerTopping.classList.add('miClase');
console.log(primerTopping.classList);

//comprobar si contiene la clase indicada
console.log(primerTopping.classList.contains('topping')); //devuelve true or false

//eliminar una clase
primerTopping.classList.remove('topping');
console.log(primerTopping.classList);

/////////////////////////////////////////////////////////////////
//CREAR ELEMENTOS /////////////////////////////
const divEnlaces = document.getElementById('enlaces');//seleccionamos donde vamos a meter el elemento
const toppingNuevo =document.createElement('a');//creamos el elemento enlace
toppingNuevo.classList.add('enlace', 'segundo-enlace'); //añadimos clases
toppingNuevo.setAttribute('href', 'https://www.google.com/imghp?hl=es&tab=ri&ogbl');//añadir atributo con valor href
divEnlaces.append(toppingNuevo);//añadimos el nuevo enlace al div seleccionado
console.log(divEnlaces.innerHTML);//comprobar en consola que se ha añadido al divEnlaces

//BORRAR UN ELEMENTO
toppingNuevo.remove();
console.log(divEnlaces);

//////////////////////////////////////////////////////
//onEVENT
function cambiarColor() {
let listaAlbahaca = document.getElementById('albahaca');
listaAlbahaca.style.backgroundColor = "pink";
listaAlbahaca.style.color = "blue";
}

function pasarValores(topp) { //le paso en el li onclick el valor que va a recibir aqui y que lo va a imprimir en consola
    console.log(topp);
}