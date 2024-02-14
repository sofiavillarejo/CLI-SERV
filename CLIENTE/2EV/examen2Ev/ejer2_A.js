//funcion que al apretar el boton del html, cambia el color de cada elemento dependiendo del select
function cambiaColor() {
    //traemos el valor del select
    let form = $("#selecion").val();
    console.log(form);
    //condicion que declara que si el valor del select es == "red"
    if(form == "red"){
        //seleccionamos el h1 del html y le cambiamos el color a rojo
        $("#titCap").css('color', 'red');
    }
    //condicion que declara que si el valor del select es == "green"
    if(form == "green"){
        //seleccionamos el h4 del html y le cambiamos el color a rojo
        $("#entrada").css('color', 'green');
    }
    //condicion que declara que si el valor del select es == "blue"
    if(form == "blue"){
        //seleccionamos el p del html y le cambiamos el color a rojo
        $("#parrafo").css('color', 'blue');
    }
}