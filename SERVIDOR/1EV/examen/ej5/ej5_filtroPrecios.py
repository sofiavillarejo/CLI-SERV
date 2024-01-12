#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\n")

import os
from urllib.parse import urlparse, parse_qs

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

#cogemos los oparametros que ha introducido el usuario
precio = param["precio_corte"][0]

fich = open("productos.txt") 

productos = fich.readlines()

fich.close()
fich2 = open("precios.txt") 
precios = fich.readlines()
fich2.close()

try:
    fich3 = open("productos_filtrados.txt") 
except: 
    #se crea el fichero en datos si da error al abrir
    print("se crea el fichero")
    fich3 = open("productos_filtrados.txt")

fich3.close()



