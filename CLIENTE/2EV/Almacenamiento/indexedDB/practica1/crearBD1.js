let db;

$(inicio); //onload

// esta funcion se lanza con el eveto onload
function inicio(){
    let openRequest = indexedDB.open("miBaseDeDatos", 1);

    //se ejecuta solo si hay un cambio de version o si no existe la BBDD
    openRequest.onupgradeneeded = function(){
        let db = openRequest.result;
        //crear almacenes, claves, indices (solo se puede aqui)
        let libros = db.createObjectStore('libros', {keyPath: 'id'});
        //crear indice--> se debe borrar la base de datos en la consola para cualquier cambio que se haga --> se usa en listarBD
        let indTitulo = libros.createIndex('titulo_ind', 'titulo');//me permite buscar por el campo titulo
    };

    openRequest.onerror = function(){
        console.log("Error: "+ openRequest.error);
    }; 

    openRequest.onsuccess = function(){
        db = openRequest.result;
        console.log("Recogido evento success");
        //una vez que este abierta la base de datos, se ejecutara la funcion de lista la información
        // listarAlmacenes();//onsuccess
    };
}
function guardaBD() {
    console.log("guardar en el almacen de objetos");
    //recuperar los datos
    //usar mejor JQuery
    //generar un objeto para guardar
    libro = {
        id: document.getElementById("id").value,
        titulo: document.getElementById("titulo").value,
        autor: document.getElementById("autor").value,
        tipo: document.getElementById("tipo").value
        // miLibro: libro //se mete el objeto a sí mismo
    }
    console.log(libro);
    
    //guardar el objeto en el almacen de la BBDD
    //1. crear una transaccion
    let transac = db.transaction("libros", "readwrite"); //si pogno ["libros"]--> bloqueo la BBDD (no se para que sirve)

    //2. obtener el almacén
    let lbrs = transac.objectStore("libros");

    //3. añadir al almacen el objeto
    let resultado = lbrs.add(libro);

    //4. gestionar los eventos (exito y error) con el resultado de la operacion (insercion)
    resultado.onsuccess = function() { 
        console.log("Libro agregado al almacen", resultado.result);
    };
    resultado.onerror = function() {
        console.log("Error", resultado.error);
    };

      //RECARGAR LA BASE DE DATOS SIEMPRE!!!!! DESDE LA CONSOLA EN LA RUEDECITA DE REFRESCAR QUE HAY!!!!
}
