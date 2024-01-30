#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

import os, mysql.connector
from urllib.parse import urlparse, parse_qs

print("Content-type:text/html\n")

#codigo necesario para recibir los parametros del formulario
ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

#recibir parametros del formulario y guardarlos en variables
tituloArt = param["titulo"][0]
content = param["contenido"][0]
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

#condicion que si la consulta esta vacia, imprime error
if miresultado == None:
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
    print("<p>Error, la categoria no existe</p>")
    print("""
        </body>
        </html>
    """)
else: #si la categoria existe
    id = miresultado[0] #meto en un variable id lo que me trae la consulta en el campo 0, que es el id
    #inserto en la tabla una vez ya tenga el id
    miCursor = midb.cursor()
    #consulta para insertar datos
    insertaArt = "INSERT INTO articulos (titulo, contenido, id_categoria) VALUES (%s, %s, %s)"
    val = (tituloArt, content, id)
    #ejecutar consulta
    miCursor.execute(insertaArt, val)
    #commit necesario para actualziar la tabla de la BBDD
    midb.commit()
    #cerrar cursor
    miCursor.close()
    #imprimir texto de inserción correcta
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
    print("<p>Articulo insertado</p>")
    print("""
        </body>
        </html>
    """)