let db;

let openRequest = indexedDB.open("miBaseDeDatos",1);

openRequest.onupgradeneeded = function() {

};

openRequest.onerror = function() {
  console.error("Error", openRequest.error);
};

openRequest.onsuccess = function() {
  db = openRequest.result;
  console.log("Recogido evento success");
  listar();
};

function listar(){
  //(1) crear una transaccion
  let transac = db.transaction("libros", "readonly");

  //(2) obtener el almacen
  let lbrs = transac.objectStore("libros");

  //(3) recuperar todos los datos del almacen
  let salida = lbrs.getAll(IDBKeyRange.bound("0", "1",false,true));

  salida.onsuccess = function() {
    

    let tabla = document.getElementById('salida');

    libro=salida.result;

    for( libro of salida.result){
      let fila = document.createElement("tr"); //crear la fila

      let celdaId = document.createElement("td"); //crear la celda 
      celdaId.appendChild(document.createTextNode(libro.id)); //rellenar la celda
      
      fila.appendChild(celdaId); //añadir la celda a la fila

      let celdaTitulo = document.createElement("td"); //crear la celda 
      celdaTitulo.appendChild(document.createTextNode(libro.titulo)); //rellenar la celda
      
      fila.appendChild(celdaTitulo); //añadir la celda a la fila

      let celdaAutor = document.createElement("td"); //crear la celda 
      celdaAutor.appendChild(document.createTextNode(libro.autor)); //rellenar la celda
      
      fila.appendChild(celdaAutor); //añadir la celda a la fila

      let celdaTipo = document.createElement("td"); //crear la celda 
      celdaTipo.appendChild(document.createTextNode(libro.tipo)); //rellenar la celda
      
      fila.appendChild(celdaTipo); //añadir la celda a la fila


      tabla.appendChild(fila);

    }
  }
  //buscar por clave
  let res = lbrs.getKey("0");

  res.onsuccess = function() {
    console.log(res.result);
  }

  //transaccion con el indice
  let tituloIndice = lbrs.index("titulo_ind"); //busco el indice en el almacen (lbrs)
  //ejecutar consultas sobre el indice --> devuelve las claves en un array
  let res1 = tituloIndice.getKey("mi libro"); //devuelve el primero que encuentre, si hay mas solo devuelve el primero
  let res2 = tituloIndice.getAllKeys("mi libro");

  res1.onsuccess = function(){
    console.log(res1.result); //me devuelve la primaryKey a traves del indice
}
  res2.onsuccess = function(){
    console.log(res2.result); //me devuelve todas las claves que tienen de titulo "mi libro"
    //recorro el resultado
    for( keylibro of res2.result){
        console.log(lbrs.get(keylibro));
    }
}
  //borrar --> delete
}