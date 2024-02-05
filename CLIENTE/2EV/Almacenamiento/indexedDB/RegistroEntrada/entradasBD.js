let db;
let openRequest = indexedDB.open("ControlVisitas", 1);
const fechaHoy = new Date(); 

//se ejecuta solo si hay un cambio de version o si no existe la BBDD
openRequest.onupgradeneeded = function(){
    let db1 = openRequest.result;

    let entradas = db1.createObjectStore('entradas', {keyPath: 'dni'});
    let salidas = db1.createObjectStore('salidas', {autoIncrement: true});

    let indiceEnt = entradas.createIndex('ent_ind', 'apellidos');
    let indiceSal = salidas.createIndex('sal_ind', 'apellidos');
};

openRequest.onerror = function(){
    console.log("Error: "+ openRequest.error);
}; 

openRequest.onsuccess = function(){
    db = openRequest.result;
    console.log("Recogido evento success");
    //PONER AQUI LA FUNCION PARA QUE SAQUE EN LA TABLA LOS DATOS
    mostrarEntradas();
    mostrarSalidas();
};

function registro() {
    console.log("guardar en el almacen de objetos");

    entrada = {
        nombre: $("#nombre").val(),
        apellidos: $("#apellidos").val(),
        dni: $("#dni").val(),
        personaContacto: $("#persContacto").val(),
        fechaEntrada : fechaHoy
    }    

    console.log(entrada.nombre);
    //guardar el objeto en el almacen de la BBDD
    //1. crear una transaccion
    let transac = db.transaction("entradas", "readwrite"); // aqui se pone el nombre que le queremos dar al almacen(tablas)

    //2. obtener el almacén
    let entds = transac.objectStore("entradas");// aqui se pone el nombre que le queremos dar al almacen(tablas)

    //3. añadir al almacen el objeto
    let result = entds.add(entrada);

    //4. gestionar los eventos (exito y error) con el result de la operacion (insercion)
    result.onsuccess = function() { 
        console.log("Nueva entrada agregada", result.result);
      };
      result.onerror = function() {
        console.log("Error", result.error);
      };

}

function limpiar(){
    $("#nombre").val("");
    $("#apellidos").val("");
    $("#dni").val("");
    $("#persContacto").val("")
}

function mostrarEntradas() {
    // (1) Crear una transacción
    let transac2 = db.transaction("entradas", "readonly");

    // (2) Obtener el almacen
    let entds2 = transac2.objectStore("entradas");

    // (3) Recuperar todos los datos del almacen
    let salida = entds2.getAll();

    salida.onsuccess = function() {
        let tabla = $("#salida");

        for( entrada of salida.result){

            let nombre = entrada.nombre;
            let ape = entrada.apellidos;
            let dni = entrada.dni;
            let contacto = entrada.personaContacto;
            let fechaEnt = entrada.fechaEntrada;

            let fila = $("<tr>");

            // Recorrer los resultados y agregar filas a la tabla
            celdaNombre = $("<td>").text(nombre);
            fila.append(celdaNombre); // Añadir la celda a la fila
            celdaApe = $("<td>").text(ape);
            fila.append(celdaApe); // Añadir la celda a la fila
            celdaDni= $("<td>").text(dni);
            fila.append(celdaDni); // Añadir la celda a la fila
            celdaCont= $("<td>").text(contacto);
            fila.append(celdaCont); // Añadir la celda a la fila
            celdaFechaEnt= $("<td>").text(fechaEnt);
            fila.append(celdaFechaEnt); // Añadir la celda a la fila
            celdaFechaSal= $("<td>");
            

            let btnSal = $("<button>");
            btnSal.html("<img  width='30px' src='flecha-derecha.png'/>")
            btnSal.on("click", function(){
                registroSalidas(nombre, ape, dni, contacto, fechaEnt);
                borrarEntrada(dni);
            })
            celdaFechaSal.append(btnSal);

            fila.append(celdaFechaSal); // Añadir la celda a la fila
            tabla.append(fila); // Añadir la fila a la tabla
        }
    }
}

function borrarEntrada(dni){
    let transac = db.transaction("entradas", "readwrite");
    let entrs = transac.objectStore("entradas");
    let request = entrs.getKey(dni);

    request.onsuccess = function(){
        let id = request.result;
        let deleteRequest = entrs.delete(id);
    };
}

function registroSalidas(nombre, apellidos, dni, personaContacto, fechaEntrada) {
    console.log("guardar en el almacen de objetos");

    salida = {
        nombre: nombre,
        apellidos: apellidos,
        dni: dni,
        personaContacto: personaContacto,
        fechaEntrada : fechaEntrada,
        fechaSalida: new Date()
    }    

    console.log(entrada.nombre);
    //guardar el objeto en el almacen de la BBDD
    //1. crear una transaccion
    let transac3 = db.transaction("salidas", "readwrite"); // aqui se pone el nombre que le queremos dar al almacen(tablas)

    //2. obtener el almacén
    let slds = transac3.objectStore("salidas");// aqui se pone el nombre que le queremos dar al almacen(tablas)

    //3. añadir al almacen el objeto
    let result = slds.add(salida);

    //4. gestionar los eventos (exito y error) con el result de la operacion (insercion)
    result.onsuccess = function() { 
        console.log("Nueva entrada agregada", result.result);
      };
      result.onerror = function() {
        console.log("Error", result.error);
      };

}

