#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

import http.cookies, os
import codHtml

cookie = http.cookies.SimpleCookie()

print("Content-type:text/html\n")

if os.environ.get("HTTP_COOKIE") != None:
    cookie.load(os.environ.get("HTTP_COOKIE"))
    if "empiezaABC" in cookie:

        codHtml.cabHTMLGen()

        listaPalabras = cookie["empiezaABC"].value.split(" ") #imprimir el contenido de la cookie
        print("<ol>")
        for item in listaPalabras:
            print(f"<li>{item}</li>")
        print("</ol>")

        codHtml.finHTMLGen()

