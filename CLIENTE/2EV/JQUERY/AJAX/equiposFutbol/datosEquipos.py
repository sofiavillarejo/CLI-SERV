#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe
import cgi
import json


# Obtener los parámetros de la solicitud GET
form = cgi.FieldStorage()
equipo_solicitado = form.getvalue("equipo")

# Datos de todos los equipos
equipos = {
    "Real Madrid": {"fundacion": 1902, "estadio": "Santiago Bernabeu"},
    "FC Barcelona": {"fundacion": 1899, "estadio": "Camp Nou"},
    "Atletico Madrid": {"fundacion": 1903, "estadio": "Wanda Metropolitano"},
    "Valencia CF": {"fundacion": 1919, "estadio": "Mestalla"},
    "Sevilla FC": {"fundacion": 1890, "estadio": "Ramon Sanchez Pizjuan"}
}

# Verificar si el equipo solicitado está en la lista
if equipo_solicitado in equipos:
    datos_equipo = equipos[equipo_solicitado]
    respuesta_json = json.dumps({equipo_solicitado: datos_equipo}, indent=2)
else:
    respuesta_json = json.dumps({"error": "Equipo no encontrado"}, indent=2)

print("Content-type: application/json")
print("")
print(respuesta_json)