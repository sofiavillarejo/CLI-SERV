#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe

print("Content-type:text/plain\n")

import os, codHtml
from urllib.parse import urlparse, parse_qs

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

precioCorte = float(param["precio_corte"][0])

fich = open("productos.txt") #abrimos el fichero de productos
productos = fich.readline() #leemos la linea ya  que solo tiene una
fich.close() #cerrar fichero

fich = open("precios.txt")
precios = fich.readline()
fich.close()

#listas que contiene cada precio y producto
#ambas son cadenas de caracteres, por eso luego hay que convertirlo a float para que lo saque
listaProductos= productos.split(" ") 
listaPrecios= precios.split(" ")

#crear fichero nuevo para escribir los productos filtrados
f = open("prod_filtrados.txt", "wt")


#recorrer los datos de ambos ficheros y sacar el precio de corte
for cont in range(len(listaProductos)): #en este caso va de 0 a 3 porque hay 4 productos en el fichero
    print(cont)#si no me fio de lo que estoy haciendo
    if float(listaPrecios[cont]) >= precioCorte:
        #print(listaProductos[cont], listaPrecios[cont])
        f.write(listaProductos[cont]+ "\n")
f.close()

codHtml.cabHTMLGen()
print("<p>Filtro realizado</p>")
codHtml.finHTMLGen()

####HACER EJERCICIOS DE FICHEROS EN VARIAS LIENA,S EN UNA LINEA, CON DISTINTITOS TIPOS DE DATOS...