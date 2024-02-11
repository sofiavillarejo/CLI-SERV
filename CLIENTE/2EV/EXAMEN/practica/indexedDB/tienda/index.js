let db;
$(document).ready(function () {
    //crear bbdd
    let openRequest = indexedDB.open('Tienda', 1);

    //lo que sicede cuando se actualiza la BBDD
    openRequest.onupgradeneeded = function() {
        //crear almacen
        let db = openRequest.result;

        let prods = db.createObjectStore('productos', {keyPath: "id", autoIncrement:true});
        //crear indice de busqueda
        let indice = prods.createIndex('nom_ind', 'nombre');
    };
    //manejo de errores que pueden surgir cuando abro la bbdd
    openRequest.onerror = function() {
        console.error("Error", openRequest.error);
    };
    //lo que sucede cuando la BBDD se abre corectamente
    openRequest.onsuccess = function(){
        db = openRequest.result;
        console.log(db);
        //una vez que este abierta la base de datos, se ejecutara la funcion de lista la información
        // listarAlmacenes();//onsuccess
    };
});

function añadirAbd() { 
    //crear el objeto que almacena los datos pasados por el form del html
    // let producto = {
    //     nombre:  $("#prod").val(),
    //     cantidad:  $("#cant").val()
    // };
    //otra forma de insertar
    let nom = $("#prod").val();
    let cant = $("#cant").val();
    

    //guardar el objeto en el almacen

    //1. crear transaccion
    let transac = db.transaction("productos", "readwrite");
    
    //2. obtener el almacén
    let almacenProd = transac.objectStore("productos");

    //3. añadir al almacen el objeto

    // let resultado = almacenProd.add(producto);
    //lo de arriba es lo mismo que esto
    almacenProd.add({
        nombre: nom,
        cantidad: cant
    })

    //borrar texto del input
    nom = $("#prod").val("");
    cant = $("#cant").val("");

    // //4. gestionar los eventos (exito y error) con el resultado de la operacion (insercion)
    // resultado.onsuccess = function() { 
    //     console.log("Producto agregado al almacen", resultado.result);
    // };
    // resultado.onerror = function() {
    //     console.log("Error", resultado.error);
    // };
}

function añadirProdAtabla(){
    //(1) crear una transaccion
    let transac = db.transaction("productos", "readonly");
    //(2) obtener el almacen
    let almacenProd = transac.objectStore("productos");

    //(3) recuperar todos los datos del almacen
    let salida = almacenProd.getAll();

    salida.onsuccess = function() {
        producto = salida.result;

        // Crear la tabla y encabezados
        let tabla = $("<table border='1'>");
        let filaEncabezados = $("<tr>");

        // Recorrer las propiedades (claves) del primer producto para obtener los encabezados
        for (let key in producto[0]) {
            console.log(key);
            // Añadir a la fila un encabezado para cada clave
            filaEncabezados.append(`<th>${key}</th>`);
        }
        filaEncabezados.append(`<th>Borrar</th><th>Modificar</th>`);

        // Agregar fila con encabezados a la tabla
        tabla.append(filaEncabezados);

        // Agregar datos de cada producto a la tabla
        for (prod of producto) {
            let produc = prod.nombre;
            let cant = prod.cantidad;
            let id = prod.id;

            let filaDatos = $("<tr>");

            let celdaId = $("<td>").text(id);
            let celdaProd = $("<td>").text(produc);
            let celdaCant = $("<td>").text(cant);

            let celdaBorrar = $("<td>");

            let btnBorrar = $("<input type='button' value='Borrar' onclick='borrarProd("+id+")'>");

            celdaBorrar.append(btnBorrar);

            let celdaMod = $("<td>");

            let btnMod = $("<input type='button' value='Modificar' onclick='modificarProducto("+id+")'>");
            celdaMod.append(btnMod);

            filaDatos.append(celdaProd, celdaCant,celdaId, celdaBorrar, celdaMod);
            tabla.append(filaDatos);
        }
        
        // Vaciar el contenedor y agregar la tabla
        $("#contenedor").empty().append(tabla);
    }
}


