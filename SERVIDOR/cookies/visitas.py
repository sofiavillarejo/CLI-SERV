#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe
import http.cookies, os

contador = 0

contador = contador + 1
#comprobar si el cliente nos envia la cookie CONTADOR
#si es true -> incrementamos el valor que trae la cookie CONTADOR
#si es false -> CONTADOR = 1, es la cookie que tengo que devolver

print("Content-type: text/html")
#con esto se envia una cookie al cliente
cookie = http.cookies.SimpleCookie()
cookie["cuqui"] = "lkjh"
#si no existe la cookie, la creo y se la mando

if os.environ.get("HTTP_COOKIE") == None:
    cookie["CONTADOR"] = 1
    cookie["CONTADOR"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT"
    print(cookie)
    print()
else:
    cookie.load(os.environ.get("HTTP_COOKIE"))
    if "CONTADOR" in cookie:
        cookie["CONTADOR"] = int(cookie["CONTADOR"].value) +1
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
        <title>Contador de visitas</title>
    </head>
    <body>
        <h1>Cookies</h1>
    """)
print("<h3>" + cookie["CONTADOR"].value + "</h3>")
print('<a href="resetContador.py">Resetear contador</a>')
print('<a href="borrarCookie.py">Borrar Cookie</a>')


print("""
    </body>
    </html>
""")