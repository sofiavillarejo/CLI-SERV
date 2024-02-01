$(document).ready(function() {
    let images = [
        'perro.png',
        'corazon.png',
        'gato.png'
    ];

    let darVueltaCartas = [];

    function barajarCartas(array) {
        return array.sort(() => Math.random() - 0.5);
    }

    function crearCartas(imagen) {
        let card = $('<div class="card"></div>');
        let cardImage = $('<img>').attr('src', imagen);

        card.append(cardImage);
        card.on('click', voltearCarta);
        return card;
    }

    function reiniciarJuego() {
        //borrar cartas
        $('.card').remove();
        $("#salida").html("");
        let barajarCartasdImages = barajarCartas(images.concat(images));
        barajarCartasdImages.forEach(function(imagen) {
            let card = crearCartas(imagen);
            $('#tablero').append(card); 
        });
    }

    function voltearCarta() {
        if (!$(this).hasClass('volteada') && darVueltaCartas.length < 2) {
            $(this).addClass('volteada');
            darVueltaCartas.push($(this));
            if (darVueltaCartas.length === 2) {
                //tras el temporizador, se ejecuta
                setTimeout(mirarCartas, 300);
            }
        }
    }

    function mirarCartas() {
        let card1 = darVueltaCartas[0].find('img').attr('src');
        let card2 = darVueltaCartas[1].find('img').attr('src');

        if (card1 === card2) {
            darVueltaCartas.forEach(function(card) {
                card.addClass('matched');
            });
        } else {
            darVueltaCartas.forEach(function(card) {
                card.removeClass('volteada');
            });
        }

        darVueltaCartas = [];
        ganador();
    }

    function ganador() {
        if ($('.matched').length === images.length * 2) {
            $("#salida").text("¡Has ganado!");
            $("#salida").slideUp(1000);
            $("#salida").slideDown(1000);
        }
    }

    $('#boton').on('click', reiniciarJuego);

    reiniciarJuego();
});