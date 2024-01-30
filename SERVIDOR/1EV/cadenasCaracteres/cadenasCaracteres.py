#!C:\Users\zx20student109\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import os
from urllib.parse import urlparse, parse_qs

ru= os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

texto = param["texto"][0]
palabra = param["palabra"][0]
letra = param["letra"][0]

#la variable texto contiene el texto introducido
#por el usuario en el formulario

#funciones de apoyo
def inicioHtml(): #Devuelve al cliente el inicio del HTML
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

def finHtml(): #Devuelve al cliente el final del HTML
    print("""
                </h6>
            </div>

            <div class="col"></div>

        </div>      
    </body>
    </html
""")

def separaLetrasLineas(t):
    for l in t:
        print(l+"<br/>")

def contarLetras(t):
    contador = 0
    for l in t:
        if (l >= "A" and l <= "Z") or (l >= "a" and l <= "z"):
            contador += 1
        if l == "ñ" or l == "á" or l == "Á" or l == "ü": 
            contador += 1
    print(contador)
        
def reverseTexto(t):
    #range() devuleve una secuencia de numeros que empieza por 0 de forma predeterminda y aumenta en 1 de forma predeterminada tambien y termina antes de un numero en especifico
    #range(start, stop, step)
    # x = range(3,6)
    # for n in x:    ESTO CREA UNA SECUENCIA DE NUMEROS DEL 3 AL 5
    #     print(n)

    tam = len(t) #calculo del tamaño de t
    salida = "" #variable con el texto revertido
    for pos in range(tam): #bucle con range -> de la secuencia 0,1..,13
        salida += t[tam-pos-1] # se recorre la palabra en la secuencia 13,12..1,0 y se añade a la salida
    print(salida) # se imprime la salida
    
    salida2 = ""
    for l in t:
        salida2 = l + salida2
    print(salida2)

    print(t[::-1])

def encontrarPalabra(t, p):
    #find() encuentra la primera aparicion del valor especificado 
    # t.find(value, start, end)
    encontrada = False
    if t.find(p) != -1: 
        encontrada = True
    return encontrada

def contarLetra(t, l): #devuelve el numero de veces que aparece letra l en texto t, si hay un error devueve -1
    contador = 0
    if len(l) == 1:
        for letra in t:
            if (l == letra):
                contador = contador + 1
            else:
                contador = -1
    return contador

def contarVocales(t):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for l in t:
        #if l == "A":
        #    a = a + 1
        #elif l == "E":
        #    e = e + 1
        #elif l == "I":
        #    i = i + 1
        #elif l == "O":
        #    o = o + 1
        #elif l == "U":
        #    u = u + 1
        match l.lower():
            case "a":
                a = a +1
            case "e":
                e = e +1
            case "i":
                i = i +1
            case "o":
                o = o +1
            case "u":
                u = u +1

    print(f"Hay {a} as, hay {e} es, hay {i} is, hay {o} os, hay {u} us")

def dividirPalabras(t):
    return t.split(" ")


#
# la salida que se envia al cliente
#
inicioHtml()
separaLetrasLineas(texto)
print("<hr/>")
contarLetras(texto)
print("<hr/>") #imprime una linea negra de separacion
reverseTexto(texto)
print("<hr/>")
if encontrarPalabra(texto, palabra):
    print("Palabra encontrada")
else: 
    print("palabra no encontrada")
print("<hr/>")
print(contarLetra(texto, letra))
print("<hr/>")
contarVocales(texto)
print("<hr/>")
print(dividirPalabras(texto))
finHtml()