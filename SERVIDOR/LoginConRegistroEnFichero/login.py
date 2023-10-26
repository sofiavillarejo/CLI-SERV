#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import os, codigoHtml, json, hashlib, http.cookies, uuid
from urllib.parse import urlparse, parse_qs

ru= os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

#fichero con usuarios
fichUsu = "datos/usuarios.json"

if "nombre" not in param:
    codigoHtml.error("Falta el nombre")
    exit() #sale del python
if "passwd" not in param:
    codigoHtml.error("Falta la contraseña")
    exit()

nombre = param["nombre"][0]
passwd = param["passwd"][0]

#contraseña encriptada
pasEnc = (hashlib.sha512(str.encode(passwd))).hexdigest()

#obtener del fichero los usuarios registrados
with open(fichUsu) as fichero:
    try:
        listaUsuarios = json.load(fichero)
    except:
        listaUsuarios = []

#comprobar si el usuario existe
usuarioEncontrado = False
for usu in listaUsuarios:
    if usu[0]==nombre and usu[1]==pasEnc:
        usuarioEncontrado = True
        break

if not usuarioEncontrado:
        codigoHtml.error("Usuario NO ENCONTRADO o Password incorrecta")
        exit()

#para saber que el usuario ha entrado en sesion y puede navegar
print("Content-type: text/html")
cookie = http.cookies.SimpleCookie()
cookie["ID1"] = uuid.uuid4() #para generar identificadores aleatorios
print(cookie)
print()

print('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="refresh" content="0; pagina1.py">
        <title>Login con registro en fichero</title>
    </head>
    <body>
        <h1>CORRECTO</h1>
        </body>
        </html>
''')
codigoHtml.correcto()
