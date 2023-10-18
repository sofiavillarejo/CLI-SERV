//lo sobjetos se declaran como constantes porque no se modifican
//pero los atributos si
//sin embargo, si el objeto se declara como let, se puede modificar después y el primero desaparecería
const persona = {
	nombre: "Federico",
	apellidos: "García Lorca",
	edad: 55,
	nacionalidad: "española"
}
alert(persona.nombre);

persona.nombre = "El Fede"; //aquí se modifica el atributo nombre
persona.apodo = "El Federius";//los atributos se pueden crear de forma dinamica sin ser declarados en el objeto
alert(persona.nombre);
alert(persona.apodo);