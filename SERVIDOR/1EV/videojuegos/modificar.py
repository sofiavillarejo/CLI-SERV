#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe
import os, sys
from urllib.parse import urlparse, parse_qs

from BDvideojuegos import BDVideojuegos
import HtmlVideojuegos

print("Content-Type: text/html\n")

ru= os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

#acceder a la base de datos
bd = BDVideojuegos()

if "nombre" in param and param["nombre"][0] !="" \
    and "empresa" in param and param["empresa"][0] !="" \
    and "tematica" in param and param["tematica"][0] !="" \
    and "nJug" in param and param["nJug"][0] !="" \
    and "anio" in param and param["anio"][0] !=""\
    and "id" in param and param["id"][0] !="":
        
    
    nombre = param["nombre"][0]
    empresa = param["empresa"][0]
    tematica = param["tematica"][0]
    nJug = param["nJug"][0]
    anio = param["anio"][0]
    id = param["id"][0]

    bd.modificar(id,nombre, empresa, tematica, nJug, anio)

    HtmlVideojuegos.error("Dato modificado")

else:
    HtmlVideojuegos.error("algún parámetro no es correcto")

#cerrar BBDD
bd.cerrarBD()