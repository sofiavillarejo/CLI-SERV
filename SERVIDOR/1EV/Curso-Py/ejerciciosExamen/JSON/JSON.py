#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

import json, os

print("Content-Type: text/plain\n")

#CONVERTIR DE JSON A PYTHON -> load/loads
#CONVERTIR DE PYTHON A JSON -> dump/dumps

#PASAR DE PYTHON A JSON
colores = ["rojo", "verde", "azul", "amarillo"]

coloresJSON = json.dumps(colores)

#COMPROBAR SI TIENE CONTENIDO -> EL RESULTADO ES QUE ESTA VACIO
if os.path.getsize("colores.json") == 0:
        print("El fichero esta vacio")
else:
        print("El fichero tiene contenido")

#AÑADIMOS DATOS AL FICHERO
with open("colores.json", "w") as fichColores:
    json.dump(coloresJSON, fichColores)
    print("Datos added al fichero")

#VOLVEMOS A COMPROBAR SI EL FICHERO TIENE ALGO Y AQUI DA QUE SI
if os.path.getsize("colores.json") == 0:
        print("El fichero esta vacio")
else:
        print("El fichero tiene contenido")

###########################
#PASAR DE JSON A PYTHON
datoJson =  '{ "name":"John", "age":30, "city":"New York"}'

#tranformar de json a python y guardarlo en una variable
datosPython = json.loads(datoJson)

print(datosPython)

with open("fich.txt", "w") as fichero:
    json.dump(datosPython, fichero)#escribir en el fichero
    print(type(datosPython))
    print(type(datoJson))
