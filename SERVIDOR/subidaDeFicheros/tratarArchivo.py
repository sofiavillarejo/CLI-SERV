#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

print("Content-Type: text/html\n")

fileitem = form['filename']#nombre de archivo del cliente

#comprobar que el fichero se ha subido
if fileitem.filename:
    fn = os.path.basename(fileitem.filename) #obtener el nombre del fichero que el cliente me ha enviado

    #abrir un fichero y escribirlo en el servidor (lo guarda en la carpeta img)
    open("img/" + fn, 'wb').write(fileitem.file.read())

    print('<img src="img/' +fn+ '">') #fn variable que contiene el nombre del fichero que ha subido el cliente

    
