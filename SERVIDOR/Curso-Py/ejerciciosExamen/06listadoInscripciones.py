#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe

import mysql.connector

#conexion a bbdd
midb = mysql.connector.connect( 
    host = "localhost",
    user = "academia",
    password = "academia",
    database = "academia"
)
#crear un cursor, la consulta ejecutar la consulta y obtener los resultados en una lista de tuplas
miCursor = midb.cursor() #crear cursor
consultaIDestudiante = "SELECT id, nombre FROM estudiantes"
miCursor.execute(consultaIDestudiante) 
miresultado = miCursor.fetchall() 
miCursor.close() 

print("Content-type: text/html\n")
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
for estudiante in miresultado:
    #salida con el nombre del estudiante
    print("<p>"+estudiante[1]+" se ha inscrito en: </p>")

    #sacar de la bbdd los cursos de cada estudiante por id
    miCursor = midb.cursor() #crear cursor

    todosCursosEstudiantes = "SELECT nombre_curso FROM cursos WHERE id_estudiante="+ str(estudiante[0])#estudiante[0]->es el id extraido en la consulta de arriba
    miCursor.execute(todosCursosEstudiantes) 
    resultadoConsultas = miCursor.fetchall() 
    miCursor.close() 

    for consulta in resultadoConsultas:
        print("<p>   "+ consulta[0]+"</p>")