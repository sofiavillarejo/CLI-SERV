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
    -queue()--> Muestra las funciones en cola en los elementos seleccionados.
    -hide()--> Esconde los elementos seleccionados
    -show()--> Muestra los elementos seleccionados (por si habiamos usado hide())
    -toggle()--> Alterna entre los métodos hide() y show()
    -slideDown()-->	Desliza hacia abajo (muestra) los elementos seleccionados
    -slideUp()--> Desliza hacia arriba (oculta) los elementos seleccionados
    -slideToggle()--> Alterna entre los métodos slideUp() y slideDown()
    -stop()--> Detiene la animación actualmente en ejecución para los elementos seleccionados.
*/
/*  MÉTODOS HTML/CSS
    -addClass()--> Adds one or more class names to selected elements
    -after()-->	Inserts content after selected elements
    -append()--> Inserts content at the end of selected elements
    -appendTo()--> Inserts HTML elements at the end of selected elements
    -attr()--> Sets or returns attributes/values of selected elements
    -before()--> Inserts content before selected elements
    -clone()--> Makes a copy of selected elements
    -css()--> Sets or returns one or more style properties for selected elements
    -detach()--> Removes selected elements (keeps data and events)
    -empty()--> Removes all child nodes and content from selected elements
    -hasClass()-->	Checks if any of the selected elements have a specified class name
    -height()--> Sets or returns the height of selected elements
    -html()-->	Sets or returns the content of selected elements
    -innerHeight()--> Returns the height of an element (includes padding, but not border)
    -innerWidth()--> Returns the width of an element (includes padding, but not border)
    -insertAfter()--> Inserts HTML elements after selected elements
    -insertBefore()--> Inserts HTML elements before selected elements
    -offset()--> Sets or returns the offset coordinates for selected elements (relative to the document)
    -offsetParent()--> Returns the first positioned parent element
    -outerHeight()--> Returns the height of an element (includes padding and border)
    -outerWidth()--> Returns the width of an element (includes padding and border)
    -position()--> Returns the position (relative to the parent element) of an element
    -prepend()--> Inserts content at the beginning of selected elements
    -prependTo()--> Inserts HTML elements at the beginning of selected elements
    -prop()--> Sets or returns properties/values of selected elements
    -remove()--> Removes the selected elements (including data and events)
    -removeAttr()--> Removes one or more attributes from selected elements
    -removeClass()--> Removes one or more classes from selected elements
    -removeProp()--> Removes a property set by the prop() method
    -replaceAll()--> Replaces selected elements with new HTML elements
    -replaceWith()--> Replaces selected elements with new content
    -scrollLeft()--> Sets or returns the horizontal scrollbar position of selected elements
    -scrollTop()--> Sets or returns the vertical scrollbar position of selected elements
    -text()--> Sets or returns the text content of selected elements
    -toggleClass()--> Toggles between adding/removing one or more classes from selected elements
    -unwrap()--> Removes the parent element of the selected elements
    -val()--> Sets or returns the value attribute of the selected elements (for form elements)
    -width()--> Sets or returns the width of selected elements
    -wrap()--> Wraps HTML element(s) around each selected element
    -wrapAll()--> Wraps HTML element(s) around all selected elements
    -wrapInner()--> Wraps HTML element(s) around the content of each selected element
*/

/* DIFERENCIA ENTRE .HTML() Y .TEXT()
    .html():
        -Si le preguntas a un elemento qué hay dentro de él, .html() te dará la respuesta con todo, incluyendo formato y etiquetas HTML.
        -Si le dices al elemento "quiero que dentro de ti haya esto", .html() tomará eso y lo pondrá tal cual, incluso si son etiquetas HTML.

    .text():
        -Si le preguntas a un elemento qué hay dentro de él, .text() solo te dará el texto sin incluir el formato ni las etiquetas HTML.
        -Si le dices al elemento "quiero que dentro de ti haya esto", .text() tomará eso y lo pondrá como texto plano, sin interpretar como HTML.
*/