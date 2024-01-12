#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe

import os, mysql.connector
from urllib.parse import urlparse, parse_qs

print("Content-type:text/html\n")

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

estud = param["estudiante"][0]
curs = param["curso"][0]
prof = param["profesor"][0]

# print(estud, curs, prof)
#conexion a bbdd
midb = mysql.connector.connect( 
    host = "localhost",
    user = "academia",
    password = "academia",
    database = "academia"
)

miCursor = midb.cursor() #crear cursor

consultaIDestudiante = "SELECT id FROM estudiantes WHERE nombre='"+estud+"'"

miCursor.execute(consultaIDestudiante) 

miresultado = miCursor.fetchone() #trae una fila

# print(miresultado)

miCursor.close()

#si el estudiante no existe:
if miresultado == None:

    print("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Base de datos</title>
        </head>
        <body>
    """)
    print("<p>El estudiante no existe</p>")
    print("""
        </body>
        </html>
    """)

#si el estudiante existe:
else:
    id = miresultado[0] #meto en un variable id lo que me trae la consulta en el campo 0, que es el id
    #inserto en la tabla una vez ya tenga el id
    miCursor = midb.cursor()
    insertaEstudiante = "INSERT INTO cursos (nombre_curso, profesor, id_estudiante) VALUES (%s, %s, %s)"
    val = (curs, prof, id)
    miCursor.execute(insertaEstudiante, val)
    midb.commit()
    miCursor.close()
    print("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Base de datos</title>
        </head>
        <body>
    """)
    print("<h1>ESTUDIANTE INSCRITO</h1>")
    print("""
        </body>
        </html>
    """)
