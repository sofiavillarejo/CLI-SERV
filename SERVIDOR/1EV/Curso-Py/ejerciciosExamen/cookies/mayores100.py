#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

#el cliente NO me envia cookies -> crear cookie
#el cliente me envia cookies pero no esta la que busco -> crear cookie
#el cliente me envia cookies y esta la que busco -> leer cookie y modificar

import http.cookies, os

from urllib.parse import urlparse, parse_qs

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

num = int(param["numero"][0])

if num>=100:
    print("Content-type: text/html")#con esto se envia una cookie al cliente

    cookie = http.cookies.SimpleCookie()

    #si el navegador no tiene esa cookie
    if os.environ.get("HTTP_COOKIE") == None:
        cookie["mayores100"] = str(num)
        cookie["mayores100"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT"
        print(cookie)
        print()
    else:
        cookie.load(os.environ.get("HTTP_COOKIE")) #cargo todas las cookies que me envia el cliente en mi objeto cookie
        if "mayores100" not in cookie: #miro si esta mi cookie entre ellas y sino, la creo otra vez
            cookie["mayores100"] = str(num) #paso el numero a string para almacenarlo
            cookie["mayores100"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT"
            print(cookie)
            print()
        else:
            #la cookie si existe, asi que guardo los valores separados por un espacio
            #lo que tenia + espacio en blanco + numero valor
            cookie["mayores100"] = cookie["mayores100"].value + " " + str(num) #cojo lo que tenia la cookie, le añado un espacio y le añado el nuevo texto
            cookie["mayores100"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT"
            print(cookie)
            print()

else:
    print("Content-type: text/html\n")
    print("Introduce un numero mayor que 100")

if "mayores100" in cookie:

    print('''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>cookies</title>
        </head>
        <body>
    ''')
    listaNumeros = cookie["mayores100"].value.split(" ") #imprimir el contenido de la cookie
    print("<ol>")
    for item in listaNumeros:
        print(f"<li>{item}</li>")
    print("</ol>")

    print('''
    </body>
    </html>
    ''')