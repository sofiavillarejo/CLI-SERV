let productos = [];
let myChart = null;

function anadirProducto(){

    nombre = $("#prod").val();
    tienda1 = $("#tri").val();
    tienda2 = $("#puc").val();
    tienda3 = $("#arc").val();
    color = $("#color").val();


    const xValues = ["Triunfo", "Puca", "Arcoiris"];
    const yValues = [55, 49, 44];

    var producto = {label: nombre, data: [tienda1,tienda2,tienda3], backgroundColor: color}
    productos.push(producto)

    if(myChart){
        myChart.destroy();
    }
    

    myChart = new Chart("myChart", {
    type: "line",
    data: {
        labels: xValues,
        datasets: productos
    },
    options: {
        legend: {display: false},
        title: {
        display: true,
        text: "Venta de productos en supermercados"
        }
    }
    });
}
