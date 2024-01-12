#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

import os
from urllib.parse import urlparse, parse_qs
import HtmlVideojuegos

from BDvideojuegos import BDVideojuegos
import HtmlVideojuegos

print("Content-Type: text/html\n")

ru= os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

bd = BDVideojuegos()

if "id" in param and param["id"][0] !="":
    #capturar el id a borrar
    id = param["id"][0]

    HtmlVideojuegos.formularioModificar(bd.seleccionarPorId(id))
else:
    HtmlVideojuegos.error("falta el id para modificar")

    bd.cerrarBD()