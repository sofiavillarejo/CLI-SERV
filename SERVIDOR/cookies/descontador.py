#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

import http.cookies, os

#Comprobar si el cliente nos envia la cookie CONTADOR
#si es true -> incrementamos el valor que trae la cookie CONTADOR
#si es false -> CONTADOR = 1, es la cookie que tengo que devolver

print("Content-type: text/html")
cookie = http.cookies.SimpleCookie()

if os.environ.get("HTTP_COOKIE") == None:
    cookie["CONTADOR"] = 10
    print(cookie)
    print()
else:
    cookie.load(os.environ.get("HTTP_COOKIE"))
    if "CONTADOR" in cookie:
        if int(cookie["CONTADOR"].value) != 0 :
            cookie["CONTADOR"] = int(cookie["CONTADOR"].value) - 1
            print(cookie["CONTADOR"])
            print()
    else:
        cookie["CONTADOR"] = 1
        print(cookie["CONTADOR"])
        print()

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Contador visitas</title>
        </head>
        <body>
           <h1>Cookies</h1>
""")

print("<h3>"+cookie["CONTADOR"].value+"</h3>")

print("""
    </body>
    </html
""")