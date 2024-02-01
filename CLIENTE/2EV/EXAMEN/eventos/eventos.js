$(inicio);

function inicio() {
    //EVENTOS DE RATÓN
    // CLICK
    $(".unClick").click(function(){
        alert("has hecho click en el "+ $(this).text());
    });

    //METODO ON CON DBLCLICK Y CON CLICK
    $(".elemento").on({
        dblclick: function(){
        alert("Has hecho doble click en el "+ $(this).html()); //.html() te saca tambien las etiquetas que haya dentro del texto
        },
        click: function(){
            alert("Has hecho un simple click en el " + $(this).text());
        }
    });

    //MOUSEENTER
    // $("#elem2").mouseenter (function(){
    //     alert("Has metido el raton en el "+ $(this).text())
    // });

    //MOUSELEAVE
    // $("#elem3").mouseleave(function(){
    //     alert("Has sacado el raton del "+ $(this).text())
    // });
    //HOVER
    // $("#elem4").hover(function(){
    //     alert("Has metido el raton en el "+ $(this).text());
    // },
    // function(){
    //     alert("Y ahora lo has sacado del "+ $(this).text());
    // });
    ////////////////////////////////
    //EVENTOS DE FORMULARIO
    //SUBMIT --> hay que clicar el btn para que salga el texto en el div
    $("#miFormulario").submit(function(event){
        //Prevenir el comportamiento predeterminado del formulario (que no se recargue la pagina automaticamente)
        event.preventDefault();
        let nom = $("#nombre").val();
        $("#miTexto").text(nom);
    });

    //CHANGE --> sale automatico en el div
    $("#miFormulario").change(function(){
        let nom = $("#nombre").val();
        $("#miTexto2").text("Nombre cambiado a: "+ nom);
    });

    //FOCUS
    $("input").focus(function(){
        $(this).css("background-color", "red");
    });

    //BLUR --> cuando se ha pinchado en el input y luego se pincha en otro lado, se cambia el background 
    $("input").blur(function(){
        $(this).css("background-color", "green");
    });

    //EVENTOS DE TECLADO
    //KEYPRESS
    $("input").keypress(function(event){
        $("#miTexto3").text("Tecla presionada: " + String.fromCharCode(event.which)); //saca en el div un texto con cada letra que presionas
    });

    //KEYDOWN
    $("input").keydown(function(event){
        $("#miTexto4").text("Tecla bajada: " + String.fromCharCode(event.which)); //saca en el div un texto con cada letra que presionas
    });

    //KEYUP
    $("input").keyup(function(event){
        $("#miTexto5").text("Tecla soltada: " + String.fromCharCode(event.which)); //saca en el div un texto con cada letra que presionas
    });
}