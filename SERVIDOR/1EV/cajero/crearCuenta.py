#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe
print("Content-Type: text/html\n")

import json, codigoHtml, random
import os
from urllib.parse import urlparse, parse_qs

#para coger los parametros introducidos por el usuario en el formulario
ru= os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

#creamos nuemeros de cuenta de forma aleatoria
nCuentaAleatorio = random.randint(100000, 999999)
# estructura de datos para representar una cuenta con un número de cuenta, un valor numérico asociado y una lista vacía para almacenar información adicional.
cuenta = [nCuentaAleatorio, 0, []]

#si el tamaño del archivo es = 0, añadimos a listaCuentas nuestra lista creada cuenta con los numeros de cuenta aleatorios
if os.path.getsize("datos/listaCuentas.dat") == 0: 
    listaCuentas = [cuenta] #lista que contiene las cuentas
    listaJson = json.dumps(listaCuentas) #convierte algo en formato json

else:
    fich = open("datos/listaCuentas.dat")
    listaCuentas = json.load(fich) # lee el contenido del fichero y lo convierte en una lista de productos
    fich.close()
    listaCuentas.append(cuenta)#añado la cuenta a la lista
    listaJson = json.dumps(listaCuentas) #convierte los objetos de python en cadenas JSON

fich = open("datos/listaCuentas.dat", "wt")#si existe el fichero, me cargo lo que tiene dentro y escribo
fich.write(listaJson)#escribo en el fichero nuestra variable listaJson que contiene la lista de cuentas
fich.close()#cierro el fichero

#crear la salida HTML
codigoHtml.htmlRecarga()