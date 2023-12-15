function arrastrando(event) {
    console.log(event.target.id);
    event.dataTransfer.setData('text/plain', event.target.id); //guardo dentro de setData el id y le doy el nombre de text para luego poder recuperarlo
    event.currentTarget.style.backgroundColor = 'yellow';
}