function mostrarSalidas(){
    // (1) Crear una transacción
    let transac4 = db.transaction("salidas", "readonly");

    // (2) Obtener el almacen
    let salids2 = transac4.objectStore("salidas");

    // (3) Recuperar todos los datos del almacen
    let result = salids2.getAll();

    result.onsuccess = function() {
        let tabla = $("#salida2");

        for( salida of result.result){
            
            let nombre = salida.nombre;
            let ape = salida.apellidos;
            let dni = salida.dni;
            let contacto = salida.personaContacto;
            let fechaEnt = salida.fechaEntrada;
            let fechSal = salida.fechaSalida;

            let fila = $("<tr>");

            // Recorrer los resultados y agregar filas a la tabla
            celdaNombre = $("<td>").text(nombre);
            fila.append(celdaNombre); // Añadir la celda a la fila
            celdaApe = $("<td>").text(ape);
            fila.append(celdaApe); // Añadir la celda a la fila
            celdaDni= $("<td>").text(dni);
            fila.append(celdaDni); // Añadir la celda a la fila
            celdaCont= $("<td>").text(contacto);
            fila.append(celdaCont); // Añadir la celda a la fila
            celdaFechaEnt= $("<td>").text(fechaEnt);
            fila.append(celdaFechaEnt); // Añadir la celda a la fila
            celdaFechaSal= $("<td>").text(fechSal);
            fila.append(celdaFechaSal); // Añadir la celda a la fila
            tabla.append(fila); // Añadir la fila a la tabla
        }
    }  
}

function buscarEntradaPorDNI() {
    let dniUsuario = $("#campoDniEntrada").val();
    mostrarEntradasPorDNI(dniUsuario);
}

function buscarEntradaPorApellidos() {
    let apellidosUsuario = $("#campoApellEntrada").val();
    mostrarEntradasPorApellidos(apellidosUsuario);
}

function buscarSalidaPorDNI() {
    let dniUsuario = $("#campoDniSalida").val();
    mostrarSalidasPorDNI(dniUsuario);
}

function buscarSalidaPorApellidos() {
    let apellidosUsuario = $("#campoApellSalida").val();
    mostrarSalidasPorApellidos(apellidosUsuario);
}

function mostrarEntradasPorDNI(dni) {
    // (1) Crear una transacción
    let transac2 = db.transaction("entradas", "readonly");

    // (2) Obtener el almacén
    let entds2 = transac2.objectStore("entradas");

    // (3) Buscar por clave (DNI)
    let getRequest = entds2.get(dni);

    getRequest.onsuccess = function () {
        let result = getRequest.result;

        if (result) {
            // Si se encuentra la entrada, mostrarla
            let tabla = $("#salida");
            tabla.empty(); // Limpiar la tabla antes de mostrar los resultados

            let fila = $("<tr>");
            celdaNombre = $("<td>").text(result.nombre);
            fila.append(celdaNombre);
            celdaApe = $("<td>").text(result.apellidos);
            fila.append(celdaApe);
            celdaDni = $("<td>").text(result.dni);
            fila.append(celdaDni);
            celdaCont = $("<td>").text(result.personaContacto);
            fila.append(celdaCont);
            celdaFechaEnt = $("<td>").text(result.fechaEntrada);
            fila.append(celdaFechaEnt);
            celdaFechaSal = $("<td>");

            let btnSal = $("<button>");
            btnSal.html("<img  width='30px' src='flecha-derecha.png'/>")
            btnSal.on("click", function () {
                registroSalidas(result.nombre, result.apellidos, result.dni, result.personaContacto, result.fechaEntrada);
                borrarEntrada(result.dni);
            })
            celdaFechaSal.append(btnSal);

            fila.append(celdaFechaSal);
            tabla.append(fila);
        } else {
            console.log("Entrada no encontrada");
        }
    };

    getRequest.onerror = function () {
        console.log("Error al buscar la entrada");
    };
}

