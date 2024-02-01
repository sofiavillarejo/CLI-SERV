$(calculaIMC);
function calculaIMC() {
    
    $("button").click(function(){
        let peso = Number($("#peso").val());
        let altura = Number($("#altura").val());
        let IMC = 0;
        IMC = (peso / (altura*altura)).toFixed(2);
        console.log(IMC);
        $("#IMC").html("EL resultado es "+IMC);
        
    })
}

$(calculaHipo);
function calculaHipo() {
    $("button").click(function(){
        console.log("Función calcula");
        //creamos variable para mostrar el resultado
        let resultado = 0;
        //crear variables para guardar los dos numeros que son el cateto 1 y el cateto 2
        let c1 = Number($("#cat1").val());
        let c2 = Number($("#cat2").val());

        //asignamos a resultado la operacion (raiz cuadrada de la suma de los catetos)
        resultado = Math.sqrt(c1*c1+c2*c2).toFixed(2);
        //mostramos en la consola el resultado
        console.log(resultado);
        //mostramos el resultado por pantalla
        $("#salida").html("El resultado es "+resultado);
        
    })
}