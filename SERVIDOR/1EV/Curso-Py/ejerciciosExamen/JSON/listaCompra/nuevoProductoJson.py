#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe
print("Content-type: text/html\n")

import json
import os
from urllib.parse import urlparse, parse_qs

ru= os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

#variable producto que quiero guardar
prod = [param["producto"][0], param["cantidad"][0]] #lista con dos elementos

if os.path.getsize("listaCompra.dat") == 0:
    listaProductos = [prod] #añade a una lista los datos que recibe del formulario
    listaJson = json.dumps(listaProductos)
else:
    fich= open("listaCompra.dat")
    listaProductos = json.load(fich)
    fich.close()
    listaProductos.append(prod)
    listaJson = json.dumps(listaProductos)

fich = open("listaCompra.dat", "wt")
fich.write(listaJson)
fich.close()

print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="refresh" content="3; listaCompra.py">
        <title>Cesta de la compra</title>
    </head>
    <body>
        <h1>Cesta de la compra</h1>
        <h3>Producto apuntado</h3>
    </body>
    </html>
""")