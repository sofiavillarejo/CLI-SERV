let dbai;

let openRequestai = indexedDB.open("BDAutoincrementada",1);

openRequestai.onupgradeneeded = function() {
    let db1 = openRequestai.result;
    //crear almacenes, claves, indices
    //solo se puede aqui
    db1.createObjectStore('libros', {autoIncrement: true});
};

openRequestai.onerror = function() {
  console.error("Error", openRequestai.error);
};

openRequestai.onsuccess = function() {
  dbai = openRequestai.result;
  console.log("Recogido evento success")
};

function guardaBDautoIncrementada(){
  console.log("guardar en el almacen de objetos")
  
  //recuperar los datos
  //generar un objeto para guardar
  libro = {
    id: document.getElementById("idai").value,
    titulo: document.getElementById("tituloai").value,
    autor: document.getElementById("autorai").value,
    tipo: document.getElementById("tipoai").value
  }


  // guardar el objeto en el almacen de la base de datos

  //(1) crear una transaccion
  let transac = dbai.transaction("libros", "readwrite");

  //(2) obtener el almacen
  let lbrs = transac.objectStore("libros"); 

  //(3) aÃ±adir al almacen el objeto
  let resultado = lbrs.add(libro);

  //(4) gestionar los eventos (exito y error) con el resultado de la operacÃ­Ã³n (inserciÃ³n)
  resultado.onsuccess = function() { 
    console.log("Libro agregado al almacÃ©n", resultado.result);
  };
  resultado.onerror = function() {
    console.log("Error", resultado.error);
  };

}