#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe

import mysql.connector

from urllib.parse import urlparse, parse_qs

print("Content-Type: text/html\n")

midb = mysql.connector.connect( 
    host = "localhost",
    user = "pruebaAjax",
    password = "pruebaAjax",
    database = "pruebaAjax"
)

nombreFich = "fichero.txt"
miCursor = midb.cursor()

#abriendo el fichero como fich
with open(nombreFich) as fich:
    #crear consulta para insertar datos
    insertar = "INSERT INTO datos (producto, cantidad) VALUES (%s, %s)"
    # borrar = "DELETE FROM datos"
    # borrarTabla = "DROP TABLE datos"

    #leer primera linea para omitirla
    primera_linea = fich.readline()
    for line in fich: #recorrer fichero
        elem = line.split(";") #separamos el contenido del fichero por ; y lo guardamos en variable
        print(elem) #imprimir lista para comprobar

        #añadir cada elemento de la lista a la bbdd
        datos_producto_cantidad = (elem[0], elem[1])
        #ejecutar la consulta y los valores de la consulta
        miCursor.execute(insertar, datos_producto_cantidad)
        # miCursor.execute(borrar)

    midb.commit()

# contenido = fich.read()
# print(contenido)

# listaProd = [prod.strip('\n') for prod in fich.readlines()]
# print(listaProd)

# fich.close()


