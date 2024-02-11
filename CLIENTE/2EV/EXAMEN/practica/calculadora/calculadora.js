$(calcular);

function calcular() {
    let resultado = 0;
    let salida = $("#salida");

    let num1 = Number($("#num1").val());
    console.log(num1);
    let num2 = Number($("#num2").val());
    console.log(num2);

    let suma = $("#suma").prop('checked'); //si en el form "suma" esta seleccionada (checked)
    console.log(suma);
    let resta = $("#resta").prop('checked');
    console.log(resta);
    let multiplicacion = $("#multi").prop('checked');
    console.log(multiplicacion);
    let division = $("#divi").prop('checked');
    console.log(division);

    if (suma){
        resultado = num1 + num2;
    }
    if (resta){
        resultado = num1 - num2;
    }
    if (multiplicacion){
        resultado = num1 * num2;
    }
    if (division){
        resultado = num1 / num2;
    }
    console.log(resultado);
    salida.html("El resultado de la operacion es "+ resultado);


}