//contador para el texto de cada elemento
let cont = 1;
//sacar el boton y añadirle una funcion
$("button").click(function() {
    //crear nuevos elementos li
    let nuevoLi = $("<li>");
    //añadimos texto
    // nuevoLi.text("Elemento "+cont);
    //incrementamos el contador para que se vaya sumando despues de cada elemento li
    // cont++;

    //añadir la lista no ordenada a ua variable
    let lista = $("ul");
    //añadir a la lista, los nuevos li
    lista.append(nuevoLi);
    //cuando se haga click en algun li, que se borre
    $(nuevoLi).click(function(){
        $(this).remove();
    })
    //añadir al li, el texto que el usuario meta en el input
    nuevoLi.text($("input").val());
    //añadir animacion a cada li
    $("li").animate({
        fontSize: "30px",
    }, 1000);
})



