function validarEmail() {
    // Obtener el valor del campo de entrada
    let email = $("#email").val();

    // Hacer la petición AJAX
    $.ajax({
        url: "/2DAW/CLIENTE/2EV/EXAMEN/practica/AJAX/ajaxConPy/ajax.py",
        method: "GET",
        data: { email: email },
        success: function(response) {
            if (response === "true") {
                $("#salida1").text("Es un correo electrónico correcto.");
            } else {
                $("#salida1").text("NO es un correo electrónico correcto.");
            }
        },
        error: function() {
            console.error("Error al realizar la solicitud.");
        }
    });
}
