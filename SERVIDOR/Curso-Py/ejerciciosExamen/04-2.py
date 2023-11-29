#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe

import http.cookies, os

from urllib.parse import urlparse, parse_qs

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

number = int(param["numero"][0])

if number >=100:
    print("Content-type: text/html")
    cookie = http.cookies.SimpleCookie()
    #si no existe la cookie, la creo
    if os.environ.get("HTTP_COOKIE") == None:
        cookie["mayores100"] = str(number)
        cookie["mayores100"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT"
        print(cookie)
        print()
    else:
        cookie.load(os.environ.get("HTTP_COOKIE"))
        #compruebo que la cookie que necesito esta y sino, la creo de nuevo
        if "mayores100" not in cookie:
            cookie["mayores100"] = str(number)
            cookie["mayores100"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT"
            print(cookie)
            print()
        else:
            cookie["mayores100"] = cookie["mayores100"].value + " " + str(number) 
            cookie["mayores100"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT"
            print(cookie)
            print()

else:
    print("Content-type: text/html\n")