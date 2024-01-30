#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe
#EJERCICIO LEER DOS FICHEROS CON VARIAS LINEAS
import os
from urllib.parse import urlparse, parse_qs

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

precioCorte = float(param["precio_corte"][0])

print("Content-type: text/plain\n")

fich = open("productos.txt")
fich2 = open("precios.txt")

contenido = fich.readlines()
contenido2 = fich2.readlines()

fich.close()
fich2.close()

nuevoFich = open("filtroPrecios.txt", "wt")

for cont in range(len(contenido)):
    print(cont)
    if float(contenido2[cont]) >= precioCorte:
            print(contenido[cont], contenido2[cont])
            nuevoFich.write(contenido[cont])
nuevoFich.close()

print("""<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Mostrar contenido ficheros</title>
                </head>
                <body>
            """)

print("<h1>Filtro realizado</h1>")      

print("""
    </body>
    </html>
""")