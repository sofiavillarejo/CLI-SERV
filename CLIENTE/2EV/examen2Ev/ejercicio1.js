//funcion onload
$(function () {
    //creo h2
    let encab = $("<h2>");
    //le añado texto
    encab.text("Berenjenas rellenas de atún al horno");
    //añado el h2 al html para que se muestre
    $("html").append(encab);

    //creo el h4
    let subti = $("<h4>");
    //le añado texto
    subti.text("Preparación");
    //añado el h4 al html para que se muestre
    $("html").append(subti);

    //creo la lista con el id --> tambien se puede hacer añadiendole .attr('id', 'receta')
    let lista = $("<ol id='receta'>");
    //le paso li a la lista con el contenido
    lista.html(`<li>Calentar el horno al máximo de potencia. Cortar la berenjena por la mitad.</li>
                <li>Meter la berenjena al horno hasta que se queden blandas.</li>
                <li>Sacar la berenjena de la piel y mezclar con todos los ingredientes.</li>
                <li>Introducir la mezcla en las dos mitades de la berenjena.</li>
                <li>Poner queso rallado encima y gratinas el horno.</li>
            `);

    //añado la lista creada al html para que se muestre
    $("html").append(lista);

    //creo otro h4
    let subti2 = $("<h4>");
    //le paso texto
    subti2.text("Ingredientes");
    //añado el h4 al html para que se muestre
    $("html").append(subti2);

    //misma repeticion que antes: crear lista, pasarle contenido y añadirla al html
    let lista2 = $("<ul id='ingredientes'>"); //se puede poner su id con la funcio attr('id','ingredientes')
    lista2.html(`<li>Una berenjena</li>
                <li>2 latas de atún.</li>
                <li>Tomate frito en aceite de oliva.</li>
                <li>Queso parmesano rallado.</li>
                <li>Cebola molida.</li>
                <li>Comino en polvo.</li>
            `);
    //añado la lista creada al html para que se muestre
    $("html").append(lista2);
});