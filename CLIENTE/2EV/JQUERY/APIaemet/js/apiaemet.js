//CONECTARSE A UNA API
var settings = {
    "async": true,
    "crossDomain": true,
    "url": "https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/28161/?api_key=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ6eDIyc3R1ZGVudDMzMjlAY29sZWdpb3ZhbGxlZGVsbWlyby5lcyIsImp0aSI6IjE3ZWRiMGY2LWRjMDAtNDhkNy1iODViLTlhOTFkZDNhNDNhMyIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNzA1OTEwNDIwLCJ1c2VySWQiOiIxN2VkYjBmNi1kYzAwLTQ4ZDctYjg1Yi05YTkxZGQzYTQzYTMiLCJyb2xlIjoiIn0.-ddVuTFdGKZ5MBL8RjUo_R40VCnhc0Ig1CjQoUaPzi0",
    "method": "GET",
    "headers": {
      "cache-control": "no-cache"
    }
  }

$.ajax(settings).done(function (response) {
    if (response.estado == 200) {
        pedirDatos(response.datos);
}else{
    alert("error:" + response.descripcion + "(" + response.estado + ")");
}
});

function pedirDatos(resultado) {
    let settings2 = {
        "async": true,
        "crossDomain": true,
        "url": resultado,
        "headers": {
          "cache-control": "no-cache"
        }
      }

    //nos devuelve un fichero que contiene json y por ello, hay que pasarlo a JSON real
    $.ajax(settings2).done(function (response) {
        let salida = JSON.parse(response);
        console.log(salida[0].nombre);
        console.log(salida[0].prediccion.dia);
        let texto = "";
        for(let predDia of salida[0].prediccion.dia){
            texto += (predDia.fecha) + "-";
            texto += (predDia.temperatura.maxima)+ "-";
            texto += (predDia.temperatura.minima)+ "-";
            texto += (predDia.probPrecipitacion[0].value)+ "-";
            texto += "<br>";
          }
        $("#salida").html(texto);
    });
  
}