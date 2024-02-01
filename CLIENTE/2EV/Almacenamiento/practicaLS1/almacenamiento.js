function guardar(){
    let datos = new Map();
    datos.set("datoTexto", $("#datoTexto").val());
    datos.set("datoNumber", $("#datoNumber").val());
    datos.set("datoEmail", $("#datoEmail").val());
    datos.set("datoFecha", $("#datoFecha").val());
    datos.set("datoColor", $("#datoColor").val());

    //guardar nuestro mapa en el local hay que convertirlo en Array y pasarlo a JSON
    //porque los mapas no se pueden pasar a JSON directamente
    let miMapa = JSON.stringify(Array.from(datos.entries()));
    localStorage.setItem("miMapa", miMapa);

    localStorage.setItem("miArray", JSON.stringify([1,2,3,4,5]));

    //forma de hacerlo mas larga////////////////////////
    // localStorage.setItem("datoTexto", $("#datoTexto").val()); //se almacena este texto en el localStorage de la web (ctrl f12 -> aplicacion)
    // localStorage.setItem("clave2", "valor2");
    // localStorage.setItem("datoNumber", $("#datoNumber").val());
    // localStorage.setItem("datoEmail", $("#datoEmail").val());
    // localStorage.setItem("datoFecha", $("#datoFecha").val());
    // localStorage.setItem("datoColor", $("#datoColor").val());
}

function borrar(){
    let clave = prompt("¿Qué clave quieres borrar?");
    localStorage.removeItem(clave);
    // localStorage.clear(); //metodo que borra todo lo que contenga el localstorage
}

function recuperar(){
    if(localStorage.getItem("miMapa")){
        let datosArray = JSON.parse(localStorage.getItem("miMapa"));
        datosRecuperados = new Map(datosArray); //pasamos el array ya convertido a un mapa para mostrarlo
        console.log(datosRecuperados);
        // alert("Existe");
    }else{
        alert("No existe");
    }
    // let clave = prompt("¿Qué clave quieres recuperar?");
    // alert(localStorage.getItem(clave));
}