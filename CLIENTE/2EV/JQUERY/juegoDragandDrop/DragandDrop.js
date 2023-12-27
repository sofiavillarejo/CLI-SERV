function arrastrando(event) {
    console.log(event.target.id);
    event.dataTransfer.setData('text/plain', event.target.id); //guardo dentro de setData el id y le doy el nombre de text para luego poder recuperarlo    

}

function soltando(event) {
    const id = event.dataTransfer.getData('text');

    let objQueArrastro = $("#" +id);
    let destino = $("#" + event.target.id);

    destino.append(objQueArrastro); 
    destino.removeAttr("ondrop");
}
function recibir(event) {
    event.preventDefault();
    console.log(event.target.id);
}

function comprobar(){
        let fotoOne = $("#foto1");
        let fotoTwo = $("#foto2");
        let fotoThree = $("#foto3");
        let fotoFour = $("#foto4");

        let fotoOnePadre = fotoOne.parent().attr("id");
        console.log(fotoOnePadre);

        if (fotoOnePadre === "destino3"){
            $("#destino3").css("background-color", "lightgreen");
        }else{
            $("#destino3").css("background-color", "lightcoral");

        }

        let fotoTwoPadre = fotoTwo.parent().attr("id");

        if (fotoTwoPadre === "destino1"){
            $("#destino1").css("background-color", "lightgreen");
        }else{
            $("#destino1").css("background-color", "lightcoral");
        }

        let fotoThreePadre = fotoThree.parent().attr("id");

        if (fotoThreePadre === "destino4"){
            $("#destino4").css("background-color", "lightgreen");
        }else{
            $("#destino4").css("background-color", "lightcoral");
        }

        let fotoFourPadre = fotoFour.parent().attr("id");

        if (fotoFourPadre === "destino2"){
            $("#destino2").css("background-color", "lightgreen");
        }else{
            $("#destino2").css("background-color", "lightcoral");
        }

        if (fotoOnePadre === "destino3" && fotoTwoPadre === "destino1" && fotoThreePadre === "destino4" && fotoFourPadre === "destino2"){
            alert("Enhorabuena! Has ganado crack!!!");
            $("#sigNivel").css("display", "block");
        }
}

