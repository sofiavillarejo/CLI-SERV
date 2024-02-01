// funcion que detecta si alguno de los dos inputs está activo o no
function campoActivo() {
    let nombre = document.getElementById("nombre");
    let apellido = document.getElementById("apellido");

    if(nombre.onfocus()){
        alert(`El campo ${nombre} está activo`);
        
    }
    if(apellido.onfocus()){
        alert(`El campo ${apellido} está activo`);
    }
    
}