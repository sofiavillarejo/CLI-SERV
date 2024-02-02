let db;
let openRequest = indexedDB.open("ControlVisitas", 1);

//se ejecuta solo si hay un cambio de version o si no existe la BBDD
openRequest.onupgradeneeded = function(){
    let db1 = openRequest.result;

    let entradas = db1.createObjectStore('entradas', {keyPath: 'dni'});
    let salidas = db1.createObjectStore('salidas', {keyPath: 'dni'});

    let indiceEnt = entradas.createIndex('ent_ind', 'apellidos');
    let indiceSal = salidas.createIndex('sal_ind', 'apellidos');

};

openRequest.onerror = function(){
    console.log("Error: "+ openRequest.error);
}; 

openRequest.onsuccess = function(){
    db = openRequest.result;
    console.log("Recogido evento success");
};

function registro() {
    console.log("guardar en el almacen de objetos");

    entrada = {
        nombre: $("#nombre").val(),
        apellidos: $("#apellidos").val(),
        dni: $("#dni").val(),
        personaContacto: $("#persContacto").val()
    }    
    console.log(entrada.nombre);
    //guardar el objeto en el almacen de la BBDD
    //1. crear una transaccion
    let transac = db.transaction("entradas", "readwrite"); // aqui se pone el nombre que le queremos dar al almacen(tablas)

    //2. obtener el almacén
    let entds = transac.objectStore("entradas");// aqui se pone el nombre que le queremos dar al almacen(tablas)

    //3. añadir al almacen el objeto
    let resultado = entds.add(entrada);

    //4. gestionar los eventos (exito y error) con el resultado de la operacion (insercion)
    resultado.onsuccess = function() { 
        console.log("Nueva entrada agregada", resultado.result);
      };
      resultado.onerror = function() {
        console.log("Error", resultado.error);
      };

      //RECARGAR LA BASE DE DATOS SIEMPRE!!!!! DESDE LA CONSOLA EN LA RUEDECITA DE REFRESCAR QUE HAY!!!!
}