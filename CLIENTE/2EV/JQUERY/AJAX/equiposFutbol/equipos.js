$(inicio);

function inicio(){
	//coger datos del py
	$.get("equipos.py",
		function(data,status){
			console.log(data);
			//llamar a la funcion y le paso los datos recibidos
			creaFormulario(data.equipos);
			console.log(status);
		});
}

//funcion que para cada equipo, añade un option en el form
function creaFormulario(datos) {
	//para cada equipo que recibe de datos (equipos.py)
	for(equipo of datos){
		console.log(equipo);
		//añade al form las option con cada equipo (nombre que recibe de datos)
        $("#seleccion").append("<option>" + equipo + "</option>");
	}
}

//funcion que se ejecuta al apretar el boton
function pedirDatos(){
	//trae el py datosEquipo y le pasamos el valor del form que se seleccione
	$.get("datosEquipos.py?equipo="+$("#seleccion").val(),
	//aqui data, son todos los datos del equipo que has selecccionado (solo te trae ese)
		function(data,status){
			console.log(data);
			//limpiar el div donde se añaden los datos
			$("#datosEquipo").html("");
			// meter en una variable los objetos (Real Madrid, FC Barcelona...)
			let clave = Object.keys(data);
			console.log(clave);
			//seleccionar el div donde meter el texto
			let miDiv = $("#datosEquipo");
			// meter en el div (en negrita) los titulos + la propiedad de cada clave (el valor textual de cada clave)
			miDiv.html("<b>" +clave+ "</b>"+ "<br> "+ "Estadio: "+ data[clave].estadio + " <br>" + "Fundacion: " + data[clave].fundacion);
			console.log(clave+""+data[clave].estadio);
		});
}
