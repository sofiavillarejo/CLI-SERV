$(function () {
    //añadir clase al h1 del titulo
    $("#agregarClase").click(function () { 
        $("#titulo").addClass("titulos");
    });

    //ocultar parrafo
    $("#ocultar").click(function (e) { 
        e.preventDefault();
        $("p").hide();
    });

    //mostrar parrafo
    $("#mostrar").click(function (e) { 
        e.preventDefault();
        $("p").show();
    });

    //agregar parrafo
    $("#agregar").click(function (e) { 
        e.preventDefault();
        let parraf = $("p").html();
        $("#contenido").append("<p>"+parraf+"</p>");
        
    });

    //borrar todo el contenido
    $("#borrarTodo").click(function (e) { 
        e.preventDefault();
        $("#contenido").remove();
    });

    //añadir atributos a una imagen y crearla
    let divContenido = $("#contenido");
    $(divContenido).append("<img>");
    let img = $("img");
    $(img).attr('id', 'imagen1');
    $("#imagen").click(function (e) { 
        e.preventDefault();
        $("#imagen1").attr('src', 'https://images.hola.com/imagenes/mascotas/20180925130054/consejos-para-cuidar-a-un-gatito-recien-nacido-cs/0-601-526/cuidardgatito-t.jpg?tx=w_680');
        $("#imagen1").attr('alt', 'foto gatito');
    });  
});

//cambiar color pasandole el id por parametro
function cambiaColor(id){
    $("#"+id).css('color', 'red');
}
//cambiar fondo pasandole el id por parametro
function cambiaBackground(id){
    $("#"+id).css('background', 'lightblue');
}

function apareceDesaparece(id) {
    $("#"+id).toggle();
}