#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

#para poder leer los aprametros que se introducen en el servidor
import os
from urllib.parse import urlparse, unquote, parse_qs

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])#siempre 4

#peso y altura
peso = float(param["peso"][0])
altura = float(param["altura"][0])

#operacion para calcular el IMC
IMC = (peso / (altura*altura))

#html para meter el encabezado de resultado
print("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Calculadora de IMC</title>
    </head>
    <body>
    <h1>TU IMC es de: </h1>
    </body>
    </html>

""")
#imprimir el resultado el pantalla
print(round(IMC,2))