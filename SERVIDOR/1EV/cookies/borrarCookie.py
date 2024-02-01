#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

import http.cookies

print("Content-type: text/html")
cookie = http.cookies.SimpleCookie()
cookie["CONTADOR"] = 1
cookie["CONTADOR"]["expires"] = "Wed, 11 Oct 2022 07:28:00 GMT" #cambiamos fecha de expiracion a una antigua que ya ha apsado para que se borre
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

print("<h3>Cookie borrada</h3>")
print('<a href="visitas.py">Visitas</a>')

print("""
    </body>
    </html>
""")