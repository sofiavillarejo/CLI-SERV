#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

#trabjar con cookies
#tratar la info que va en la cookie

#los casos son:
#el cliente NO me envia cookies -> crear cookie
#el cliente me envia cookies pero no esta la que busco -> crear cookie
#el cliente me envia cookies y esta la que busco -> leer cookie y modificar

import http.cookies, os

from urllib.parse import urlparse, parse_qs

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

num = int(param["numero"][0]) #se convierte a entero para hacer la comparacion bien

if num >= 100: #si es mayor que 100, lo meto en la cookie

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
