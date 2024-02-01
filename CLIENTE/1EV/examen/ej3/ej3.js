onload = sonPositivos
function sonPositivos() {
    console.log("hola");
    let numeros = [2,4,6,8];
    let numeros2 = [-2, 4, -6, 8];
    for (num of numeros){
        if (num>0){
            console.log(numeros);
            return true;
        }else if(num<0){
            return false;
        }
    }
    for (num of numeros2){
        if (num<0){
            console.log(numeros2);
            return false;
        }
    }
}