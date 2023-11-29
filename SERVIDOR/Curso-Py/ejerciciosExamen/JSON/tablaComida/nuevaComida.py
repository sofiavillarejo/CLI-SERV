#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe
print("Content-type: text/html\n")

import json
import os
from urllib.parse import urlparse, parse_qs

ru= os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

#variable producto que quiero guardar
comid = param["comida"][0]


if os.path.getsize("listaComida.dat") == 0:
    listaComidas = [comid]
    listaJsonComidas = json.dumps(listaComidas)
else:
    fich = open("listaComida.dat")
    listaComidas = json.load(fich)
    fich.close()
    listaComidas.append(comid)
    listaJsonComidas = json.dumps(listaComidas)

fich= open("listaComida.dat", "wt")
fich.write(listaJsonComidas)
fich.close()

print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="refresh" content="3; tablaComida.py">
        <title>Comidas favoritas</title>
    </head>
    <body>
        <h1>Comidas favoritas</h1>
        <h3>comida apuntado</h3>
    </body>
    </html>
""")