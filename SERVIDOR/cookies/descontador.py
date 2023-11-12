#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

import http.cookies, os

#Comprobar si el cliente nos envia la cookie CONTADOR
#si es true -> incrementamos el valor que trae la cookie CONTADOR
#si es false -> CONTADOR = 1, es la cookie que tengo que devolver

print("Content-type: text/html")
cookie = http.cookies.SimpleCookie()

#verificar si la variable de entorno HTTP_COOKIE está presente. 
# Si no está presente, se asume que es la primera visita y se establece la cookie "CONTADOR" en 10.
if os.environ.get("HTTP_COOKIE") == None:
    cookie["CONTADOR"] = 10
    print(cookie)
    print()
else:
    #Si la cookie "CONTADOR" ya existe en la solicitud del cliente, cargas su valor actual.
    cookie.load(os.environ.get("HTTP_COOKIE"))
    if "CONTADOR" in cookie:
        #Si el valor no es cero, decrementas el valor de la cookie en 1.
        if int(cookie["CONTADOR"].value) != 0 :
            cookie["CONTADOR"] = int(cookie["CONTADOR"].value) - 1
            print(cookie["CONTADOR"])
            print()

    #Si la cookie "CONTADOR" no existe, la estableces en 1.
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
#imprimir valor actual de nuestra cookie
print("<h3>"+cookie["CONTADOR"].value+"</h3>")

print("""
    </body>
    </html>
""")