function mostrarEntradasPorApellidos(apellidos) {
    // (1) Crear una transacción
    let transac2 = db.transaction("entradas", "readonly");

    // (2) Obtener el almacén
    let entds2 = transac2.objectStore("entradas");

    // (3) Utilizar el índice para buscar por apellidos
    let apeIndice = entds2.index("ent_ind");
    let getRequest = apeIndice.getAllKeys(apellidos);

    getRequest.onsuccess = function () {
        let result = getRequest.result;

        if (result.length > 0) {
            // Si se encuentran entradas, mostrarlas
            let tabla = $("#salida");
            tabla.empty(); // Limpiar la tabla antes de mostrar los resultados

            for (let key of result) {
                let getRequestByKey = entds2.get(key);

                getRequestByKey.onsuccess = function () {
                    let entrada = getRequestByKey.result;
                    let fila = $("<tr>");

                    // Recorrer los resultados y agregar filas a la tabla
                    celdaNombre = $("<td>").text(entrada.nombre);
                    fila.append(celdaNombre);
                    celdaApe = $("<td>").text(entrada.apellidos);
                    fila.append(celdaApe);
                    celdaDni = $("<td>").text(entrada.dni);
                    fila.append(celdaDni);
                    celdaCont = $("<td>").text(entrada.personaContacto);
                    fila.append(celdaCont);
                    celdaFechaEnt = $("<td>").text(entrada.fechaEntrada);
                    fila.append(celdaFechaEnt);
                    celdaFechaSal = $("<td>");

                    let btnSal = $("<button>");
                    btnSal.html("<img  width='30px' src='flecha-derecha.png'/>")
                    btnSal.on("click", function () {
                        registroSalidas(entrada.nombre, entrada.apellidos, entrada.dni, entrada.personaContacto, entrada.fechaEntrada);
                        borrarEntrada(entrada.dni);
                    })
                    celdaFechaSal.append(btnSal);

                    fila.append(celdaFechaSal);
                    tabla.append(fila);
                };
            }
        } else {
            console.log("Entradas no encontradas");
        }
    };

    getRequest.onerror = function () {
        console.log("Error al buscar las entradas");
    };
}

function mostrarSalidasPorDNI(dni) {
    // (1) Crear una transacción
    let transac4 = db.transaction("salidas", "readonly");

    // (2) Obtener el almacén
    let salids2 = transac4.objectStore("salidas");

    // (3) Buscar por clave (DNI)
    let getRequest = salids2.index("sal_ind").get(dni);

    getRequest.onsuccess = function () {
        let result = getRequest.result;

        if (result) {
            // Si se encuentra la salida, mostrarla
            let tabla = $("#salida2");
            tabla.empty(); // Limpiar la tabla antes de mostrar los resultados

            let fila = $("<tr>");
            celdaNombre = $("<td>").text(result.nombre);
            fila.append(celdaNombre);
            celdaApe = $("<td>").text(result.apellidos);
            fila.append(celdaApe);
            celdaDni = $("<td>").text(result.dni);
            fila.append(celdaDni);
            celdaCont = $("<td>").text(result.personaContacto);
            fila.append(celdaCont);
            celdaFechaEnt = $("<td>").text(result.fechaEntrada);
            fila.append(celdaFechaEnt);
            celdaFechaSal = $("<td>").text(result.fechaSalida);
            fila.append(celdaFechaSal);
            tabla.append(fila);
        } else {
            console.log("Salida no encontrada");
        }
    };

    getRequest.onerror = function () {
        console.log("Error al buscar la salida");
    };
}


function mostrarSalidasPorApellidos(apellidos) {
    // (1) Crear una transacción
    let transac4 = db.transaction("salidas", "readonly");

    // (2) Obtener el almacén
    let salids2 = transac4.objectStore("salidas");

    // (3) Utilizar el índice para buscar por apellidos
    let apeIndice = salids2.index("sal_ind");
    let getRequest = apeIndice.getAllKeys(apellidos);

    getRequest.onsuccess = function () {
        let result = getRequest.result;

        if (result.length > 0) {
            // Si se encuentran salidas, mostrarlas
            let tabla = $("#salida2");
            tabla.empty(); // Limpiar la tabla antes de mostrar los resultados

            for (let key of result) {
                let getRequestByKey = salids2.get(key);

                getRequestByKey.onsuccess = function () {
                    let salida = getRequestByKey.result;
                    let fila = $("<tr>");

                    // Recorrer los resultados y agregar filas a la tabla
                    celdaNombre = $("<td>").text(salida.nombre);
                    fila.append(celdaNombre);
                    celdaApe = $("<td>").text(salida.apellidos);
                    fila.append(celdaApe);
                    celdaDni = $("<td>").text(salida.dni);
                    fila.append(celdaDni);
                    celdaCont = $("<td>").text(salida.personaContacto);
                    fila.append(celdaCont);
                    celdaFechaEnt = $("<td>").text(salida.fechaEntrada);
                    fila.append(celdaFechaEnt);
                    celdaFechaSal = $("<td>").text(salida.fechaSalida);
                    fila.append(celdaFechaSal);
                    tabla.append(fila);
                };
            }
        } else {
            console.log("Salidas no encontradas");
        }
    };

    getRequest.onerror = function () {
        console.log("Error al buscar las salidas");
    };
}