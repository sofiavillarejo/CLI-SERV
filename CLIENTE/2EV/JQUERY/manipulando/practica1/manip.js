$(principal);

function principal(){
    // $("p").text();
    // console.log($("body").text());
    // // alert("");
    // $("p").text("<b>HOLA MUNDO</b>");//manipula el contenido del parrafo
    // console.log($("p").text());
    // //text -> cambiar contenido del nodo texto
    // // html -> permite crear estructuras 
    // // alert("");
    // $("p").html("<b>Hola mundo</b>");//manipulo el parrafo
    // console.log($("p").text());

    // //me devuelve el contenido de los inputs que haya en el html
    // console.log($("input").val());

    // $("p1").css("backgroundColor", "red");
    // $("p1").css("color", "white");

    // $("p").addClass("verde");//añade la clase verde a los parrafos
    // // toggleClass->si tiene la clase, la quita y sino, la pone
    // //en este ejemplo, desaparece la clase verde
    // $("p").toggleClass("amarillo");
    // $("p").removeClass("amarillo");

    //ANIMACIONES
    // $("p").fadeOut(1000);
    // $("p").fadeIn(1000);
    $("p").slideUp(1000);
    $("p").slideDown(1000);

    //CREAR ELEMENTOS DEL DOM
    let elem = $("<p>");
    let b = $("body");
    elem.text("Este es mi nuevo parrafo creado");
    b.append(elem);
}