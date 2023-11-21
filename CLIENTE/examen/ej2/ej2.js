//.js que valida los parametros de un formulario y los envia segun las condiciones
//creamos la respuesta para enviar o no el formulario
let respuesta = false;
//funcion para validarlo
function validarNumeros() {
    //cogemos los valores que introduce el usuario en el input
    let num1 = document.getElementById("numero1").value;
    let num2 = document.getElementById("numero2").value;
    //convertir texto a numeros enteros
    parseInt(num1);
    parseInt(num2);
    //condicionales para validar o no el formulario
    if(num1>num2){
        alert("Error: 'Número 1' debe ser menos o igual que 'Número2'.");
        respuesta= false;
    }else if(isNaN(num1) || isNaN(num2)){
        alert("Error: Introduce un número entero válido.");
        respuesta= false;
    }
    //validar formulario si todo esta bien
    alert("Formulario validado");
    respuesta= true;

}