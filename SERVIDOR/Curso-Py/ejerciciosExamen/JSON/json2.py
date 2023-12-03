#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

import json

print("Content-type: text/html\n")

#objeto python
estudiantes = [
    {
        "nombre": "Juan",
        "edad": 20,
        "asignaturas": [
            {"nombre": "Matematicas", "calificacion": 90},
            {"nombre": "Historia", "calificacion": 75},
            {"nombre": "Ingles", "calificacion": 85}
        ]
    },
    {
        "nombre": "Maria",
        "edad": 21,
        "asignaturas": [
            {"nombre": "Matematicas", "calificacion": 78},
            {"nombre": "Historia", "calificacion": 92},
            {"nombre": "Ingles", "calificacion": 88}
        ]
    },
    {
        "nombre": "Carlos",
        "edad": 19,
        "asignaturas": [
            {"nombre": "Matematicas", "calificacion": 85},
            {"nombre": "Historia", "calificacion": 80},
            {"nombre": "Ingles", "calificacion": 95}
        ]
    }
]

#convertir objeto py a JSON
estudiantesJson = json.dumps(estudiantes)
# print("Salida en objeto Python: ")
# print(estudiantes)
# print("<br>")
# print("<br>")
# print("Salida en JSON: ")
# print(estudiantesJson)

#crear fichero json y escribir los datos formato JSON
#crear el fichero y se abre en modo escritura
with open("fichero.json", "w") as fichJson:
    #escribimos los datos e indicamos en el fichero donde queremos que se escriba
    json.dump(estudiantesJson, fichJson)

#abrir el fichero en modo lectura
with open("fichero.json", "r") as fichJson:
    #leemos lo que hay dentro y lo metemos en la variable datos
    datos = json.load(fichJson)
#imprimir datos
print(datos)