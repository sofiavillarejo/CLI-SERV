#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

#para poder leer los aprametros que se introducen en el servidor
import os
from urllib.parse import urlparse, unquote, parse_qs

#import para que reconozca la raiz cuadrada
import math

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])#siempre 4

#cateto 1 y cateto2
c1 = float(param["cat1"][0])
c2 = float(param["cat2"][0])

#calculo con ambos catetos
hipotenusa = math.sqrt(c1*c1+c2*c2)
#imprimir en pantalla redondeando a dos decimales el resultado
print(round(hipotenusa,2))