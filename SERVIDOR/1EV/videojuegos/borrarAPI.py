#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

import os, json
from urllib.parse import urlparse, parse_qs

from BDvideojuegos import BDVideojuegos
import HtmlVideojuegos

print("Content-Type: text/html\n")

ru= os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

#acceder a la base de datos
bd = BDVideojuegos()

if "id" in param and param["id"][0] !="":
    #capturar el id a borrar
    id = param["id"][0]

    #borrar la BBDD
    bd.borrarPorId(id)
    print(json.dumps(True))

else:
    print(json.dumps(False))

#cerrar BBDD
bd.cerrarBD()