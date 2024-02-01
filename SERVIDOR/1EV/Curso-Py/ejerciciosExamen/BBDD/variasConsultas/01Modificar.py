#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe

import os, mysql.connector
from urllib.parse import urlparse, parse_qs

print("Content-type:text/html\n")

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

id = int(param["id"][0])
name = param["nombre"][0]
age = int(param["edad"][0])
peso_trabajador = float(param["peso"][0])

#conexion a bbdd
midb = mysql.connector.connect( 
    host = "localhost",
    user = "trabajo",
    password = "trabajo",
    database = "trabajo"
)
#crear cursor
miCursor = midb.cursor()

modificarDatos = "UPDATE personas SET nombre=%s,edad=%s,peso=%s WHERE id=%s" 
val = (name, age, peso_trabajador, id)
miCursor.execute(modificarDatos, val)

#NECESARIO PARA HACER CUALQUIER TIPO DE CAMBIO A LA TABLA -> DELETE, UPDATE O INSERT
midb.commit()

miCursor.close()
print('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ejercicio BBDD</title>
    </head>
    <body>
''')
print("<p>Trabajador modificado correctamente</p>")

print('''
    </body>
    </html>
''')