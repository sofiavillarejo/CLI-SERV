#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe

import os, mysql.connector, json
from urllib.parse import urlparse, parse_qs

print("Content-type:text/html\n")

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

name = param["nombre"][0]
age = int(param["edad"][0])
peso_trabajador = float(param["peso"][0])

# print(estud, curs, prof)
#conexion a bbdd
midb = mysql.connector.connect( 
    host = "localhost",
    user = "trabajo",
    password = "trabajo",
    database = "trabajo"
)
#crear cursor
miCursor = midb.cursor()

# INSERTAR DATOS EN LA BBDD

insertaDatos = "INSERT INTO personas (nombre, edad, peso) VALUES (%s, %s, %s)"
val = (name, age, peso_trabajador)
miCursor.execute(insertaDatos, val)

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
print("<p>Trabajador insertado correctamente</p>")
print("<hr>")


#MOSTRAR DATOS DE LA BBDD QUE SE HAN IDO INSERTANDO
midb = mysql.connector.connect( 
    host = "localhost",
    user = "sofia",
    password = "sofia",
    database = "trabajo"
)
miCursor2 = midb.cursor()
mostrarDatos = "SELECT * FROM personas"
miCursor2.execute(mostrarDatos)
miresultado = miCursor2.fetchall()
print(miresultado)
miCursor.close()

for persona in miresultado:
    print("<p>"+str(persona)+"</p>")
    #METER DATOS A FICHERO JSON 
    with open("ficheroPersonasBBDD.json", "w") as fichJson:
        json.dump(persona, fichJson)
    fichJson.close()
print("<hr/>")


#MODIFICAR UN REGISTRO DE LA TABLA
midb = mysql.connector.connect( 
    host = "localhost",
    user = "trabajo",
    password = "trabajo",
    database = "trabajo"
)
miCursor2 = midb.cursor()
print('''
    </body>
    </html>
''')
