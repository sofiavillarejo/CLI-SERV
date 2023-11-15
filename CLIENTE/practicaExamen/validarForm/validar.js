// function validar() {
// 	let respuesta = false;
// 	let param1 = document.getElementById("param1");
// 	let param2 = document.getElementById("param2");
// 	let param3 = document.getElementById("param3");

// 	if (param1.value == "hola"){
// 		respuesta=true;
// 	}else if (param2.value == 22){
//         respuesta=true;
//     }else if (param3.value == 1.70){
//         respuesta=true;
//     }else{
// 		param1.style.background = "red"
// 	}
// 	return respuesta
// }

let respuesta = false;
let palabrasProhibidas = ["Hola", "Adios" , "Maria"];

function validarFormulario() {
    let nombre = document.getElementById("nombre").value;
    let edad = document.getElementById("edad").value;
    let contraseña1 = document.getElementById("cont1").value;
    let contraseña2 = document.getElementById("cont2").value;

    //validar que no esten vacios
    if (nombre == "" && edad=="") {
      alert("No has introducido tu nombre ni tu edad");
      respuesta= false;
    }else if (nombre == "" && edad !=0){
      alert("No has introducido tu nombre");
      respuesta= false;
    }else if (nombre != "" && edad == ""){
      alert("No has introducido tu edad");
      respuesta= false;
    }else if (isNaN(edad)){
      alert("Debes introducir numeros");
      respuesta= false;
    }else if (contraseña1 != contraseña2){
      alert("Tus contraseñas no coinciden");
      respuesta= false;
    }else{
      for (let palabraProhibida of palabrasProhibidas) {
        if (nombre.toLowerCase().includes(palabraProhibida.toLowerCase())) {
            alert("Esa palabra está prohibida en el nombre");
            respuesta= false;
        }    
      }
      respuesta= true;
    }

    if ()
}