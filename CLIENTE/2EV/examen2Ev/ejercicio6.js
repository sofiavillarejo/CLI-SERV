//traer con el id nuestro canva del html para crear el grafico
const cnv = $("#grafScatter");
//declaramos los datos que va a representar el grafico
  const datos = {
    //conjuntos de datos del grafico
    datasets: [{
        //nombre del primer conjunto que se verá en la leyenda
      label: 'Ventas',
      //datos x e y del grafico
      data: [
            { x: 1, y: 12000 },
            { x: 2, y: 15000 },
            { x: 3, y: 18000 },
            { x: 4, y: 16000 },
            { x: 5, y: 20000 },
            { x: 6, y: 17000 },
            { x: 7, y: 22000 },
            { x: 8, y: 21000 },
            { x: 9, y: 23000 },
            { x: 10, y: 24000 },
            { x: 11, y: 25000 },
            { x: 12, y: 26000 }
        ],
        //color de los puntos y de la etiqueta de la leyenda
      backgroundColor: 'blue'
    },
    {
    //nombre del segundo conjunto de datos
      label: 'Gastos',
      //datos x e y del segundo conjunto
      data: [
            { x: 1, y: 8000 },
            { x: 2, y: 7000 },
            { x: 3, y: 9000 },
            { x: 4, y: 5000 },
            { x: 5, y: 12000 },
            { x: 6, y: 6000 },
            { x: 7, y: 10000 },
            { x: 8, y: 11000 },
            { x: 9, y: 9500 },
            { x: 10, y: 10500 },
            { x: 11, y: 12000 },
            { x: 12, y: 13000 }
        ],
        //color de los puntos y de la etiqueta de la leyenda del segundo conjunto de datos
      backgroundColor: 'red'
    }],
  };

  //declaramos la creacion del grafico de tipo scatter pasandole todos los datos creado anteriormente y metidos
  //en la variable datos
  //previamente declarar que se crea dentro de cnv que es nuestro canva
  new Chart(cnv, {
    type: 'scatter',
      data: datos,
    });
