let db;
$(document).ready(function () {
    //crear bbdd
    let openRequest = indexedDB.open('Biblioteca', 1);

    openRequest.onupgradeneeded = function() {
        //crear almacen
        let db1 = openRequest.result;

        let libros = db1.createObjectStore('libros', {keyPath: 'id'});
        //crear indice de busqueda
        let indice = libros.createIndex('precio_ind', 'precio');
    };

    openRequest.onerror = function() {
        console.error("Error", openRequest.error);
    };
    
    openRequest.onsuccess = function(){
        db = openRequest.result;
        console.log(db);
        //una vez que este abierta la base de datos, se ejecutara la funcion de lista la información
        // listarAlmacenes();//onsuccess
    };
    
    
});

function registrarLibro() {  
    //crear el objeto que almacena los datos pasados por el form del html
    let libro = {
        id: $("#id").val(),
        titulo:  $("#titulo").val(),
        precio:  $("#precio").val(),
        creado: new Date()
    };
    console.log(libro);

    //guardar el objeto en el almacen

    //1. crear transaccion
    let transac = db.transaction("libros", "readwrite");
    
    //2. obtener el almacén
    let libros = transac.objectStore("libros");

    //3. añadir al almacen el objeto
    let resultado = libros.add(libro);

    //4. gestionar los eventos (exito y error) con el resultado de la operacion (insercion)
    resultado.onsuccess = function() { 
        console.log("Libro agregado al almacen", resultado.result);
    };
    resultado.onerror = function() {
        console.log("Error", resultado.error);
    };
    //operación terminada: RECARGAR LA BASE DE DATOS SIEMPRE!
}

function añadirLibroAlista(){
    //(1) crear una transaccion
    let transac = db.transaction("libros", "readonly");
    //(2) obtener el almacen
    let libros = transac.objectStore("libros");

    //(3) recuperar todos los datos del almacen
    let salida = libros.getAll();

    salida.onsuccess = function() {
    
        libro=salida.result;

        let lista = $("#lista");

        for( lbr of salida.result){
            let listElem = $("<li>");

            for (const clave in lbr) {
                listElem.append(`<b>${clave}: </b> ${lbr[clave]} `);
            }

            lista.append(listElem);
        }
    }

}

function añadirLibroAtabla(){
    //(1) crear una transaccion
    let transac = db.transaction("libros", "readonly");
    //(2) obtener el almacen
    let libros = transac.objectStore("libros");

    //(3) recuperar todos los datos del almacen
    let salida = libros.getAll();

    salida.onsuccess = function() {
    
        libro=salida.result;
        //saca el primer libro guardado
        console.log(libro[0]);

       // Crear la tabla y encabezados
        let tabla = $("<table border='1'>");
        let fila = $("<tr>");

        //recorrer las propiedades (claves) del primer libro
        for (let key in libro[0]) {
            console.log(key);
            //añadir a la fila un encabezado para cada clave
            fila.append(`<th>${key}</th>`);
        }
        //agregar fila con encabezados a la tabla
        tabla.append(fila);

        // Agregar datos de cada libro a la tabla
        for (let lbr of libro) {
            //crear una nueva fila para cada libro
            let fila = $("<tr>");
            //bucle que trae los valores dentro de cada libro y los mete en celdas
            for (let valor in lbr) {
                fila.append(`<td>${lbr[valor]}</td>`);
            }
            //añadir fila con las celdas a la tabla
            tabla.append(fila);
        }

        // Agregar la tabla al html
        
        tabla.empty();
        $("html").append(tabla);
        actualizarListaYTabla();
    }
}

function limpiarAlmacen() {  
    //(1) crear una transaccion
    let transac = db.transaction("libros", "readwrite");
    //(2) obtener el almacen
    let libros = transac.objectStore("libros");

    //(3) recuperar todos los datos del almacen
    let salida = libros.getAll();

    salida.onsuccess = function() {
        libros.clear();
        $("ul").empty();
        $("table").empty();
    }
}

function modificarLibro() {
    //crear transaccion
    let transaction = db.transaction("libros", "readwrite"); // (1)

    // obtiene un almacén de objetos para operar con él
    let libros = transaction.objectStore("libros"); // (2)

    //obtener valores de los campos del formulario
    const id = $("#id").val();
    const titulo = $("#titulo").val(); // Obtener el título del formulario
    const precio = $("#precio").val(); // Obtener el precio del formulario

    // Obtener el registro que deseas modificar
    let libroAmodificar = libros.get(id);

    libroAmodificar.onsuccess = function(event) {
        let existeLibro = event.target.result;

        // Verificar si se encontró un registro con el título especificado
        if (existeLibro) {
            // Modificar los campos necesarios
            existeLibro.titulo = titulo;
            existeLibro.precio = precio;
            existeLibro.creado = new Date();

            // Actualizar el registro modificado
            let actualizarLibro = libros.put(existeLibro);

            actualizarLibro.onsuccess = function() {
                console.log("Libro modificado en el almacén");
                actualizarListaYTabla();

            };

            actualizarLibro.onerror = function() {
                console.log("Error al modificar el libro", actualizarLibro.error);
            };
        } else {
            console.log("No se encontró ningún libro con el título especificado");
        }
    };

    libroAmodificar.onerror = function() {
        console.log("Error al obtener el libro", libroAmodificar.error);
    };

}

//FUNCION PARA ACTUALIZAR LA TABLA Y LA LISTA UNA VEZ HE MODIFICADO ALGÚN CAMPO DEL LIBRO
function actualizarListaYTabla() {
    // Limpiar la lista y la tabla existentes
    $("#lista").empty();
    $("table").empty();

    // Volver a añadir los libros a la lista y la tabla
    añadirLibroAlista();
    añadirLibroAtabla();
}

function borrarLibro() {  
    // Comenzar una transacción en modo de escritura
    let transaction = db.transaction("libros", "readwrite");
    
    // Obtener el almacén de objetos
    let libros = transaction.objectStore("libros");

    //obtener valores de los campos del formulario
    const id = $("#id").val();

    // Eliminar el libro por su ID
    let borrarLibro = libros.delete(id);

    // Manejar el éxito o el error de la operación
    borrarLibro.onsuccess = function () {  
        console.log("Libro borrado exitosamente");
        // Actualizar la lista y la tabla después de borrar el libro
        actualizarListaYTabla();
    };

    borrarLibro.onerror = function () {  
        console.error("Error al borrar el libro", borrarLibro.error);
    };
}
