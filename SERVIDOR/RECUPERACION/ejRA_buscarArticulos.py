#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

import os, mysql.connector
from urllib.parse import urlparse, parse_qs

#para imprimir html
print("Content-type:text/html\n")

#codigo necesario para recibir los parametros del formulario
ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

#recibir solo la categoria seleccionada
categ = param["categoria"][0]

#conexion a bbdd
midb = mysql.connector.connect( 
    host = "localhost",
    user = "periodico",
    password = "periodico",
    database = "periodico"
)
miCursor = midb.cursor() #crear cursor

#crear consulta para sacar el id de la categoria seleccionada
consultarPorCategoria = "SELECT id FROM categorias WHERE nombre='"+categ+"'" 
#ejecutar consulta
miCursor.execute(consultarPorCategoria) 

miresultado = miCursor.fetchone() #trae una fila
#cerrar cursor
miCursor.close() 
#meter el resultado en una variable id
id = miresultado[0]
miCursor = midb.cursor() #crear cursor

#crear consulta para sacar todos los articulos de la categoria seleccionada
todosArticulos = "SELECT * FROM articulos WHERE id_categoria='"+str(id)+"'"
#ejecutar consulta
miCursor.execute(todosArticulos) 
#meter el resultado en variable
resultadoConsultas = miCursor.fetchall() 
miCursor.close() 
#imprimir cabecera html
print("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Ejercicio 6</title>
        </head>
        <body>
    """)
#imprimir lista con el contenido de la consulta. Recorremos el resultado con un bucle for e imprimimos solo los datos del lugar 1 y 2
print(f"<h1>Mostrando articulos (titulo, contenido) de la categoria con id {id}</h1>")
print("<ul>")
for consulta in resultadoConsultas:
    print("<li>"+str(consulta[1])+", "+str(consulta[2])+"</li>")
print("</ul>")
#fin html
print("""
        </body>
        </html>
    """)
