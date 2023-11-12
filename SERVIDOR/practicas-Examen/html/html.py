#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe

print("Content-type: text/html\n")

import os
from urllib.parse import urlparse, unquote, parse_qs

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])#siempre 4

peso = float(param["peso"][0])
nombre = param["nombre"][0]
edad = int(param["edad"][0])

print("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Datos</title>
    </head>
    <body>
    <h1>TU peso es de: </h1>
    </body>
    </html>

""")
salida = "Tus datos son {}, {} y {}. <br/>"
print(salida.format("nombre", peso, edad))
print(f"Tu nombre es {nombre}, pesas {peso} kilos y tu edad es {edad} años." + "<br/>")
print(peso, nombre, edad)

productos = ["Manzana", "Albaricoque", "Pera"]
print("<br/>")
print(productos)
print("<br/>")

print("<ol>")
for prod in productos:
    print(f"<li>Producto: {prod} </li>")
print("</ol>")

cantidades = [2, 3, 5]

#recorrer dos listas a la vez e imprimirlas en una tabla
print("<table border=1>")
print(f"<th>Producto</th><th>Cantidad</th>")
for tupla in zip(productos, cantidades): 
    print("<tr>")
    print(f"<td>{tupla[0]}</td><td>{tupla[1]}</td>")
    print("</tr>")
print("</table>")



