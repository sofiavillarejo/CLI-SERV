#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exeprint("Context-Type: text/html\n")

import os,json, codigoHtml
from urllib.parse import urlparse, parse_qs

#para coger los parametros introducidos por el usuario en el formulario
ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

#seleccionamos el parametro numero de cuenta
numCuenta = param["numC"][0]

#abrimos el fichero listaCuentas.dat que esta en la carpeta datos y lo guardamos en una variable fich
fich = open("datos/listaCuentas.dat")
listaCuentas = json.load(fich) #guardamos nuestro fichero e una variable y a la vez, lo convertimos a json
fich.close() #cerramos el fichero
historial = "" #creamos la variable historial vacía

#recorremos el fichero
for x in listaCuentas:
    #si en la posicion 1 del fichero hay un numero de cuenta
    if x[0] == int(numCuenta):
        #si hay una coincidencia, se asigna el tercer valor del ítem a la variable transacciones y salimos del bucle.
        transacciones = x[2]
        break

#recorremos las transacciones
for operacion in transacciones:
    if operacion > 0:
        #añadimos al historial en forma de lista la operacion qu ese haya realizado de ingreso
        historial = historial + "<li style='color: green;'>Ingreso: "+ str(operacion) + "</li>"
    else:
        #sino, es un gasto y lo añadimos
        historial = historial + "<li style='color: red;'> Gasto: "+ str(operacion) + "</li>"

#importamos del codigoHtml, la parte de consultar cuenta y le pasamos los valores que hemos utilizado (numCuenta e historial)
codigoHtml.consultarCuenta(numCuenta, historial)
