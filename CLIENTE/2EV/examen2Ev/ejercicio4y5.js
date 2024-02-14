//crear variable para usar
let db;

$(inicio); //onload

// esta funcion se lanza con el eveto onload
function inicio(){
    //abrir la BBDD
    let openRequest = indexedDB.open("notasAlumno", 1);

    //se ejecuta solo si hay un cambio de version o si no existe la BBDD
    openRequest.onupgradeneeded = function(){
        let db = openRequest.result;
        //crear almacenes, claves, indices (solo se puede aqui)
        let almacenAlumnos = db.createObjectStore('alumnos', {keyPath: 'nombre'});
        //crear indice--> se debe borrar la base de datos en la consola para cualquier cambio que se haga --> se usa en listarBD
        let indCiclo = almacenAlumnos.createIndex('ciclo_ind', 'ciclo');//me permite buscar por el campo ciclo
    };
    //manejo de errores
    openRequest.onerror = function(){
        console.log("Error: "+ openRequest.error);
    }; 
    //si todo esta bien, es lo que se ejecuta
    openRequest.onsuccess = function(){
        db = openRequest.result;
        console.log("Recogido evento success");
        //una vez que este abierta la base de datos, se ejecutara la funcion de guardarBD()
        guardaBD();

    };

}

//añadir registros a BBDD
function guardaBD() {
    console.log("guardar en el almacen de objetos");
    //recuperar los datos
    //usar mejor JQuery
    //generar un objeto para guardar
    let alumno = {
            nombre: "Jorge",
            idMatricula: "DAW246",
            modulo: "Despliegue",
            ciclo: "DAW",
            nota: 7
        };
    let alumno2 = {
        nombre: "Maria",
        idMatricula: "TEAS357",
        modulo: "Medio natural",
        ciclo: "Teas",
        nota: 8
    };
    console.log(alumno, alumno2);
    
    //guardar el objeto en el almacen de la BBDD
    //1. crear una transaccion
    let transac = db.transaction("alumnos", "readwrite"); //si pogno ["alumnos"]--> bloqueo la BBDD (no se para que sirve)

    //2. obtener el almacén
    let almacenAlu = transac.objectStore("alumnos");

    //3. añadir al almacen el objeto
    almacenAlu.add(alumno);
    almacenAlu.add(alumno2);

//llamo a la funcion listar para que si hay registros, los saque
listar();
}
//funcion que muestra los registros que haya dentro del indexeddb
function listar(){
    //(1) crear una transaccion
    let transac = db.transaction("alumnos", "readonly");
  
    //(2) obtener el almacen
    let almacenAlum = transac.objectStore("alumnos");
  
    //(3) recuperar todos los datos del almacen
    let salida = almacenAlum.getAll();

    //una vez que sale bien, se ejecuta este bloque
    salida.onsuccess = function(){
    //guardo los datos de la bd en una variable
    alumno=salida.result;
    // Crear la tabla y encabezados
    let tabla = $("<table border='1'>");
    let fila = $("<tr>");

    //recorrer las propiedades (claves) del primer libro
    for (let key in alumno[0]) {
        console.log(key);
        //añadir a la fila un encabezado para cada clave
        fila.append(`<th>${key}</th>`);
    }

    //agregar fila con encabezados a la tabla
    tabla.append(fila);

    // Agregar datos de cada libro a la tabla
    for (let alu of alumno) {
        //crear una nueva fila para cada libro
        let fila = $("<tr>");
        //bucle que trae los valores dentro de cada libro y los mete en celdas
        for (let valor in alu) {
            fila.append(`<td>${alu[valor]}</td>`);
            console.log(valor);
        }
        //añadir fila con las celdas a la tabla
        tabla.append(fila);
    }
    // Agregar la tabla al html
    $("html").append(tabla);

    }
}
//funcion para añadir mas datos a la tabla
function guardarAlumno() {
    //cojo el valor que se meta en cada campo del form
    let nom = $("#nombre").val();
    let idMatricula = $("#matric").val();
    let modulo = $("#modulo").val();
    let ciclo = $("#ciclo").val();
    let nota = $("#nota").val();

    //para que no se dejen los campos vacios
    if(nom == "" || idMatricula == "" || modulo == "" || ciclo == "" || nota == "" )

    return alert("no se pueden dejar los campos vacíos");
    //guardar el objeto en el almacen

    //1. crear transaccion
    let transac = db.transaction("alumnos", "readwrite");
    
    //2. obtener el almacén
    let almacenAlum = transac.objectStore("alumnos");

    //3. añadir al almacen el objeto
    let resultado = almacenAlum.add({
        nombre: nom,
        idMat: idMatricula, 
        modulo: modulo,
        ciclo: ciclo,
        nota: nota
    })

    //vaciar los campos una vez se ha insertado el cliente
     nom = $("#nombre").val();
     idMatricula = $("#matric").val();
     modulo = $("#modulo").val();
     ciclo = $("#ciclo").val();
     nota = $("#nota").val();
        
    //manejo de posibles errores
    resultado.onsuccess = function() { 
        console.log("Cliente agregado al almacen", resultado.result);
    };
    resultado.onerror = function() {
        console.log("Error", resultado.error);
    };
    //vaciar tabla para que no cree una tabla nueva y la muestre cad vez que se meta algo
    $("table").empty();
    //lamar a la funcion listar para que muestre todo
    listar();

}