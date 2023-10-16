#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/plain\n")#en vez de html se pone plain--> texto plano para guardar en ficheros

import os
from urllib.parse import urlparse, unquote, parse_qs

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

fig= int(param["figura"][0])
nFil = int(param["nFilas"][0])

# funcion dibuja un cuadrado de astericos de n filas y n columnas
def cuadrado(n): #n es el numero de filas a representar

    #variable global a toda la función
    linea = ""#variable que contiene una fila

    print(f"dibujar un cuadrado de {n} filas y {n} columnas")
    #i --> n de filas
    #c --> columnas
    #bucle para crear filas
    for i in range(n): #devuelve un n entre 0 y el n de filas que hayan puesto, e decir si n es 5--> 0 1 2 3 4 5 
        #bucle para crear las columnas
        for c in range(n):
            linea += "*" #acumulando los asteriscos para formar una línea
        print(linea) #imprimir linea
        linea="" #vaciar linea para que no la vuelva a imprimir, hay que hacerlo si o si porque sino imprime como una escalera

#funcion dubijar triangulo de astericos de nfilas
def triangulo(n):
    print(f"Dibujar un triángulo de {n} filas")
    linea = ""

    #start, stop, step
    #(num1, num2, num3)
    for f in range(n): #si n es 5 --> 0 1 2 3 4 
        for c in range (f+1): #si f es 0 -->0; si f es 1 -> 0 1; si f es 2 --> 0 1 2 ...
            linea +="*"
        print(linea)
        linea=""
#fin de la funcion triangulo

#funcion dibujar triangulo invertido
def trianguloVuelta(n):
    print(f"Dibujar un triángulo dado la vuelta de {n} filas")
    linea=""

    for f in range(n): # con n es 5 --> 0 1 2 3 4 
        for c in range(n-f):#con n-f siendo n=5 y f=0 --> 0 1 2 3 4, con 5-1 --> 0 1 2 3 
            linea+="*"
        print(linea)
        linea=""

def trianguloReves(n):
    print(f"Dibujar un triángulo al revés de {n} filas")
    linea=""
    for f in range(n):
        for e in range(n-f-1):
            linea+=" "
        for c in range(f+1):
            linea+="*"
        print(linea)
        linea=""
        
def trianguloRevesInvertido(n):
    print(f"Dibujar un triángulo al revés invertido de {n} filas")
    linea=""
    for f in range(n,0,-1):
        for e in range(n-f):
            linea+=" "
        for c in range(f):
            linea+="*"
        print(linea)
        linea=""

def cuadradoMultiStr(n):
    print(f"Dibujar un cuadrado de {n} filas y {n} columnas")
    linea=""

    for f in range(n):
        linea+="*" *n #coger un string y multiplicarlo
        print(linea)
        linea=""
def trianguloMultiStr(n):
    linea=""
    for f in range(n):
        linea = "+"+(f+1)
        print(linea)
        linea=""
    
match fig:
    case 1:
        cuadrado(nFil)
    case 2:
        triangulo(nFil)
    case 3: 
        trianguloVuelta(nFil)
    case 4:
        trianguloReves(nFil)
    case 5:
        trianguloRevesInvertido(nFil)
    case 6: 
        cuadradoMultiStr(nFil) #cuadrado multiplicado por string
    case 7:
        trianguloMultiStr(nFil)
    case _:
        print("opción no contemplada")
