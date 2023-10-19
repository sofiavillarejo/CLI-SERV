//lo sobjetos se declaran como constantes porque no se modifican
//pero los atributos si
//sin embargo, si el objeto se declara como let, se puede modificar después y el primero desaparecería
const persona = {
	nombre: "Federico",
	apellidos: "García Lorca",
	edad: 55,
	nacionalidad: "española",
	//DENTRO DE LOS OBJETOS PUEDE HABER METODOS
	datosCompletos: function () {
		alert(this.nombre + " - " + this.apellidos + " - " + this.edad);
	}
}

alert(persona.nombre);

persona.nombre = "El Fede"; //aquí se modifica el atributo nombre
persona.apodo = "El Federius";//los atributos se pueden crear de forma dinamica sin ser declarados en el objeto
/*
alert(persona.nombre);
alert(persona.apodo);
persona.datosCompletos();

const persona1 = new Object(); //creamos un objeto vacio que se puede rellenar luego
persona1.nombre = "Jose";
persona1.apellidos = "Garcia";

const persona2 = persona1;

persona2.nombre = "Josete";

alert(persona1.nombre);
*/
//saca los atributos
for (let variable in persona){
	console.log(variable);//saca el nombre de los atributos
	console.log(persona[variable]);//saca el contenido de los atributos
}
delete persona.apodo;
console.log(persona);

const myObj = {
  name: "John",
  age: 30,
  cars: [
    {name:"Ford", models:["Fiesta", "Focus", "Mustang"]},
    {name:"BMW", models:["320", "X3", "X5"]},
    {name:"Fiat", models:["500", "Panda"]}
  ]
}
console.log(myObj.cars[0]); //saca el modelo que hay en la posicion 0 del atributo coches
//imprimir todos los modelos
for ( let modelo of myObj.cars[0].models){
	console.log(modelo);
}

function verElemento(elem){
		elem.style.display = "none";
		console.log(elem);
}

const person = {
  name: "John",
  age: 30,
  city: "New York"
};

let myString = JSON.stringify(person);
document.getElementById("parrafo").innerHTML = myString;
