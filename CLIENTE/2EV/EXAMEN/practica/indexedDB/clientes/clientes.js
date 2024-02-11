let db;
$(function () {
     //crear bbdd
    let openRequest = indexedDB.open('Cliente', 1);

    //lo que sicede cuando se actualiza la BBDD
    openRequest.onupgradeneeded = function() {
        //crear almacen
        let db = openRequest.result;

        let clientes = db.createObjectStore('clientes', {keyPath: "id", autoIncrement:true});
        //crear indice de busqueda
        let indice = clientes.createIndex('nom_ind', 'nombre');
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
        listar();
    };
});

function guardarCliente() {
    let id = $("#id").val();
    let nom = $("#nombre").val();
    let apellido = $("#ape").val();
    let edad = $("#edad").val();

    //para que no se dejen los campos vacios
    if(nom == "" || apellido == "" || edad == "" )

    return alert("no se pueden dejar los campos vacíos");
    //guardar el objeto en el almacen

    //1. crear transaccion
    let transac = db.transaction("clientes", "readwrite");
    
    //2. obtener el almacén
    let almacenCli = transac.objectStore("clientes");

    //3. añadir al almacen el objeto

    // let resultado = almacenProd.add(producto);
    //lo de arriba es lo mismo que esto
    let resultado = almacenCli.add({
        id : id,
        nombre: nom,
        ape: apellido, 
        edad: edad
    })

    //vaciar los campos una vez se ha insertado el cliente
    nom = $("#nombre").val("");
    apellido = $("#ape").val("");
    edad = $("#edad").val("");
        
    //manejo de posibles errores
    resultado.onsuccess = function() { 
        console.log("Cliente agregado al almacen", resultado.result);
    };
    resultado.onerror = function() {
        console.log("Error", resultado.error);
    };

    listar();

}

function listar() {
    //(1) crear una transaccion
    let transac = db.transaction("clientes", "readonly");

    //(2) obtener el almacen
    let clientes = transac.objectStore("clientes");

    //(3) recuperar todos los datos del almacen
    let salida = clientes.getAll();

    salida.onsuccess = function() {
        cliente = salida.result;
        console.log(cliente);
        // Crear la tabla y encabezados
        let lista = $("#lista");
        $("#lista").empty().append(lista);

        // for( cli of salida.result){
        //     let listElem = $("<li>");

        //     for (const clave in cli) {
        //         listElem.append(`<b>${clave}: </b> ${cli[clave]} `);
        //     }

        //     lista.append(listElem);
        // }
        for (cli of cliente) {
            let name = cli.nombre;
            let apell = cli.ape;
            let ed = cli.edad;

            lista.append("<li>Nombre: "+ name + "<br>" + "Apellido: "+apell+ "<br>" + "Edad: "+ed+ "<br>" + "</li><hr>");

        }



    }
}

//funcion que borra todo los datos del almacen
function limpiarCliente(){
    //(1) crear una transaccion
    let transac = db.transaction("clientes", "readwrite");
    //(2) obtener el almacen
    let clientes = transac.objectStore("clientes");

    //(3) recuperar todos los datos del almacen
    let datos = clientes.getAll();
    console.log(datos);
    datos.onsuccess = function() {
        clientes.clear();
        $("#lista").empty();
    }
}

//NO FUNCIONA POR EL ID, LO SACA PERO PARA QUE LO BORRE HAY QUE PONER EL ID PASANDOSELO AQUI
function borrarCliente() {
    let id = $("#id").val();

    console.log("ID del cliente a borrar:", id);

    // Comenzar una transacción en modo de escritura
    let transac = db.transaction("clientes", "readwrite");
    
    // Obtener el almacén de objetos
    let clints = transac.objectStore("clientes");
    
    // Eliminar el cliente usando su ID
    let deleteRequest = clints.delete(7); //LE PASAMOIS EL ID PARA QUE FUNCIONE

    // Manejar el resultado de la solicitud de eliminación
    deleteRequest.onsuccess = function() {
        console.log("Cliente eliminado correctamente");
        listar(); // Actualizar la lista después de borrar un cliente
    };

    // Manejar errores en la solicitud de eliminación del cliente
    deleteRequest.onerror = function() {
        console.error("Error al intentar eliminar el cliente:", deleteRequest.error);
    };
}

function modificarCliente() {
    // Obtener el ID del cliente a modificar
    const id = $("#id").val();

    // Iniciar una transacción en modo de lectura/escritura
    let transaction = db.transaction("clientes", "readwrite");

    // Obtener el almacén de objetos para clientes
    let almacenCli = transaction.objectStore("clientes");

    // Obtener el cliente que se desea modificar
    let getRequest = almacenCli.get(id);

    // Manejar el éxito de la solicitud de obtención del cliente
    getRequest.onsuccess = function(event) {
        // Obtener el cliente desde el evento
        let cliente = event.target.result;
        console.log(cliente);
        // Verificar si se encontró el cliente
        if (cliente) {
            // Actualizar los campos del cliente con los nuevos valores del formulario
            cliente.nombre = $("#nombre").val();
            cliente.ape = $("#ape").val();
            cliente.edad = $("#edad").val();

            // Actualizar el cliente en el almacén de objetos
            let updateRequest = almacenCli.put(cliente);

            // Manejar el éxito de la solicitud de actualización
            updateRequest.onsuccess = function() {
                console.log("Cliente modificado correctamente");
                listar(); // Actualizar la lista después de modificar el cliente
            };

            // Manejar errores en la solicitud de actualización del cliente
            updateRequest.onerror = function() {
                console.error("Error al intentar modificar el cliente:", updateRequest.error);
            };
        } else {
            console.error("No se encontró ningún cliente con el ID proporcionado");
        }
    };

    // Manejar errores en la solicitud de obtención del cliente
    getRequest.onerror = function() {
        console.error("Error al intentar obtener el cliente:", getRequest.error);
    };
}
