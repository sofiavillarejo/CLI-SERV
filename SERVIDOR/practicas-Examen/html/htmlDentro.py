#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe

print("Content-type: text/html\n")

import os
from urllib.parse import urlparse, parse_qs

ru= os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

texto = param["texto"][0]
palabra = param["palabra"][0]
letra = param["letra"][0]


#tambien contiene funciones
def cabeceraHTML():
    print("""
    <!DOCTYPE html>
    <html>  
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Calculadora</title>

        <!-- Latest compiled and minified CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet">
        <!-- Latest compiled JavaScript -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js"></script>
    </head>
    <body>
        <div class="row mt-3">

            <div class="col"></div>

            <div class="col bg-secondary text-light text-center">      
                <h1 class="display-1">Resultado</h1>
                <h6 class="display-6">
    """)

def finHtml():
#Devuelve al cliente el final del HTML
    print("""
                </h6>
            </div>

            <div class="col"></div>

        </div>      
    </body>
    </html
""")
    
def separarLetras(t):
    for l in t:
        print(l + "<br/>")


cabeceraHTML()
separarLetras(texto)
finHtml()