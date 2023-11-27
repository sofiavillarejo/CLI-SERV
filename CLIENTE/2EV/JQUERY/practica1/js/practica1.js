/*
//ONLOAD en Jquery 
// $ -> forma de acceder a las funcionalidades de Jquery
// $ (selector).accion()
//se ejecutan las tres en el orden en que estan escritas
// forma 1
$(principal);

function principal(){
    alert("una forma");
}

//forma 2
$(document).ready(function(){
    alert("otra forma");
})

//forma 3
$(function(){
    alert("ultima forma");
})

//seleccionar elementos del html -> una vez este cargado el parrafo, se lanza el alert (es como un onload del parrafo)
$("#p1").ready(alert("párrafo accesible"));

//////////////////////////////////////////////////

    SELECTORES
    $(elementos html)
    $(.clase)
    $(#id)

$("p").ready(alert("parrafo accesible")); //saca todos los parrafos que haya en el html

*/

//cargo la funcion = onload
$(principal);

//creo funciones
function principal(){
    console.log("DOM creado");
    //selecciono el boton con el id ocultar y le asigno una funcion que selecciona los parrafos del html y los oculta
    $("#ocultar").click(function () {
        $("p").hide();    
    })

    //selecciono el boton con el id mostrar y le asigno una funcion que selecciona los parrafos del html y los muestra
    $("#mostrar").click(function () {
        $("p").show();    
    })
    $("#mostrarOcultar").click(function () {
        $("p").toggle(); //alterna entre mostrar y ocultar los elementos   
    })
    $("#mostrarOcultarPares").click(function () {
        $(".par").toggle(); //alterna entre mostrar y ocultar los elementos con la clase par  
    })
    $("#mostrarOcultarImpares").click(function () {
        $(".impar").toggle(); //alterna entre mostrar y ocultar los elementos con la clase impar  
    })

    //cuando pulses en el parrafo 1, este se oculta
    //sin el dolar, se selecciona el DOM
    $("#p1").click(function() {
        // this.innerHTML = "pulsado"; //this se refiere al elemento seleccionado
        this.style.display = "none"; //ocultar el parrafo al pulsarse
    })

    //ocultar el parrafo al hacer click en él
    //con el $, se selecciona el objeto y se pueden usar los metodos de JQuery
    $("#p2").click(function() {
        $(this).hide(); 
    })

    //cuando se haga doble click en algun parrafo:
    $("p").dblclick(function(){
        console.log(this.innerHTML);//sacar su contenido por consola
    })

    //cuando se pase el raton por encima
    $ ("p").mouseenter(function(){
        console.log(this.innerHTML);//sacar su contenido por consola
    })

    //cuando se clique y se SUELTE el boton
    $ ("p").mouseup(function(){
        console.log(this.innerHTML);//sacar su contenido por consola
    })

    //mouseenter + mouseleave (saca dos eventos: cuando entra el raton y cuando sale)
    $ ("p").hover(function(){
        console.log(this.innerHTML);//sacar su contenido por consola
    })

    //foco en los botones (se resaltan)
    $ ("button").focus(function(){
        console.log(this.innerHTML);//sacar su contenido por consola
    })

}
