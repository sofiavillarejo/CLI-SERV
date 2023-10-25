#!C:\Users\zx20student109\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import os, codigoHtml
from urllib.parse import urlparse, parse_qs

ru= os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

"""
validar que nos envian los parametros
que existen
que contienen algo
que cumplen los requisitos, p.e : la passwd sea de mas de 4 caracteres

el objetivo es guardar el nuevo usuario en el fichero de usuarios

abrir  el fichero de usuarios -> JSON

comprobar que el usuaro no existe en la lista de usuarios

si no existe -> se añade y se vuelve a la pag principal

si existe -> ir a la página de error 

formato de la estructura de datos para la lista de usuarios
[["usuario1", "1234", "usu1@miempresa.com"],["usuario2", "3456", "usu2@mitienda.com"]]
"""
if "nombre" not in param:
    codigoHtml.error()
    exit()
if "passwd" not in param:
    codigoHtml.error()
if "email" not in param:
    codigoHtml.error()

codigoHtml.correcto()

