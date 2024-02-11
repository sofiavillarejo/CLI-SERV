
$(function () {
    let nFila = 1;

    $("#btn").click(function (e) { 
        e.preventDefault();
        let nom = $("#nombre").val();
        let ape = $("#apellido").val();
        let ed = $("#edad").val();

        console.log(nom, ape, ed);

        let tab = $("#tabla");
        let fila = $("<tr>");
        fila.attr('id', 'fila'+nFila);

        let btn = $("<button id='borrado'>Borrar</button>");
        btn.attr('onclick', "borrarFila("+nFila+")");

        let celdaNom = $("<td>").append(nom);
        fila.append(celdaNom);

        let celdaApe = $("<td>").append(ape);
        fila.append(celdaApe);

        let celdaEdad = $("<td>").append(ed);
        fila.append(celdaEdad);

        let celdaBorrar = $("<td>").append(btn);
        fila.append(celdaBorrar);

        tab.append(fila);
        nFila++;
    });

    //modificar atributos
    $("#cambiarAtrr").click(function (e) { 
        e.preventDefault();
        //le quito la clase
        $("#parrafo").removeClass('parraf1');
        //le cambio su id directamente
        $("#parrafo").attr('id', 'id2');
    });

});

function borrarFila(nFila) {
    let filaBorrar = $("#fila"+nFila);
    filaBorrar.remove();
}

function modificarFila() {
    let nom = $("#nombre").val();
    let ape = $("#apellido").val();
    let ed = $("#edad").val();

    let filaMod = $("#fila").val();
    let filaSelecc = $("#fila"+filaMod);
    filaSelecc.empty();
    let celdaNom = $("<td>").append(nom);
    filaSelecc.append(celdaNom);

    let celdaApe = $("<td>").append(ape);
    filaSelecc.append(celdaApe);

    let celdaEdad = $("<td>").append(ed);
    filaSelecc.append(celdaEdad);

    let btn = $("<button id='borrado'>Borrar</button>");
    btn.attr('onclick', "borrarFila("+filaMod+")");

    let celdaBorrar = $("<td>").append(btn);
    filaSelecc.append(celdaBorrar);

    filaSelecc.css('background', 'red');
}

