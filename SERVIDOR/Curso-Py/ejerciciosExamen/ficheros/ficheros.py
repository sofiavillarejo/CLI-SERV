#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe
import os
from urllib.parse import urlparse, parse_qs

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

letra = param["letra"][0]

print("Content-type: text/plain\n")

fich = open("productos.txt")
fich2 = open("precios.txt")

contenido = fich.readline()
contenido2 = fich2.readline()

fich.close()
fich2.close()

# print(contenido, contenido2)
listaProducto = contenido.split(" ")
listaPrecios = contenido2.split(" ")

nuevoFich = open("filtroLetras.txt", "wt")

#se añade al fichero solo si contiene la letra que indique el usuario
for prod in listaProducto:
    print(prod)
    if prod.__contains__(letra):
        nuevoFich.write(prod+ "\n")

nuevoFich.close()

print("""<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Mostrar contenido cookie</title>
                </head>
                <body>
            """)

print("<h1>Filtro realizado</h1>")      

print("""
    </body>
    </html>
""")