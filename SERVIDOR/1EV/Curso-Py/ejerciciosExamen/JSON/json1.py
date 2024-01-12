#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe

import json

print("Content-type: text/plain\n")

#CONVERTIR DE JSON A PYTHON -> load/loads
#CONVERTIR DE PYTHON A JSON -> dump/dumps

#variable con texto en formato JSON
fraseJson =  '{ "name":"John", "age":30, "city":"New York"}'

analizarJson = json.loads(fraseJson) #-> Convertir cadena de texto JSON a objeto de Python

#el resultado es un objeto python
print(analizarJson)

#CONVERTIR DE PYTHON A JSON

diccionarioPython = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

#Convertir objeto de Python a cadena de texto JSON
convertirAJson = json.dumps(diccionarioPython)

#el resultado es una cadena de texto de JSON
print(convertirAJson)

#SE PUEDEN CONVERTIR TODOS ESTOS DATOS EN JSON
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#CONVERTIR UN OBJETO DE PYTHON A JSON
miObjeto = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print()
#LECTURA Y ESCRITURA DE ARCHIVOS JSON

#leer datos desde un archivo JSON
with open('datos.json') as fichero:
    datos = json.load(fichero)
print(datos)

#modificar algun dato
datos['persona']['nombre'] = "Sofia"

#escribir los cambios en el fichero
with open('datos.json', 'w') as fichero:
    json.dump(datos, fichero)

print()
print("CADENA JSON CON SANGRIAS Y CLAVES ORDENADAS")
#ARGUMENTOS ADICIONALES CON DUMPS Y LOADS

miObjeto2 = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Buenos Aires"
}

#convertir objeto de python a cadena de texto JSON con sangria y claves ordenadas alfabeticamente
jsonCadenaTexto = json.dumps(miObjeto2, indent=4, sort_keys=True)

#imprimir el resultado
print(jsonCadenaTexto)