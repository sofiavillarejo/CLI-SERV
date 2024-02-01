$(inicio);

function inicio(){
	$.get("equipos.py",
		function(data,status){
			creaFormulario(data.equipos);
			console.log(status);
		});
}

function creaFormulario(datos) {
	
	for(equipo of datos){
		console.log(equipo);
        $("#seleccion").append("<option>" + equipo + "</option>");
	}
    
}

function pedirDatos(){
	$.get("datosEquipos.py?equipo="+$("#seleccion").val(),
		function(data,status){
			$("#datosEquipo").html("");
			let clave = Object.keys(data);
			let miDiv = $("#datosEquipo");
			miDiv.html("<b>" +clave+ "</b>"+ "<br> "+ "Estadio: "+ data[clave].estadio + " <br>" + "Fundacion: " + data[clave].fundacion);
			console.log(clave+""+data[clave].estadio);
		});
}
