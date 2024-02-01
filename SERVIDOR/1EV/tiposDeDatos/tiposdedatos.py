#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\n")

#importa libreria y funciones 
import os 
from urllib.parse import urlparse, unquote, parse_qs 

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

dato = param["dato"][0]

equiposFutbolBuenos = "Sporting Madrid Barsa Atlético Betis Sevilla"

#si dato no esta en equiposFutbolBuenos, imprime...
if dato not in equiposFutbolBuenos:
    #print("El equipo " + dato + " no es bueno")#no usado
    #print("El equipo {} no es bueno".format(dato))#se usa a veces
    print(f"El equipo {dato} no es bueno")#muy usado --USAR ESTA FORMA LA F INDICA QUE SE VANA  METER DATOS ENTRE LOS CORCHETES

#si no, imprime..
else:
    print(f"El equipo {dato} es bueno <br>")

# print(equiposFutbolBuenos[10:15] + "<br/>")#saca el texto que haya desde la posicion 11 hasta la 15
# print(equiposFutbolBuenos[:15] + "<br/>")#desde el principio hasta el 15
# print(equiposFutbolBuenos[10:] + "<br/>")#desde el 10 hasta el final
# print(equiposFutbolBuenos[-5:] + "<br/>")
# print(equiposFutbolBuenos[-5:-3] + "<br/>")#cuenta desde atrás
# print(equiposFutbolBuenos[10] + "<br/>")#caracter 10 
# print(equiposFutbolBuenos[-10] + "<br/>")

# print(equiposFutbolBuenos.upper() + "<br/>")#poner todo en mayúsculas
# print(equiposFutbolBuenos.lower() + "<br/>")#poner todo en minúsculas

# print(equiposFutbolBuenos.replace("a","1") + "<br/>")#cambia las a por 1
# print(equiposFutbolBuenos.replace("ti","00") + "<br/>")#cambia las ti por ceros
# print(equiposFutbolBuenos.split(" ")[3])#me devuelve un array con los datos separados por comas pero, en este caso, le pedimos el que está en la cuarta posición

# listaEquipos = equiposFutbolBuenos.split(" ")
# print(listaEquipos[1] + "<br/>")

# print(dato.isdecimal())#devuelve vd o falso segun si todo los caracteres sean numeros o no
# print(dato.isdigit())

# print(dato + "aa" + "<br/>")#concatena variables pero depende de que contengan funciona o no

# x = 2
# print(dato, str(x))

# print("En un lugar de \"La\" Mancha")#para que se impriman las comillas
# print("\x12")#pone un cuadrado

# print(type(10>9))#imprime en consola que es un tipo de dato booleano

