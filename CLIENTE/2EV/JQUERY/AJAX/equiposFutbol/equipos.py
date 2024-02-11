#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe
import json

equipos = ["Real Madrid", "FC Barcelona", "Atletico Madrid", "Valencia CF", "Sevilla FC"]

# Crear un diccionario con los nombres de los equipos
equipos_dict = {"equipos": equipos}

# Convertir el diccionario a formato JSON
json_equipos = json.dumps(equipos_dict, indent=2)

print("Content-type: application/json")
print("")
# Imprimir el JSON
print(json_equipos)