function borrarProd(id) {
    // Comenzar una transacción en modo de escritura
    let transac = db.transaction("productos", "readwrite");
    
    // Obtener el almacén de objetos
    let prods = transac.objectStore("productos");

    let eliminar = prods.delete(id);

    eliminar.onsuccess = function(){
        console.log("borrado");
    };
    eliminar.onerror = function(){
        console.log("error")
    };
    añadirProdAtabla();
}

function modificarProducto(id){
    // Comenzar una transacción en modo de escritura
    let transac = db.transaction("productos", "readwrite");
    
    // Obtener el almacén de objetos
    let prods = transac.objectStore("productos");

    // Obtener el producto con el ID especificado
    let existeProd = prods.get(id);

    existeProd.onsuccess = function(event){
        // Obtener el producto desde el evento
        let prod = event.target.result;

        // Actualizar las propiedades del producto con los nuevos valores de los campos del formulario
        prod.nombre = $("#prod").val(); // Obtener el nuevo valor del nombre del producto desde el campo con el ID "prod" en el formulario
        prod.cantidad = $("#cant").val();

        // Actualizar el producto en el almacén de objetos utilizando el método 'put()'
        prods.put(prod);

        // Llamar a la función para añadir el producto a la tabla después de modificarlo
        añadirProdAtabla();

    }

}

function limpiarAlmacen() {  
    //(1) crear una transaccion
    let transac = db.transaction("productos", "readwrite");
    //(2) obtener el almacen
    let prods = transac.objectStore("productos");

    //(3) recuperar todos los datos del almacen
    let salida = prods.getAll();

    salida.onsuccess = function() {
        prods.clear();
        $("table").empty();
    }
}

//ES IGUAL QUE EN LISTAR PERO SE METE LA LINEA DEL INDICE Y EN RES, SE METE EL CAMPO DEL INPUT FILTRAR
function buscarPorNombre() {
    // Comenzar una transacción en modo de solo lectura
    let transac = db.transaction("productos", "readonly");
    
    // Obtener el almacén de objetos
    let prods = transac.objectStore("productos");

    // Obtener el índice
    let indice = prods.index("nom_ind");

    // Obtener todos los elementos que coincidan con el nombre proporcionado
    let res = indice.getAll($("#nombre").val());

    res.onsuccess = function() {
        producto = res.result;

        // Crear la tabla y encabezados
        let tabla = $("<table border='1'>");
        let filaEncabezados = $("<tr>");

        // Recorrer las propiedades (claves) del primer producto para obtener los encabezados
        for (let key in producto[0]) {
            console.log(key);
            // Añadir a la fila un encabezado para cada clave
            filaEncabezados.append(`<th>${key}</th>`);
        }
        filaEncabezados.append(`<th>Borrar</th><th>Modificar</th>`);

        // Agregar fila con encabezados a la tabla
        tabla.append(filaEncabezados);

        // Agregar datos de cada producto a la tabla
        for (prod of producto) {
            let produc = prod.nombre;
            let cant = prod.cantidad;
            let id = prod.id;

            let filaDatos = $("<tr>");

            let celdaId = $("<td>").text(id);
            let celdaProd = $("<td>").text(produc);
            let celdaCant = $("<td>").text(cant);

            let celdaBorrar = $("<td>");

            let btnBorrar = $("<input type='button' value='Borrar' onclick='borrarProd("+id+")'>");

            celdaBorrar.append(btnBorrar);

            let celdaMod = $("<td>");

            let btnMod = $("<input type='button' value='Modificar' onclick='modificarProducto("+id+")'>");
            celdaMod.append(btnMod);

            filaDatos.append(celdaProd, celdaCant,celdaId, celdaBorrar, celdaMod);
            tabla.append(filaDatos);
        }
        
        // Vaciar el contenedor y agregar la tabla
        $("#contenedor").empty().append(tabla);
    }
}
