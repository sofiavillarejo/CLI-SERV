#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

#.py que crea una cookie para almacenar los valores introducidos por el usuario

import http.cookies, os

from urllib.parse import urlparse, parse_qs

print("Content-type: text/html\n")

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

text = param["texto"][0]

#crear cookie
cookie = http.cookies.SimpleCookie()
cookie["empiezaABC"] = text
#si el texto introducido contiene "ABC"
if "ABC" in text:
    print("dato almacenado")
else:
    print("este dato no se almacena")

text = []
print(cookie["empiezaABC"])
print()

#devolver formulario al cliente
print('''
      <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Separador de palabras</title>
    </head>
    <body>
        <form action="ej4_separaABC.py" method="get">
            <label for="texto">Texto:</label>
            <input type="text" name="texto" id=""><br />
            <input type="submit" value="Enviar" />
        </form>
    </body>
    </html>
''')
#enlace a la pagina para mostrar el contenido de la cookie
print('<a href="ej4_muestraABC.py">Mostrar contenido cookie</a>')


