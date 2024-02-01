#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

import http.cookies


cookie = http.cookies.SimpleCookie()
cookie["ID1"] = 1
cookie["ID1"]["expires"] = "Wed, 11 Oct 2022 07:28:00 GMT"
print("Content-type: text/html")
print(cookie["ID1"])
print()

print('''   
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="refresh" content="3; index.html">
            <title>Login con registro en fichero</title>
        </head>
        <body>
          <h1>Saliendo de la aplicacion</h1>
    ''')