#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe

import http.cookies, os

from urllib.parse import urlparse, parse_qs

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

text = param["texto"][0]

if text.startswith("ABC"):
    print("Content-type: text/html")
    cookie = http.cookies.SimpleCookie()
    #si no existe la cookie, la creo
    if os.environ.get("HTTP_COOKIE") == None:
        cookie["empiezaABC"] = text
        cookie["empiezaABC"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT"
        print(cookie)
        print()
    #si existe, cargo las cookies
    else:
        cookie.load(os.environ.get("HTTP_COOKIE"))
        #compruebo que la cookie que necesito esta y sino, la creo de nuevo
        if "empiezaABC" not in cookie:
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