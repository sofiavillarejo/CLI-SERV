#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\n")

import json
import os
from urllib.parse import urlparse, parse_qs
import codigoHtml


ru= os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

#variable producto que quiero guardar
prod = [param["producto"][0], param["cantidad"][0]] #lista con dos elementos

if os.path.getsize("datos/listaCompra.dat") == 0: 
    listaProductos = [prod] #lista que contiene los productos
    listaJson = json.dumps(listaProductos) #convierte algo en formato json

else:
    fich = open("datos/listaCompra.dat")
    listaProductos = json.load(fich) # lee el contenido del fichero y lo convierte en una lista de productos
    fich.close()
    listaProductos.append(prod)#añado el producto a la lista
    listaJson = json.dumps(listaProductos) #convierte algo en formato json

fich = open("datos/listaCompra.dat", "wt")#si existe el fichero, me cargo lo que tiene dentro y escribo
fich.write(listaJson)#escribo en el fichero
fich.close()#cierro el fichero

#crear la salida HTML
codigoHtml.htmlRecarga()