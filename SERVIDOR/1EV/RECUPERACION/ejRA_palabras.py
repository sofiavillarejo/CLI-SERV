#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

import http.cookies, os

from urllib.parse import urlparse, parse_qs

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

texto = param["palabra"][0]

vocales = ("A", "E", "I", "O", "U")
if texto.startswith(vocales):
    print("Content-type: text/html")#con esto se envia una cookie al cliente
    cookie = http.cookies.SimpleCookie()
    #si el navegador no tiene esa cookie
    if os.environ.get("HTTP_COOKIE") == None:
        cookie["palabrasVocales"] = texto
        cookie["palabrasVocales"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT"
        print(cookie)
        print()
    else:
        cookie.load(os.environ.get("HTTP_COOKIE")) #cargo todas las cookies que me envia el cliente en mi objeto cookie
        if "palabrasVocales" not in cookie: #miro si esta mi cookie entre ellas y sino, la creo otra vez
            cookie["palabrasVocales"] = texto
            cookie["palabrasVocales"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT"
            print(cookie)
            print()
        else:
            cookie["palabrasVocales"] = cookie["palabrasVocales"].value + " " + texto #cojo lo que tenia la cookie, le añado un espacio y le añado el nuevo texto
            cookie["palabrasVocales"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT"
            print(cookie)
            print()
else:
    print("Content-type: text/html")#con esto se envia una cookie al cliente
    cookie = http.cookies.SimpleCookie()
    #si el navegador no tiene esa cookie
    if os.environ.get("HTTP_COOKIE") == None:
        cookie["palabrasConsonantes"] = texto
        cookie["palabrasConsonantes"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT"
        print(cookie)
        print()
    else:
        cookie.load(os.environ.get("HTTP_COOKIE")) #cargo todas las cookies que me envia el cliente en mi objeto cookie
        if "palabrasConsonantes" not in cookie: #miro si esta mi cookie entre ellas y sino, la creo otra vez
            cookie["palabrasConsonantes"] = texto
            cookie["palabrasConsonantes"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT"
            print(cookie)
            print()
        else:
            cookie["palabrasConsonantes"] = cookie["palabrasConsonantes"].value + " " + texto #cojo lo que tenia la cookie, le añado un espacio y le añado el nuevo texto
            cookie["palabrasConsonantes"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT"
            print(cookie)
            print()

print("""<!DOCTYPE html>
   <html>
   <head>
       <title>Ejercicio 4</title>
   </head>
   <body>
       <form action="ejRA_palabras.py" method="get">
           <label for="palabra">Palabra:</label>
           <input type="text" name="palabra"/>
           <input type="submit" value="Enviar" />
       </form>
   </body>
   </html>
""")