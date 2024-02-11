//funcion $.Get()
$(function () {
    //archivo.txt
    $("#leer").click(function (e) { 
        e.preventDefault();
        console.log("Click en boton");
        $.get("archivo.txt", function (data, textStatus, jqXHR) {
                console.log(data);
                console.log(textStatus);
                console.log(jqXHR);

            },
        );
    });

    //ARCHIVO JSON
    $("#leerJSON").click(function (e) { 
        e.preventDefault();
        //la funcion que le pasamos es el callback --> una vez que termine de leer los datoss
        //le decimos que hacer con ellos
        $.get("archivos/empleado.json", function (data, textStatus, jqXHR) {
                console.log(data);
                $("#datosEmple").html(`
                Nombre: ${data.nombre} <br/>
                Puesto: ${data.puesto} <br/>
                Edad: ${data.edad}
                `);

            }
        );
    });

    //ARCHIVO JSON CON ARRAY
    $("#leerJSONArray").click(function (e) { 
        e.preventDefault();
        //limpiar la funcion para que saque los tres registros
        $("#lista").html('');
        $.get("archivos/arrayEmpleados.json", function (data, textStatus, jqXHR) {
                console.log(data);
                $.each(data, function (indice, item) { 
                    //debemos concatenarlos porque sino los sobreescribe y solo sale el ultimo
                    $("#lista").html($("#lista").html()+`
                    <li>Nombre: ${item.nombre}</li>
                    <li>Puesto: ${item.puesto}</li>
                    <li>Edad: ${item.edad}</li>
                    <hr/>
                    `);
                });
            },
        );
    });

    //getJSON --> entrega los txt transformados a JSON
    $("#leerGetJSON").click(function (e) { 
        e.preventDefault();
        //limpiar la funcion para que saque los tres registros
        $("#lista").html('');
        $.getJSON("archivos/empleadosJSON.txt", function (data, textStatus, jqXHR) {
            //apesar de ser un archivo txt, lo transforma a JSON
                console.log(data);
                $.each(data, function (indice, item) { 
                    //debemos concatenarlos porque sino los sobreescribe y solo sale el ultimo
                    $("#lista").html($("#lista").html()+`
                    <li>Nombre: ${item.nombre}</li>
                    <li>Puesto: ${item.puesto}</li>
                    <li>Edad: ${item.edad}</li>
                    <hr/>
                    `);
                });            
        
        }
        );
    });

    //usando $.get()--> convertir el txt a JSON
    $("#convertirAjson").click(function (e) { 
        e.preventDefault();
        $("#contenido p").html('');
        $.get("archivos/empleadosJSON.txt", function (data, textStatus, jqXHR) {
                //data antes --> trae los datos como texto
                console.log(data);
                //convierte los datos que me ha traido del archivo en json
                data = JSON.parse(data);
                //trae los datos como JSON
                console.log(data);

                $.each(data, function (index, item) { 
                    // Crear un nuevo párrafo para cada dato
                let nuevoParrafo = $("<p>");
                nuevoParrafo.html(`
                    Nombre: ${item.nombre}<br>
                    Puesto: ${item.puesto}<br>
                    Edad: ${item.edad}
                `);
                //añadir al div el nuevo parrafo con los datos
                $("#contenido").append(nuevoParrafo);
                });
            },
        );
    });

    //mostrar datos de 2 objetos con arrays
    $("#objArray").click(function (e) { 
        e.preventDefault();
        $.getJSON("archivos/objetoConArray.json", function (data, textStatus, jqXHR) {
            //imprime los dos objetos con sus arrays    
            console.log(data);
            console.log(textStatus);

            //acceder a un objeto
            console.log(data.empleados);
            console.log(data.temporales);

            //sacar titulo de "Empleados"
            $("<h1>Empleados</h1>").appendTo("#contenido2"); 
            $.each(data.empleados, function (index, item) {
                // Crear un nuevo párrafo para cada dato
                let nuevoParrafo = $("<p>");
                nuevoParrafo.html(`
                    Nombre: ${item.nombre}<br>
                    Puesto: ${item.puesto}<br>
                    Edad: ${item.edad}
                `);
                //añadir al div el nuevo parrafo con los datos
                $("#contenido2").append(nuevoParrafo);
            });

            $("<hr/>").appendTo("#contenido2"); 

            //sacar titulo de "Temporales"
            $("<h1>Temporales</h1>").appendTo("#contenido2"); 
            $.each(data.temporales, function (index, item) { 
                // Crear un nuevo párrafo para cada dato
                let nuevoParrafo = $("<p>");
                nuevoParrafo.html(`
                    Nombre: ${item.nombre}<br>
                    Puesto: ${item.puesto}<br>
                    Edad: ${item.edad}
                `);
                //añadir al div el nuevo parrafo con los datos
                $("#contenido2").append(nuevoParrafo);
                });
            }
        );
    });
});