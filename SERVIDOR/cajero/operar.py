#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

print("Context-Type: text/html\n")

import os,json
from urllib.parse import urlparse, unquote, parse_qs

import codigoHtml

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

numCuenta = int(param["numC"][0]) -1
cant = int(param["c"][0])
oper = param["operacion"][0]

fich = open("datos/listaCuentas.dat")
listaCuentas = json.load(fich)
fich.close()

if oper == "Ingresar":
    listaCuentas[numCuenta][1] += cant
    listaCuentas[numCuenta][2].append(cant)
    fich = open("datos/listaCuentas.dat","wt")
    fich.write(json.dumps(listaCuentas))
    fich.close()
    codigoHtml.ingRet()
else:
    if listaCuentas[numCuenta][1] >= cant:
        listaCuentas[numCuenta][1] -= cant
        listaCuentas[numCuenta][2].append(-cant) #añado a la lista de cuentas en la tercera posición el valor de la cantidad que ingreso o retiro
        fich = open("datos/listaCuentas.dat","wt")
        fich.write(json.dumps(listaCuentas))
        fich.close()
        codigoHtml.ingRet()
    else:
        codigoHtml.error()




