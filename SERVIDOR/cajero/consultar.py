#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe
print("Context-Type: text/html\n")

import os,json, codigoHtml
from urllib.parse import urlparse, unquote, parse_qs

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

numCuenta = param["numC"][0]

fich = open("datos/listaCuentas.dat")
listaCuentas = json.load(fich)
fich.close()
historial = ""

for x in listaCuentas:
    if x[0] == int(numCuenta):
        transacciones = x[2]
        break
for operacion in transacciones:
    if operacion > 0:
        historial = historial + "<li style='color: green;'>Ingreso: "+ str(operacion) + "</li>"
    else:
        historial = historial + "<li style='color: red;'> Gasto: "+ str(operacion) + "</li>"

codigoHtml.consultarCuenta(numCuenta, historial)
