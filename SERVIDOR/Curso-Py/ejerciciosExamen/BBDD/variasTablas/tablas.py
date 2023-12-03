#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe

# CREATE TABLE pedidos(
#     id INT AUTO_INCREMENT NOT NULL,
#     cliente VARCHAR(50) NOT NULL UNIQUE,
#     CONSTRAINT pk_cliente PRIMARY KEY(id));

# CREATE TABLE detalles_ped(
#     id INT AUTO_INCREMENT NOT NULL,
#     marca VARCHAR(50) NOT NULL,
#     id_pedido INT(6) NOT NULL,
#     CONSTRAINT pk_detalle_ped PRIMARY KEY(id),
#     CONSTRAINT fk_detalle_ped FOREIGN KEY (id_pedido) REFERENCES pedidos(id));


import os, mysql.connector
from urllib.parse import urlparse, parse_qs

print("Content-type:text/html\n")

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

name = param["nombre"][0]
brand = param["marca"][0]

#conexion a bbdd
midb = mysql.connector.connect( 
    host = "localhost",
    user = "fabrica",
    password = "fabrica",
    database = "fabrica"
)
#crear cursor
miCursor = midb.cursor()

# INSERTAR DATOS EN LA BBDD
traerId = "SELECT id FROM pedidos WHERE cliente='"+name+"'"
miCursor.execute(traerId)
miresultado = miCursor.fetchone() #trae una fila

miCursor.close() 

if miresultado == None:
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
    print("<p>Error, el cliente no existe</p>")
    print('''
        </body>
        </html>
    ''')
else: #si el paciente existe
    id = miresultado[0] #meto en un variable id lo que me trae la consulta en el campo 0, que es el id
    #inserto en la tabla una vez ya tenga el id
    miCursor = midb.cursor()
    insertaMarca = "INSERT INTO detalles_ped (marca, id_pedido) VALUES (%s, %s)"
    val = (brand, id)
    miCursor.execute(insertaMarca, val)
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
    print("<p>Marca insertada</p>")
    print('''
        </body>
        </html>
    ''')
    