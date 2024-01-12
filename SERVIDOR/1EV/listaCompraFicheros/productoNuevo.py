#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\n")

import os
from urllib.parse import urlparse, parse_qs
import codigoHtml


ru= os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

prod = param["producto"][0]
cant = param["cantidad"][0]

fich = open("datos/listaCompra.dat", "at")

if os.path.getsize("datos/listaCompra.dat") != 0: 
    fich.write("\n")

fich.write(prod + " ; " + cant)#escribimos el producto y la cantidad

fich.close()

#crear la salida HTML
codigoHtml.htmlRecarga()
