#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe

import http.cookies, os

cookie = http.cookies.SimpleCookie()

print("Content-type:text/html\n")

if os.environ.get("HTTP_COOKIE") != None:
    cookie.load(os.environ.get("HTTP_COOKIE"))
    if "empiezaABC" in cookie:

        print("""<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Mostrar contenido cookie</title>
                </head>
                <body>
            """)

        listaPalabras = cookie["empiezaABC"].value.split(" ") #imprimir el contenido de la cookie
        print("<ol>")
        for item in listaPalabras:
            print(f"<li>{item}</li>")
        print("</ol>")

        print("""
            </body>
            </html>
        """)