#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe
print("Content-Type: text/html\n")

import os, codigoHtml, json


try:
    #abrir el fichero en modo lectura
    fich = open("datos/listaCuentas.dat") 
except: 
    #se crea el fichero en datos si da error al abrir
    fich = open("datos/listaCuentas.dat", "x")

#leemos el contenido del fichero en una lsta de productos si no está vacío
if os.path.getsize("datos/listaCuentas.dat") != 0: 
    cuentas = json.load(fich)
    
else:
    cuentas = []
#cerrar fichero
fich.close()

def listaDeCuentas():
    if len(cuentas) != 0:
        print("<ol>")
        for c in cuentas:
            print(f"<li>Numero de cuenta: {c[0]}  Saldo: {c[1]} euros.<form action='consultar.py'><input type='hidden' name='numC' value={c[0]}><button type='submit' class='btn btn-light'>Consultar</button></li></form>")
        print("</ol>")
    else: 
        print("<h3>No existe ninguna cuenta, debes crear una primero.</h3>")
    print("<hr/>")


#importamos html del otro archivo (crear cabecera)
codigoHtml.cabeceraHtml()

listaDeCuentas()

codigoHtml.crearCuenta()

codigoHtml.operar()
#crear fin del html
codigoHtml.finHtml()