function siguienteNivel(){
    $("#sigNivel").css("display","none");
    $("td").css("background-color", "gray");
    $(".fila2").empty();
    $(".fila2").css("width", 200);
    let crearTd = $("<td id='text5'>");
    $("#columna").append(crearTd);

    let crearTdFila2 = $("<td class='fila2' id='destino5' dropzone='true' ondragover='recibir(event);' ondrop='soltando(event)'>")
    $("#columna2").append(crearTdFila2);
    
    $("#text1").text("Iluminador");
    $("#text2").text("Máscara de pestañas");
    $("#text3").text("Colorete");
    $("#text4").text("Pintalabios");
    $("#text5").text("Spray Fijador");

    $("#juego2").css("display","inline");
    $("#boton2").css("display", "block");

}
function comprobarJuego2(){
        let FirstPic = $("#fotoCol");
        let SecondPic = $("#fotoRim");
        let ThirdPic = $("#fotoLab");
        let FourPic = $("#fotoIlum");
        let FivePic = $("#fotoSpray");

        let FirstPicPadre = FirstPic.parent().attr("id");
        console.log(FirstPicPadre);
        
        if (FirstPicPadre === "destino3"){
            $("#destino3").css("background-color", "lightgreen");
        }else{
            $("#destino3").css("background-color", "lightcoral");

        }

        let SecondPicPadre = SecondPic.parent().attr("id");

        if (SecondPicPadre === "destino2"){
            $("#destino2").css("background-color", "lightgreen");
        }else{
            $("#destino2").css("background-color", "lightcoral");
        }

        let ThirdPicPadre = ThirdPic.parent().attr("id");

        if (ThirdPicPadre === "destino4"){
            $("#destino4").css("background-color", "lightgreen");
        }else{
            $("#destino4").css("background-color", "lightcoral");
        }

        let FourPicPadre = FourPic.parent().attr("id");

        if (FourPicPadre === "destino1"){
            $("#destino1").css("background-color", "lightgreen");
        }else{
            $("#destino1").css("background-color", "lightcoral");
        }
        
        let FivePicPadre = FivePic.parent().attr("id");

        if (FivePicPadre === "destino5"){
            $("#destino5").css("background-color", "lightgreen");
        }else{
            $("#destino5").css("background-color", "lightcoral");
        }

        if (FirstPicPadre === "destino3" && SecondPicPadre === "destino2" && ThirdPicPadre === "destino4" && FourPicPadre === "destino1" && FivePicPadre === "destino5"){
            alert("Enhorabuena! Has ganado crack!!!");
            $("#sigNivel").css("display", "none");
            $("#ultNivel").css("display", "block");
        }else{
            alert("Ohhh! Has perdido, inténtalo de nuevo.")
        }
}
function ultimoNivel(){
    $("td").css("background-color", "gray");
    $(".fila2").empty();
    let crearTd2 = $("<td id='text6'>");
    $("#columna").append(crearTd2);
    let crearTdFila3 = $("<td class='fila2' id='destino6' dropzone='true' ondragover='recibir(event);' ondrop='soltando(event)'>")
    $("#columna2").append(crearTdFila3);
    
    $("#text1").text("Nike");
    $("#text2").text("LG");
    $("#text3").text("McDonalds");
    $("#text4").text("Adidas");
    $("#text5").text("Charlotte Tilbury");
    $("#text6").text("Pepsi");

    $("#nike").css("width", 200);
    $("#nike").css("height", 150);

    $("#juego3").css("display","inline");
    $("#boton3").css("display", "block");
    $("#ultNivel").css("display", "none");

}
function comprobarJuego3(){
        let primer = $("#lg");
        let segun = $("#mcdo");
        let tercer = $("#pepsi");
        let cuarta = $("#charloteTi");
        let quinta = $("#nike");
        let sexta = $("#adidas");

        let primPadre = primer.parent().attr("id");
        console.log(primPadre);
        
        if (primPadre === "destino2"){
            $("#destino2").css("background-color", "lightgreen");
        }else{
            $("#destino2").css("background-color", "lightcoral");

        }

        let segunPadre = segun.parent().attr("id");

        if (segunPadre === "destino3"){
            $("#destino3").css("background-color", "lightgreen");
        }else{
            $("#destino3").css("background-color", "lightcoral");
        }

        let tercerPadre = tercer.parent().attr("id");

        if (tercerPadre === "destino6"){
            $("#destino6").css("background-color", "lightgreen");
        }else{
            $("#destino6").css("background-color", "lightcoral");
        }

        let cuartaPadre = cuarta.parent().attr("id");

        if (cuartaPadre === "destino5"){
            $("#destino5").css("background-color", "lightgreen");
        }else{
            $("#destino5").css("background-color", "lightcoral");
        }
        
        let quintaPadre = quinta.parent().attr("id");

        if (quintaPadre === "destino1"){
            $("#destino1").css("background-color", "lightgreen");
        }else{
            $("#destino1").css("background-color", "lightcoral");
        }

        let sextaPadre = sexta.parent().attr("id");

        if (sextaPadre === "destino4"){
            $("#destino4").css("background-color", "lightgreen");
        }else{
            $("#destino4").css("background-color", "lightcoral");
        }
        if (primPadre === "destino2" && segunPadre === "destino3" && tercerPadre === "destino6" && cuartaPadre === "destino5" && quintaPadre === "destino1" && sextaPadre == "destino4"){
            alert("Enhorabuena! Te has pasado todos los niveles!!!");
            $("#gif").css("display", "inline");
        }else{
            alert("Ohhh! Has perdido, inténtalo de nuevo.")
        }

}