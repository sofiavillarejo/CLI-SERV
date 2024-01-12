#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

print("Content-Type: text/html\n")

fileitem = form['filename']#nombre de archivo del cliente

def tabla(fn):
            with open(fn, 'r') as fich:
                lineas = fich.readlines()
                tabla = "<table border='1'>"
                header = lineas[0].strip().split(";")  # Divide la primera línea en encabezados por punto y coma
                tabla += "<tr>\n"
                for encabezado in header:
                    tabla += f"<th>{encabezado}</th>"
                tabla += "</tr>\n"
                for linea in lineas[1:]: #empieza el bucle desde la segunda linea del fichero ( la primera son encabezados)
                    datos = linea.strip().split(";")  # Divide cada línea en campos por punto y coma
                    tabla += "<tr>"
                    for campo in datos:
                        tabla += f"<td>{campo}</td>"
                    tabla += "</tr>\n"
                tabla += "</table>"
                return tabla

#comprobar si el nombre del archivo del cliente esta presente 
if fileitem.filename:
    #asignar a una variable y obtenemos el nombre del archivo
    fn = os.path.basename(fileitem.filename)
    #abrir archivo desde la carpeta img, con el nombre recibido en modo escritura binaria porque es una imagen y se escribe el contendio del archivo cargado
    #en el archivo recien creado
    open("img/" + fn, 'wb').write(fileitem.file.read())
    #variable para imprimir la tabla. Llamamos a la funcion tabla y le pasamos la ruta del archivo recien creado
    tablaImprimir = tabla("img/'"+ fn)
    #imprimir todo para que se muestre en forma de tabla
    print(tablaImprimir)
