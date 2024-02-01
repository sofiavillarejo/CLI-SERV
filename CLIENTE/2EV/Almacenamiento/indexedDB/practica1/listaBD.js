let db;
let openRequest = indexedDB.open("miBaseDeDatos", 1);

//se ejecuta solo si hay un cambio de version o si no existe la BBDD
openRequest.onupgradeneeded = function(){
    let db1 = openRequest.result;
    //crear almacenes, claves, indices (solo se puede aqui)
    db1.createObjectStore('libros', {keyPath: 'id'});
};

openRequest.onerror = function(){
    console.log("Error: "+ openRequest.error);
}; 

openRequest.onsuccess = function(){
    db = openRequest.result;
    console.log("Recogido evento success");
    listar();
};

//hasta aqui hemos abierto la BBDD
function listar(){
    //1. traer la transaccion
    let transac = db.transaction("libros", "readonly"); //solo leer

    //2. obtener el almacén
    let lbrs = transac.objectStore("libros");

    //(3) recuperar todos los datos del almacen
    let salida = lbrs.getAll();

    console.log(salida);

    salida.onsuccess = function() {
    console.log(salida);
  }

}
