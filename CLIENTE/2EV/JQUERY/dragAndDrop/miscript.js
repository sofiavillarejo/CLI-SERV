//funcion que se ejecuta cuando empiezas a arrastrar el elemento
function arrastrando(event) {
    console.log(event.target.id);
    event.dataTransfer.setData('text/plain', event.target.id);
    event.currentTarget.style.backgroundColor = 'yellow';
}

//funcion que se ejecuta cuando sueltas el elemento
function soltando(event) {
    event.dataTransfer.setData('text/plain', event.target.id);
    event.currentTarget.style.backgroundColor = 'pink';
    const id = event.dataTransfer.getData('text');
    console.log("destino:" + event.target.id);
}

function recibir(event) {
    event.preventDefault();
    console.log(event.target.id);
}