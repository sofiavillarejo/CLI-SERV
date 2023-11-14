#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

#.py que genera las distintas consultas a la base de datos creada en mysql 
#ademas, comprobamos los valores recibimos del formulario
import mysql.connector
import os
from urllib.parse import urlparse, parse_qs

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

#cogemos los oparametros que ha introducido el usuario
estud = param["estudiante"][0]
curso = param["curso"][0]
profesor = param["profesor"][0]

print("Content-Type: text/html\n")

#conexion a bbdd
midb = mysql.connector.connect( 
    host = "localhost",
    user = "academia",
    password = "academia",
    database = "academia"
)
#realziar consulta
miCursor = midb.cursor()
estudiante = "SELECT * FROM  estudiantes"
miCursor.execute(estudiante) 
miresultado = miCursor.fetchall() #trae una fila
print(miresultado)
miCursor.close()

miCursor = midb.cursor()
curso = "INSERT INTO cursos VALUES (%s, %s, %s)"
miCursor.execute(estudiante) 
miresultado = miCursor.fetchall() #trae una fila
miCursor.close()
