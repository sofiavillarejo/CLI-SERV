$(document).ready(function() {
    let images = [
        'perro.png',
        'corazon.png',
        'gato.png'
    ];

    let darVueltaCartas = [];
    let intentos = 0
    let maxIntentos = 4

    function shuffle(array) {
        return array.sort(() => Math.random() - 0.5);
    }

    function createCard(imagen) {
        let card = $('<div class="card"></div>');
        let cardImage = $('<img>').attr('src', imagen);

        card.append(cardImage);
        card.on('click', voltearCarta);
        return card;
    }

    function resetGame() {
        $('.card').remove();
        $("#salida").html("");
        let shuffledImages = shuffle(images.concat(images));
        shuffledImages.forEach(function(imagen) {
            let card = createCard(imagen);
            $('#tablero').append(card);
            
        });
    }

    function voltearCarta() {
        
        if (!$(this).hasClass('volteada') && darVueltaCartas.length < 2) {
            $(this).addClass('volteada');
            darVueltaCartas.push($(this));
            if (darVueltaCartas.length === 2) {
                setTimeout(checkMatch, 300);
            }
        }
    }

    function checkMatch() {
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
        checkWin();
    }

    function checkWin() {
        if ($('.matched').length === images.length * 2) {
            $("#salida").text("¡Has ganado!");
            $("#salida").slideUp(1000);
            $("#salida").slideDown(1000);
        }
    }

    $('#boton').on('click', resetGame);

    resetGame();
});