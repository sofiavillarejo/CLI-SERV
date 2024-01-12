#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exeprint

("Context-Type: text/html\n")

import os,json
from urllib.parse import urlparse, unquote, parse_qs
import codigoHtml

#para coger los parametros introducidos por el usuario en el formulario
ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

#selecciono del formulario el numero de cuenta, cantridad y la operacion a realizar
numCuenta = int(param["numC"][0]) -1
cant = int(param["c"][0])
oper = param["operacion"][0]

#abrimos el fichero listaCuentas.dat que esta en la carpeta datos y lo guardamos en una variable fich
fich = open("datos/listaCuentas.dat")
listaCuentas = json.load(fich) #guardamos nuestro fichero e una variable y a la vez, lo convertimos a json
fich.close() #cerramos el fichero

# "Si la operación es 'Ingresar', entonces aumenta el valor en la posición 1 de la lista ubicada en listaCuentas en la posición numCuenta por la cantidad cant
if oper == "Ingresar":
    listaCuentas[numCuenta][1] += cant
    listaCuentas[numCuenta][2].append(cant) # agrega la cantidad cant a la lista en la posición 2 de la misma cuenta
    fich = open("datos/listaCuentas.dat","wt") #abre el archivo 'datos/listaCuentas.dat' en modo de escritura de texto
    fich.write(json.dumps(listaCuentas)) # escribe el contenido de listaCuentas convertido a formato JSON en el archivo,
    fich.close() #cierra el archivo
    codigoHtml.ingRet() #codigo que contiene la pagina de recarga de que la operacion se esta realizando
else:
    if listaCuentas[numCuenta][1] >= cant: # Si el saldo en la cuenta es mayor o igual a la cantidad a retirar
        listaCuentas[numCuenta][1] -= cant # Resta la cantidad al saldo de la cuenta
        listaCuentas[numCuenta][2].append(-cant) #añado a la lista de cuentas en la tercera posición el valor de la cantidad que ingreso o retiro
        fich = open("datos/listaCuentas.dat","wt") #abrimos el fichero en modo escritura
        fich.write(json.dumps(listaCuentas)) # Escribe el contenido de listaCuentas en formato JSON en el archivo
        fich.close() #cerramos el fichero
        codigoHtml.ingRet() #codigo que contiene la pagina de recarga de que la operacion se esta realizando
    else:
        codigoHtml.error() #si ha habido un error, muestro el codigo de la pagina de error



