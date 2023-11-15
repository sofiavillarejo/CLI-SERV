/*document -> donde se "carga" la web que se esta representando en el navegador. Es el punto de entrada a los elementos de la página.
PROPIEDADES:
    - attributes
    - className
    - id
    - innerHtml
    - outerHtml
    - ariaXXXXX
    - hidden
    - draggable
    - innerText
    - style
    - ...
*/
/* ESCOGER EELEMENTOS DE LA WEB QUE VOY A MODIFICAR, AÑADIR, ELIMINAR... MAS TARDE
    función:
        - .getElementById('id') -> un elemento con id concreto
        - .getElementsByTagName('tagName') -> varios elementos de una etiqueta determinada
        - .getElementsByClass('class') -> varios elementos hijos de una clase determinada
        - .querySelector('css selector') -> un primer elemento del documento que cumple con el selector
        - .querySelectorAll('css selector') -> varios elementos del documento que cumplen con el selector

PROPIEDADES PARA SELECCIONAR:
    - .documentElement -> un elemento del html
    - .body, .forms, .head, .images... -> todos los elementos de ese tipo del documento

    ejemplo:
    html-> ... <li id="especial">Opción 3</li>
    let especial = document.getElementById("especial");
    special.stye.color = "red";
*/