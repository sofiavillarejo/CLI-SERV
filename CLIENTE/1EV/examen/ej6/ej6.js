//.js que realiza una solicitud al AJAX del servidor y analice el resultado

//sacamos los valores de los campos del formulario qu eenvie el cliente
let email = document.getElementById("email").value;
document.getElementById('resultado').innerHTML = email;
console.log(email);
function validarEmail() {
        //objeto para hacer peticiones al servidor -> XMLHttpRequest()
        let httprq = new XMLHttpRequest();//se usa el new porque es un objeto y se usa eso para construirlo
    
        //registrar la funcion que trata la respuesta del servidor
        httprq.onreadystatechange = function () {
        //esta linea siempre es asi
            if(this.readyState == 4 && this.status == 200){ //si la respuesta es correcta, se ejecuta este codigo
                //para ver la diferencia entre texto normal y  el json
                console.log(this.responseText);
                //console.log(JSON.parse(this.responseText));
                //texto que me envia el servidor y que tengo que convertir en objeto de json
                let datos = JSON.parse(this.responseText);//lo que me devuelve el python
                alert(datos); //creo una funcion que contiene todo lo que me ha enviado el servidor
            } else{ // la peticion tiene un error
                console.log("estado: " +this.readyState+", respuesta servidor: "+this.status);
            }
        }
        //construir peticion
        httprq.open("GET", "/ej6/validar_email.py", true) 
    
        //ejecuto la peticion
        httprq.send();
}

	


    
