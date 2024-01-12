#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe
print("Content-type: text/html\n")

import json
import os

try:
    fich = open("listaComida.dat")
except:
    fich = open("listaComida.dat", "x")

if os.path.getsize("listaComida.dat") != 0:
    listaComidas = json.load(fich)
else:
    listaComidas = []

def tablaDeComidas():
    print("<table border='1px'>")
    print("<tr><th>Comida favorita</th></tr>")
    for comida in listaComidas:
        print(f"<tr><td>{comida}</th></tr>")
    print("</table>")

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

tablaDeComidas()

print("""
    </body>
    </html>
""")