#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

print("Content-Type: text/html\n")

fileitem = form['filename']#nombre de archivo del cliente

def crearLista(nomFich):
    
    #abrir fichero
    with open(nomFich) as fichero:
        #tratar la primera linea para crear la cabecera
        linea = fichero.readlines()
        lista = "<ol>\n"
        datos = linea[0].split(",")
        lista += f"<li>{datos[0]}\n"
        
        lista+="<ol>"

        for li in datos[1:]:
            lista += f"<li>{li}</li>\n"
        lista+="</ol>"
        lista+="</li>"
        lista+="</ol>"

        return lista
 
if fileitem.filename:
    fn = os.path.basename(fileitem.filename)
    open("img/" + fn, 'wb').write(fileitem.file.read())

    print(crearLista("img/"+ fn))
    
    