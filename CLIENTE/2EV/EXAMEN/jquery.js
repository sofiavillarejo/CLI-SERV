/*SELECTORES
    -clase: $(".clase").accion()
    -id: $("#id").accion()
    -cualquier elemento html: $("p").accion() --> aqui se aplicaria a los parrafos
    -elemento actual: $(this).accion()
    -todos los p con la clase intro: $("p.intro").accion()
*/

/*   EVENTO DOCUMENT READY--> sirve para evitar que se ejecute cualquier codigo de js antes de que el documento termine de cargarse. HACERLO SIEMPRE

        --forma1--
        $(principal);

        function principal(){
            alert("una forma");
        }
-------------------------------------------------
        --forma 2--
        $(document).ready(function(){
            alert("otra forma");
        })
-------------------------------------------------
        --forma 3--
        $(function(){
            alert("ultima forma");
        })
*/

/*  EVENTOS--> acciones de los visitantes a las que puede responder una web

Mouse 	        Keyboard 	Form 	Document/Window 
---------------------------------------------------------
click	        keypress	submit	    load
dblclick	    keydown	    change	    resize
mouseenter	    keyup	    focus	    scroll
mouseleave	 	            blur	    unload
*/

/*  EFECTOS
    -animate()--> Ejecuta una animación personalizada en los elementos seleccionados.
    -clearQueue()--> Elimina todas las funciones restantes en cola de los elementos seleccionados 
    -delay()-->	Establece un retraso para todas las funciones en cola en los elementos seleccionados
    -dequeue()--> Elimina la siguiente función de la cola y luego ejecuta la función.
    -fadeIn()--> Se desvanece en los elementos seleccionados.
    -fadeOut()--> Desvanece los elementos seleccionados
    -fadeTo()--> Funde/aparece los elementos seleccionados hasta una opacidad determinada
    -fadeToggle()--> Alterna entre los métodos fadeIn() y fadeOut()
    -finish()--> Detiene, elimina y completa todas las animaciones en cola para los elementos seleccionados.
    -queue()--> Muestra las funciones en cola en los elementos seleccionados ($("span").text(div.queue().length);)--> saca en un p el numero total de animaciones que tiene
    -hide()--> Esconde los elementos seleccionados
    -show()--> Muestra los elementos seleccionados (por si habiamos usado hide())
    -toggle()--> Alterna entre los métodos hide() y show()
    -slideDown()-->	Desliza hacia abajo (muestra) los elementos seleccionados
    -slideUp()--> Desliza hacia arriba (oculta) los elementos seleccionados
    -slideToggle()--> Alterna entre los métodos slideUp() y slideDown()
    -stop()--> Detiene la animación actualmente en ejecución para los elementos seleccionados.
*/
/*  MÉTODOS HTML/CSS
    !-addClass()--> Agrega uno o más nombres de clase a los elementos seleccionados.
    !-after()-->	Inserta contenido después de los elementos seleccionados.
    !-append()--> Inserta contenido al final de los elementos seleccionados.
    -appendTo()--> Inserta elementos HTML al final de los elementos seleccionados.
    -attr()--> Establece o devuelve atributos/valores de elementos seleccionados
    !-before()--> Inserta contenido antes de los elementos seleccionados.
    -clone()--> Hace una copia de los elementos seleccionados.
    !-css()--> Establece o devuelve una o más propiedades de estilo para elementos seleccionados
    -detach()--> Elimina elementos seleccionados (mantiene datos y eventos)
    !-empty()--> Elimina todos los nodos secundarios y el contenido de los elementos seleccionados.
    -hasClass()-->Comprueba si alguno de los elementos seleccionados tiene un nombre de clase específico
    -height()--> Establece o devuelve la altura de los elementos seleccionados.
    !-html()-->	Establece o devuelve el contenido de los elementos seleccionados.
    -innerHeight()--> Devuelve la altura de un elemento (incluye relleno, pero no borde)
    -innerWidth()--> Devuelve el ancho de un elemento (incluye relleno, pero no borde)
    -insertAfter()--> Inserta elementos HTML después de los elementos seleccionados.
    -insertBefore()--> Inserta elementos HTML antes de los elementos seleccionados.
    -offset()--> Establece o devuelve las coordenadas de desplazamiento para los elementos seleccionados (en relación con el documento)
    -offsetParent()--> Devuelve el primer elemento padre posicionado
    -outerHeight()--> Devuelve la altura de un elemento (incluye relleno y borde)
    -outerWidth()--> Devuelve el ancho de un elemento (incluye relleno y borde)
    -position()--> Devuelve la posición (relativa al elemento padre) de un elemento
    !-prepend()--> Inserta contenido al principio de los elementos seleccionados.
    -prependTo()--> Inserta elementos HTML al principio de los elementos seleccionados.
    -prop()--> Establece o devuelve propiedades/valores de elementos seleccionados
    !-remove()--> Elimina los elementos seleccionados (incluidos datos y eventos)
    !-removeAttr()--> Elimina uno o más atributos de los elementos seleccionados.
    !-removeClass()--> Elimina una o más clases de los elementos seleccionados.
    -removeProp()--> Elimina una propiedad establecida por el método prop()
    -replaceAll()--> Reemplaza los elementos seleccionados con nuevos elementos HTML
    -replaceWith()--> Reemplaza elementos seleccionados con contenido nuevo
    -scrollLeft()--> Establece o devuelve la posición de la barra de desplazamiento horizontal de los elementos seleccionados
    -scrollTop()--> Establece o devuelve la posición de la barra de desplazamiento vertical de los elementos seleccionados
    !-text()--> Establece o devuelve el contenido de texto de los elementos seleccionados.
    !-toggleClass()--> Alterna entre agregar/eliminar una o más clases de elementos seleccionados
    -unwrap()--> Elimina el elemento padre de los elementos seleccionados.
    !-val()--> Establece o devuelve el atributo de valor de los elementos seleccionados (para elementos de formulario)
    -width()--> Establece o devuelve el ancho de los elementos seleccionados.
    -wrap()--> Envuelve los elementos HTML alrededor de cada elemento seleccionado
    -wrapAll()--> Envuelve los elementos HTML alrededor de todos los elementos seleccionados
    -wrapInner()--> Envuelve los elementos HTML alrededor del contenido de cada elemento seleccionado
*/

/* DIFERENCIA ENTRE .HTML() Y .TEXT()
    .html():
        -Si le preguntas a un elemento qué hay dentro de él, .html() te dará la respuesta con todo, incluyendo formato y etiquetas HTML.
        -Si le dices al elemento "quiero que dentro de ti haya esto", .html() tomará eso y lo pondrá tal cual, incluso si son etiquetas HTML.

    .text():
        -Si le preguntas a un elemento qué hay dentro de él, .text() solo te dará el texto sin incluir el formato ni las etiquetas HTML.
        -Si le dices al elemento "quiero que dentro de ti haya esto", .text() tomará eso y lo pondrá como texto plano, sin interpretar como HTML.
*/