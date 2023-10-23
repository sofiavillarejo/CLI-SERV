//asi se define un constructor
function Persona(nom,apell,ed,nac) {
	this.nombre = nom;
	this.apellidos = apell;
	this.edad = ed;
	this.nacionalidad = nac
	//ESTA FORMA DE MOSTRAR ES LO MISMO QUE PERSONA2.VERDATOS 
	this.dimeLaEdad = function(){
		return "Mi edad es " + this.edad;
	}
}
const persona2 = new Persona("Federico","Garcia Lorca", 55, "Española");

persona2.verDatos = function () {
	return this.nombre + " " + this.apellidos;
}

//lo sobjetos se declaran como constantes porque no se modifican
//pero los atributos si
//sin embargo, si el objeto se declara como let, se puede modificar después y el primero desaparecería
/*
const persona = {
	nombre: "Federico",
	apellidos: "García Lorca",
	edad: 55,
	nacionalidad: "española",
	//DENTRO DE LOS OBJETOS PUEDE HABER METODOS
	datosCompletos: function () { //funcion anonima
		//devuelve los atributos seleccionados
		return this.nombre + " - " + this.apellidos + " - " + this.edad;//dentro de un metodo del objeto se usa el this siempre
	}
}
*/
function verPersona(){
	//document.getElementById('salida').innerHTML = persona.datosCompletos();
	//document.getElementById('salida2').innerHTML = persona;//imprime [object]
	/*
	let texto = "";

	for(let propi in persona){
		//texto += propi+"-";
		texto += "<li>" + persona[propi]+"</li>";
	*/
	//persona.datosCompletos = persona.datosCompletos.toString();
	}
	//document.getElementById('salida').innerHTML = texto;
	//document.getElementById('salida').innerHTML = JSON.stringify(persona);// convierte los atributos a JSON, pero no las funciones

//persona.dimeLaEdad = function(){return "Mi edad es " + this.edad;}
//document.getElementById('salida').innerHTML = JSON.stringify(persona2);
document.getElementById('salida').innerHTML = persona2.verDatos();


//crear metodos una vez creado el objeto

persona2.dimeLaEdad = function(){
	return "mi edad es " + this.edad;
}
function verEdad() {
	document.getElementById('salida').innerHTML = persona2.dimeLaEdad();
}

 //w3schools
//HEMOS VISTO LOS GETTER Y SETTER
//JS OBJECT ACCESORS 
//oBJECT pROTOTYPE
//ITERABLES
//OBJECT SETS (CONJUNTOS) --> FOREACH() METHOD
//OBJECTS MAPS

/*
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
*/