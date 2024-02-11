$(inicio);
// PARA EL EXAMEN ENTRAN --> BAR CHART, PIE CHART, LINE CHART Y SCATTER CHART

function inicio(){
  const cnv = $("#misBarras");

  const datos = {
    labels:['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado'],
    datasets:[
      //PRIMER CONJUNTO
        {
        label : "DATOS AZUL",
        data:[1,2,3,4,2,1,3],
        borderWidth: 3,
        backgroundColor: ["blue", "black"], //el primer valor, azul, el segundo negro y asi DE ESTE CONJUNTO DE DATOS (PRIMERA BARRA EN CADA CONJUNTO)
        borderColor: ["yellow", "black"],
        hoverBackgroundColor : ["white", "green"]
        },
      //SEGUNDO CONJUNTO
        {
        label : "DATOS ROSA",
        data:[3,1,2,3,4,2,1],
        backgroundColor: "pink"

        },
      //TERCER CONJUNTO
        {
        label : "DATOS AMARILLO",
        data:[1,3,1,2,3,4,2],
        backgroundColor: "yellow"

        }
      ]
  };

new Chart(cnv, {
type: 'bar',
  data: datos,
  //poner barras en horizontal
  options:{ 
    indexAxis: 'y'
  }
});

  const cnv2 = $("#miScatter");
  const datos2 = {
    datasets: [{
      label: 'Lunes',
      //para el scatter es importante meter los ejes x e y
      data: [{
        x: -10,
        y: 0
      }, 
      {
        x: 0,
        y: 10
      }, 
      {
        x: 10,
        y: 5
      }, 
      {
        x: 0.5,
        y: 5.5
      }],
      backgroundColor: 'blue'
    },
    {
      label: 'Martes',
      //para el scatter es importante meter los ejes x e y
      data: [{
        x: 5,
        y: 0
      }, 
      {
        x: 0,
        y: 8
      }, 
      {
        x: 3,
        y: 10
      }, 
      {
        x: 1,
        y: 6
      }],
      backgroundColor: 'red'
    }],
  };

  new Chart(cnv2, {
    type: 'scatter',
      data: datos2,
    });

  const cnv3 = $("#miPie");
  const datos3 = {
    labels: [
      'Lunes',
      'Martes',
      'Miércoles'
    ],
    datasets: [{
      label: 'Grafico de tarta',
      data: [300, 50, 100],
      backgroundColor: [
        'red',
        'blue',
        'yellow'
      ],
      hoverOffset: 4
    }]
  };

  new Chart(cnv3, {
    type: 'pie',
      data: datos3,
    });



}

