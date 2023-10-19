#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\n")

import json, codigoHtml, random
import os
from urllib.parse import urlparse, parse_qs

ru= os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

#variable producto que quiero guardar
nCuentaAleatorio = random.randint(100000, 999999)
cuenta = [nCuentaAleatorio, 0]

if os.path.getsize("datos/listaCuentas.dat") == 0: 
    listaCuentas = [cuenta] #lista que contiene los productos
    listaJson = json.dumps(listaCuentas) #convierte algo en formato json

else:
    fich = open("datos/listaCuentas.dat")
    listaCuentas = json.load(fich) # lee el contenido del fichero y lo convierte en una lista de productos
    fich.close()
    listaCuentas.append(cuenta)#añado el producto a la lista
    listaJson = json.dumps(listaCuentas) #convierte algo en formato json

fich = open("datos/listaCuentas.dat", "wt")#si existe el fichero, me cargo lo que tiene dentro y escribo
fich.write(listaJson)#escribo en el fichero
fich.close()#cierro el fichero

#crear la salida HTML
codigoHtml.htmlRecarga()