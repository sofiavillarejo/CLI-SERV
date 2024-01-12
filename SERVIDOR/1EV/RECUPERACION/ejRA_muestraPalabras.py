#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

import http.cookies, os

cookie = http.cookies.SimpleCookie()

print("Content-type:text/html\n")

if os.environ.get("HTTP_COOKIE") != None:
    cookie.load(os.environ.get("HTTP_COOKIE"))
    if "palabrasVocales" in cookie:

        print("""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Ejercicio 4</title>
            </head>
            <body>
                <h1>Palabras que empiezan con vocal en cookie</h1>

        """)

        listaPalabras = cookie["palabrasVocales"].value.split(" ") #imprimir el contenido de la cookie
        print("<ol>")
        for item in listaPalabras:
            print(f"<li>{item}</li>")
        print("</ol>")

        print("""
            </body>
            </html>
        """)

if os.environ.get("HTTP_COOKIE") != None:
    cookie.load(os.environ.get("HTTP_COOKIE"))
    if "palabrasConsonantes" in cookie:

        print("""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Ejercicio 4</title>
            </head>
            <body>
              <h1>Palabras que empiezan con consonante en cookie</h1>
        """)
        listaPalabras = cookie["palabrasConsonantes"].value.split(" ") #imprimir el contenido de la cookie
        print("<ol>")
        for item in listaPalabras:
            print(f"<li>{item}</li>")
        print("</ol>")

        print("""
            </body>
            </html>
        """)