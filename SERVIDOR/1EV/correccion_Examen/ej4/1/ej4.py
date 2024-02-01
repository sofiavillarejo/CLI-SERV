#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe

#trabjar con cookies
#tratar la info que va en la cookie

#los casos son:
#el cliente no me envia cookies -> crear cookie
#el cliente me envia cookies pero no esta la que busco -> crear cookie
#el cliente me envia cookies y esta la que busco -> leer cookie y modificar

import http.cookies, os

from urllib.parse import urlparse, parse_qs

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

text = param["texto"][0]

#diferentes maneras de ver el contenido
# print(text[0], text[1], text[2])

# print(text[0:3])

#print(text.startswith("ABC"))

if text.startswith("ABC"):
    print("Content-type: text/html")#con esto se envia una cookie al cliente
    cookie = http.cookies.SimpleCookie()
    #si el navegador no tiene esa cookie
    if os.environ.get("HTTP_COOKIE") == None:
        cookie["empiezaABC"] = text
        cookie["empiezaABC"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT"
        print(cookie)
        print()
    else:
        cookie.load(os.environ.get("HTTP_COOKIE")) #cargo todas las cookies que me envia el cliente en mi objeto cookie
        if "empiezaABC" not in cookie: #miro si esta mi cookie entre ellas y sino, la creo otra vez
            cookie["empiezaABC"] = text
            cookie["empiezaABC"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT"
            print(cookie)
            print()
        else:
            cookie["empiezaABC"] = cookie["empiezaABC"].value + " " + text #cojo lo que tenia la cookie, le añado un espacio y le añado el nuevo texto
            cookie["empiezaABC"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT"
            print(cookie)
            print()

else:
    print("Content-type: text/html\n")