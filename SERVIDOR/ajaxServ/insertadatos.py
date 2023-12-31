#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe
import mysql.connector
import sys,json
import os
from urllib.parse import urlparse, parse_qs

sys.stderr.write("Dentro del pedirdatos.py--------\n") #esto escribe en el archivo error.log

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])#siempre 4

#datos que nos envia el cliente en el formulario
t = param["texto"][0]
n = param["numero"][0]

#Crear conexion con la BBDD
#creamos objeto que contiene todos los datos para conectarnos a la BBDD
midb = mysql.connector.connect( 
    host = "localhost",
    user = "pruebajax",
    password = "pruebajax",
    database = "pruebajax"
)

#cursos para hacer peticiones -> objeto que permite hacer consultas a la BBDD
miCursor = midb.cursor()

#crear consulta
insercion = f"INSERT INTO datos (dato1, dato2) VALUES('{t}',{n})" #insertar datos del cliente

#ejecutamos la consulta
miCursor.execute(insercion) 

#crear commit necesario para actualizar la base de datos
midb.commit()

#cerrar cursos y conector
miCursor.close()
midb.close()

#generar salida para el cliente ajax
print("Content-Type: application/json\n") #se va a devolver siempre texto plano, pero lo hemo scambiado a applicaction json para indicar
#que vamos a devolver datos en ese tipo de formato

print(json.dumps("ok"))#imprimir ok convertido a JSON -> esto es el alert(datos) en ajax.js insertaAjax()



