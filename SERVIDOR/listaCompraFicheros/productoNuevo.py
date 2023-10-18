#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\n")

import os
from urllib.parse import urlparse, parse_qs
import codigoHtml


ru= os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

dato = param["producto"][0]
fich = open("datos/listaCompra.dat", "at")

fich.write("\n"+dato)

fich.close()

#importamos html del otro archivo (crear cabecera)
codigoHtml.cabeceraHtml()

print("producto en la lista de productos")

#crear fin del html
codigoHtml.finHtml()
