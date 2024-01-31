$(inicio);
function inicio() {
    //hide
    $("#elem1").click(function(){
        $(this).hide();
    });

    //show
    $("#btn1").click(function(){
        $("#elem1").show();
    });

    //toggle --> alterna los dos anteriores

    $("#btn2").click(function() {
        $("#elem2").toggle();
    });

    //fadeIn
    $("#fadeInCuad1").click(function() {
        $("#cuad1").fadeIn();
        $("#cuad2").fadeIn();
    }); 

    //fadeOut
    $("#cuad2").click(function() {
        $(this).fadeOut();
    });

    //fadeToggle
    $("#fadeTog").click(function() {
        $(".cuadrados").fadeToggle();
    });

    //animate --> animate({styles},speed,easing,callback) --> callback es poner el nombre de la funcion que se va a volver a reproudicr cuando termine esta
    $("#animate").click(function() {
        $("#cuad2").animate({height: "500px", width: "500px"}, 2000);
    });
    //animate con callback
    // $("#animateCallback").click(function(){
    // let div = $("#divAnimado");
    // startAnimation();
    // function startAnimation(){
    //     div.animate({height: 300}, "slow");
    //     div.animate({width: 300}, "slow");
    //     div.css("background-color", "pink");  
    //     div.animate({height: 100}, "slow");
    //     div.animate({width: 100}, "slow", startAnimation);
    // }
    // });

    //clearQueue
    $("#animateCallback").click(function(){
        let div = $("#divAnimado");
            div.animate({height: 300}, "slow");
            div.animate({width: 300}, "slow");
            div.css("background-color", "pink");  
            div.animate({height: 100}, "slow");
            div.animate({width: 100}, "slow");
    });
    $("#stopAnimate").click(function(){
        div.clearQueue(); //detiene los animate y no los vuelve a reproducir, lo borra todo
    })
    //finish --> lleva directamente al resultado final de la animacion
    $("#finishAnimate").click(function(){
        $("#cuad2").finish();
    });

    //slideUp y SlideDown
    $("#Sup").click(function(){
        $("p").slideUp();
    });
    $("#Sdown").click(function(){
        $("p").slideDown();
    });

    //slideToggle --> aparece hacia arriba y hacia abajo alternamente (hay que hacer click para que vaya alternando)
    $("#sToggle").click(function(){
        $("p").slideToggle();
    });




}



