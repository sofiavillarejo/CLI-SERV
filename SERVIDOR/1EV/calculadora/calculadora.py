#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import os
from urllib.parse import urlparse, unquote, parse_qs

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])


#n1 = param["num1"][0]
#n2 = param["num2"][0]
#oper = param["operacion"][0]

#esto se ve en la consola del navegador y nos dice que son strings
#print(type(n1))
#print(type(n2))
#para pasarlo directamente a int se podría hacer así:

n1 = int(param["num1"][0])         
n2 = int(param["num2"][0])        #ASÍ YA SON INTEGER
oper = param["operacion"][0]

#lo pasamos a int porque el formato que hay puesto es texto, entonces no nos suma el resultado sino que
#nos imprime un numero al lado del otro

#IMPORTANTE --> APRENDERSE ESTA LÍNEA PARA USARLA
salida = "El resultado de la {} de {} {} {} es {}" #esta línea es para la division, para rellenar los huecos

if oper == "s":
    #print(int(n1) + int(n2))
    print("El resultado de la suma de " + str(n1) + " más " + str(n2) + " es " + str(n1 + n2)+"<br>")
    print(salida.format("suma", n1, "más", n2, n1+n2))

if oper == "r":
    #print(int(n1) - int(n2))
    print("El resultado de la resta de " + str(n1) + " menos " + str(n2) + " es " + str(n1 - n2))

if oper == "multiplicacion":
    #print(int(n1) * int(n2))
    print("El resultado de la multiplicación de " + str(n1) + " por " + str(n2) + " es " + str(n1 * n2)+ "<br>")
    print(f"El resultado de la {oper} de {n1} por {n2} es {n1+n2}")
if oper == "d":
    #print(int(n1) / int(n2))    
    #print("El resultado de la división de " + str(n1) + " entre " + str(n2) + " es " + str(n1 / n2))
    print(salida.format("división", n1, "por", n2, n1/n2))

