$(inicio);
//funcion inicio que al hacer click en el boton con id="marcas" del html, te trae los registro del py
function inicio(){
    $("#marcas").click(function () { 
	//coger datos del py
	$.get("ejer3A.py",
		function(data,status){
            //mostrar en consola los datos que nos trae
			console.log(data);
			//bucle que recorrre los datos
            for(dat of data){
                $("#salida").append(dat);
                for (d of dat){
                    
                }

            }
		});
    });
}
