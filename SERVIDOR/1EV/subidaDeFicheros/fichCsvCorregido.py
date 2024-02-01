#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

def crearTabla(nomFich):
    print("Content-Type: text/html\n")
    print("<table border='1px solid'>")
    #abrir fichero
    with open(nomFich) as fichero:
        #tratar la primera linea para crear la cabecera
        cabecera = fichero.readline().split(";")#dividir cada linea por puntos y comas
        cabecera = [ele.strip() for ele in cabecera] #quitar el espacio en blanco de cada elemento en cabecera

        print("<tr>")
        for dato in cabecera:
            print(f"<th> {dato}</th>")
        print("</tr>")

        for linea in fichero:
            print("<tr>")
            for dato in linea.strip().split(";"):
                print(f"<td> {dato}</td>")
            print("</tr>")
    print("</table>")

fileitem = form['filename']#nombre de archivo del cliente

#comprobar si el nombre del archivo del cliente esta presente 
if fileitem.filename:
    #asignar a una variable y obtenemos el nombre del archivo
    fn = os.path.basename(fileitem.filename)
    #abrir archivo desde la carpeta img, con el nombre recibido en modo escritura binaria porque es una imagen y se escribe el contendio del archivo cargado
    #en el archivo recien creado
    open("img/" + fn, 'wb').write(fileitem.file.read())
    #variable para imprimir la tabla. Llamamos a la funcion tabla y le pasamos la ruta del archivo recien creado
    crearTabla("img/"+ fn)
