$(function () {
    //ARCHIVO JSON
    $("#leerJSON").click(function (e) { 
        e.preventDefault();
        //la funcion que le pasamos es el callback --> una vez que termine de leer los datos
        //le decimos qué hacer con ellos
        $.get("datos.json", function (data, textStatus, jqXHR) {

            //PRIMERA FORMA
            //Iterar sobre cada objeto en el array de datos
            // data.forEach(function(datos) {
            //Crear una nueva fila para cada objeto
            //     let fila = $("<tr>");

            // Agregar cada propiedad del objeto como una celda en la fila
            //     fila.append(`<td>${datos.id}</td>`);
            //     fila.append(`<td>${datos.name}</td>`);
            //     fila.append(`<td>${datos.username}</td>`);
            //     fila.append(`<td>${datos.email}</td>`);

            //Agregar la fila a la tabla
            //     $("#datos").append(fila);
            // });
            
//************************************************************
            //SEGUNDA FORMA
            for(persona of data){
                let tabla =$("#datos");
                let fila =$("<tr>");

                let celdaId = $("<td>").text(persona.id);
                let celdaName = $("<td>").text(persona.name);
                let celdaUsername = $("<td>").text(persona.username);
                let celdaEmail = $("<td>").text(persona.email);

                fila.append(celdaId, celdaName, celdaUsername, celdaEmail);

                tabla.append(fila);
            }
        });
    });
});

