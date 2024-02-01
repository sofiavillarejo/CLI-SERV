$(principal);

function principal(){
//addClass
$("#btn1").click(function(){
    $("p").addClass("rojo");
});

//after
$("#after").click(function(){
    // $("#parraf2").after("<p>Nuevo parrafo añadido</p>");
    //forma para guardar el p y añadirle la clase rojo
    let nuevoP = $("<p>Nuevo parrafo añadido</p>");
    $("#parraf2").after(nuevoP);
    let mensaje = prompt("¿Quieres añadirle la clase 'rojo'?");
    if (mensaje == "si" || mensaje == "Si"){
        nuevoP.addClass("rojo");
    }
});

//append --> añade html al final del elemento indicado // before funciona igual pero se añade antes que el elemento indicado
$("#append").click(function(){
    $("#parraf2").after("<p><b>Texto adjunto</b></p>");
});

//empty
$("#borrarDiv").click(function(){
    $("#elem1").empty();
});

//html
$("#html").click(function(){
    $("#elem1").html("Hola");
});

//prepend --> añadir al principio contenido
$("#prepend").click(function(){
    $("ol").prepend("<li>Texto añadido</li>");
});

//remove
$("#borrar").click(function(){
    $("#parraf2").remove();
});

//remoteAttr
$("#borrarAttr").click(function(){
    $("#parraf3").removeAttr("style");
});

//removeClass
$("#borrarClass").click(function(){
    $("p").removeClass("rojo");
});
//text
$("#cambiarText").click(function(){
    $("#parraf4").text("Nuevo contenido del parrafo");
});

//toggleClass
$("#toggleClass").click(function(){
    $("#parraf2").toggleClass("parrafos");
    $("#parraf4").toggleClass("parrafos");
});

//val
$("#valForm").click(function(){
    $("input").val("Sofia");
});

$("#send").click(function(){
    let valor = $("input").val();
    let p4 = $("#parraf4");
    let añadirP = $("<p>"+ valor + "</p>");
    p4.append(añadirP);
    añadirP.css("color", "green");
})
}