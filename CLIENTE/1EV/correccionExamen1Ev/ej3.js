
function sonPares(listaNumeros){
	let res = true;

	for(n of listaNumeros){
		if(n%2 != 0){
			res = false;
		}
	}

	return res;
}

console.log(sonPares([1,2,3,4]));
console.log(sonPares([8,2,16,4,4,10]));

function sonPositivos(listaNumeros){
	let res = true;

	for(n of listaNumeros){
		if(n<0){
			res = false;
		}
	}

	return res;
}

console.log(sonPositivos([1,2,-3,4]));
console.log(sonPositivos([8,2,16,4,4,10]));
console.log(sonPositivos([]));