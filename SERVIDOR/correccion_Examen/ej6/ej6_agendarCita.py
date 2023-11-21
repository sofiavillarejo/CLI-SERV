#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

#PARA INSERTAR INFO:
#recuperar los datos a intertar (param) del formulario
#recuperar de la BBDD el id del paciente, si no existe no se inserta
#insertar la informacion en la tabla citas_medicas

import os, mysql.connector, codHtml
from urllib.parse import urlparse, parse_qs

print("Content-type:text/html\n")

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

nombre = param["nombre"][0]
fecha = param["fecha"][0]
hora = param["hora"][0]
consulta = param["consulta"][0]

#comprobar qué datos me están llegando
#print(nombre, fecha, hora, consulta)

#conexion a bbdd
midb = mysql.connector.connect( 
    host = "localhost",
    user = "clinica",
    password = "clinica",
    database = "clinica"
)

miCursor = midb.cursor() #crear cursor

consultaIDPaciente = "SELECT id FROM pacientes WHERE nombre='"+nombre+"'" #buscamos por id a traves del texto que nos pase el usuario en el campo nombre

miCursor.execute(consultaIDPaciente) 

miresultado = miCursor.fetchone() #trae una fila

miCursor.close() 

if miresultado == None:
    codHtml.cabHTMLGen()
    print("<p>Error, el paciente no existe</p>")
    codHtml.finHTMLGen()
else: #si el paciente existe
    id = miresultado[0] #meto en un variable id lo que me trae la consulta en el campo 0, que es el id
    #inserto en la tabla una vez ya tenga el id
    miCursor = midb.cursor()
    insertaCita = "INSERT INTO citas_medicas (fecha_cita, hora_cita, consulta, id_paciente) VALUES (%s, %s, %s, %s)"
    val = (fecha, hora, consulta, id)
    miCursor.execute(insertaCita, val)
    midb.commit()
    miCursor.close()
    codHtml.cabHTMLGen()
    print("<p>Cita insertada</p>")
    codHtml.finHTMLGen()

#para ver qué me está trayendo
# print("---")
# print(miresultado)




#cerrar BBDD
midb.close()

