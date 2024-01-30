#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\n")

import os, codigoHtml
try:
    #abrir el fichero en modo lectura
    fich = open("datos/listaCompra.dat") 
except: 
    #se crea el fichero en datos si da error al abrir
    print("se crea el fichero en datos")
    fich = open("datos/listaCompra.dat", "x")

#leemos el contenido del fichero en una lsta de productos si no está vacío
if os.path.getsize("datos/listaCompra.dat") != 0: 
    productos = fich.readlines()
else:
    productos = []
#cerrar fichero
fich.close()

def listaDeProductos():
    if len(productos) != 0:#si hay productos, se crea la lista
        print("<ol>")
        prod = [p.strip('\n') for p in productos] #quitar saltos de linea de la lista
        for p in prod:
            #separamos el producto de la caantidad por ;
            elem = p.split(";")
            print(f"<li>{elem[1]}  de  {elem[0]} </li>")
        print("</ol>")
    else:
        print("<h3>Lista de la compra vacía</h3>")
    print("<hr/>")

#importamos html del otro archivo (crear cabecera)
codigoHtml.cabeceraHtml()

#metodo que imprime la lista de la compra
listaDeProductos()

#crear formulario
codigoHtml.formulario()

#crear fin del html
codigoHtml.finHtml()



