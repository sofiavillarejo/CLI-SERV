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
}



