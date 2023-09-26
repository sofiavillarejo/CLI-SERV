#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\n")

#importa libreria y funciones 
import os 
from urllib.parse import urlparse, unquote, parse_qs 

print("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mi pagina</title>
    </head>
    <body>
    <h1>Tratar formulario </h1>
    """)

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4]) #el 4 cuenta los parametros de la oracion que os saca (cada = de la oracion)s

print(param['nombre'][0])
print("<br />")
print(param['edad'][0])

print("""
</body>
</html>
""")