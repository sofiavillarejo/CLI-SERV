$("button").click(function() {
    //crear nuevos elementos li
    let input1 = $("#input1").val();
    let imagen = $("<img>"); 

    // let imagen = $("<img src='"+input1+"'>"); otra forma de declarar el src
    imagen.attr("src", input1) //crear el atributo src de cada imagen

    let boton = $("<button>");
    boton.text("Eliminar imagen");
    let miDiv = $("#galeria");
    let crearDiv = $("<div>");
        

    imagen.css("height", 300);    
    imagen.css("width", 400);
    imagen.append(boton);
    crearDiv.append(imagen);
    crearDiv.append("<br>");
    crearDiv.append(boton);
    miDiv.append(crearDiv);

    //cuando se haga click en algun li, que se borre
    $(boton).click(function(){
        $(crearDiv).remove();
    })
    $(imagen).fadeOut(0);
    $(imagen).fadeIn(1000);

})