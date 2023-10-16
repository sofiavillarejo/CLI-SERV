#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

import http.cookies, os

from urllib.parse import urlparse, parse_qs

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

usuario = param["usuario"][0]
passwd = param["passwd"][0]

dentro = False

if(usuario == "pepe") and (passwd == "1234"):
    dentro = True

if not dentro:
    print("Content-type: text/html\n")
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cookies</title>
    </head>
    <body>
        <h1>Cookies</h1>
        <h3> ERROR EN LA AUTENTICACIÓN
        <form action="cookie.py" method="get">
            <label for="usuario">Usuario</label>
            <input type="text" name="usuario" id=""><br />
            <label for="passwd">Password</label>
            <input type="text" name="passwd" id=""><br />
            <input type="submit" value="Entrar">
        </form>
    </body>
    </html>
    """)
else:
    print("Content-type: text/html")
    cookie = http.cookies.SimpleCookie()
    cookie["ID1"] = "algo"

    print(cookie)
    print()#linea en blanco
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cookies</title>
    </head>
    <body>
        <h1>Estás dentro</h1>
    </body>
    </html>
    """)

    #ORDEN DE LAS COSAS
    #1. PRINT(CONTENT-TYPE)
    #2.COOKIES
    #3. LÍNEA EN BLANCO
    #4.HTML
    