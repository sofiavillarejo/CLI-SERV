//funcion que se ejecuta cuando empiezas a arrastrar el elemento
function arrastrando(event) {
    console.log(event.target.id);
    event.dataTransfer.setData('text/plain', event.target.id); //guardo dentro de setData el id y le doy el nombre de text para luego poder recuperarlo
    event.currentTarget.style.backgroundColor = 'yellow';
}

//funcion que se ejecuta cuando sueltas el elemento
function soltando(event) {
    event.currentTarget.style.backgroundColor = 'pink';
    const id = event.dataTransfer.getData('text');
    console.log("soltar:" + id);
    console.log("destino:" + event.target.id);

    let objQueArrastro = $("#" +id);
    let destino = $("#" + event.target.id);

    destino.append(objQueArrastro);
}

function recibir(event) {
    event.preventDefault();
    console.log(event.target.id);
}