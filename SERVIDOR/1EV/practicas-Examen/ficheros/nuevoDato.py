#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe
("Context-Type: text/html\n")

import os
from urllib.parse import urlparse, parse_qs
import codigo

#para coger los parametros introducidos por el usuario en el formulario
ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

#selecciono del formulario el salario y los gastos
sal = param["salario"][0]
gas = param["gastos"][0]

fich = open("listaSalarios.dat", "at")

if os.path.getsize("listaSalarios.dat") != 0: 
    fich.write("\n")

fich.write(sal + " ; " + gas)#escribimos el producto y la cantidad

fich.close()

codigo.htmlRecarga()
