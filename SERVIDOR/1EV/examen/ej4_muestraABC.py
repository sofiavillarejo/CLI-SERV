#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

#.py que muestra el contendio de la cookie metiendolo en una lista ordenada
import http.cookies, os

print("Content-type: text/html\n")

cookie = http.cookies.SimpleCookie()
cookie["empiezaABC"] = "hola"

print('''
      <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Separador de palabras</title>
        </head>
        <body>        
          <h1>Muestra ABC</h1>
''')

for datos in cookie:
    print("<ol>")
    print(f"<li>{datos}</li>")
    print("</ol>")

print('''
    </body>
    </html>
''')