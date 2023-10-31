#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

import cgi, os, csv
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
                for linea in lineas[1:]:
                    datos = linea.strip().split(";")  # Divide cada línea en campos por punto y coma
                    tabla += "<tr>"
                    for campo in datos:
                        tabla += f"<td>{campo}</td>"
                    tabla += "</tr>\n"
                tabla += "</table>"
                return tabla
            
if fileitem.filename:
    fn = os.path.basename(fileitem.filename)
    open("ficheros/" + fn, 'wb').write(fileitem.file.read())
    tablaImprimir = tabla("ficheros/'"+ fn)
    print(tablaImprimir)
