#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe

print("Content-Type: text/html\n")

import os, codigo
try:
    #abrir el fichero en modo lectura
    fich = open("listaSalarios.dat") 
except: 
    #se crea el fichero si da error al abrir
    print("se crea el fichero en datos")
    fich = open("listaSalarios.dat", "x")

#leemos el contenido del fichero en una lista de salarios si no está vacío
if os.path.getsize("listaSalarios.dat") != 0: 
    salarios = fich.readlines()
else:
    salarios = []
#cerrar fichero
fich.close()

def listaDeSalarios():
    if len(salarios) != 0:#si hay salarios, se crea la lista
        print("<ol>")
        sala = [s.strip('\n') for s in salarios] #quitar saltos de linea de la lista
        for s in sala:
            #separamos el producto de la caantidad por ;
            elem = s.split(";")
            print(f"<li>Salario: {elem[0]}  Gastos:  {elem[1]} </li>")
        print("</ol>")
        
    else:
        print("<h3>Lista de salarios vacía</h3>")
    print("<hr/>")

#importamos html del otro archivo (crear cabecera)
codigo.cabeceraHtml()

#metodo que imprime la lista de la compra
listaDeSalarios()

#crear formulario
codigo.formulario()

#crear fin del html
codigo.finHtml()