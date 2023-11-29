#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe

import json
import os


print("Content-type: text/html\n")

try:
    fich = open("listaCompra.dat")
except:
    fich = open("listaCompra.dat", "x")

if os.path.getsize("listaCompra.dat") != 0:
    productos = json.load(fich)
else:
    productos = []

fich.close()

def listadeProductos():
    if len(productos) !=0:
        print("<ol>")
        for prod in productos:
            print(f"<li>{prod[1]} de {prod[0]}</li>")
        print("</ol>")
    else:
        print("<h1>Lista de la compra vacia</h1>")
    print("<hr/>")

print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cesta de la compra</title>
    </head>
    <body>
        <h1>Cesta de la compra</h1>
    """)

listadeProductos()

print("""
    </body>
    </html>
""")