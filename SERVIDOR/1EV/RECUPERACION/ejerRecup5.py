#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

import os
from urllib.parse import urlparse, parse_qs

print("Content-type:text/plain\n")

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

valor = param["tipo"][0]

#abrimos el fichero de numeros
fich = open("numeros.dat") 
listaNumeros = [num.strip('\n') for num in fich.readlines()]#guardo cada una de las lineas que voy leyendo y quito el \n
#recorrer elementos del fichero
for num in listaNumeros:
        #separamos los elementos por espacios en blanco y se guardan en una lista cada uno
    elem = num.split(" ")
        # print(elem[0])
    if elem[1] == "A":
        suma = 0
        suma+=int(elem[0])
        print(suma)
    
f = open("resultado.dat", "wt")
f.write(suma)



    

