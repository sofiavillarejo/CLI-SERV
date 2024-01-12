#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

#listado de citas médicas en este formato:
#nombre del paciente tiene cita en:
#   cita1
#   cita2
#nombre del paciente tiene cita en:
#   cita1
#   cita2
#   cita3

#recuperar de la tabla PACIENTES el id y el nombre del paciente
#con el id, recuperar cada una de las citas del paciente y sacar la informacion

import mysql.connector, codHtml

#conexion a bbdd
midb = mysql.connector.connect( 
    host = "localhost",
    user = "clinica",
    password = "clinica",
    database = "clinica"
)
#crear un cursor, la consulta ejecutar la consulta y obtener los resultados en una lista de tuplas
miCursor = midb.cursor() #crear cursor
consultaIDPaciente = "SELECT id, nombre FROM pacientes"
miCursor.execute(consultaIDPaciente) 
miresultado = miCursor.fetchall() 
miCursor.close() 

print("Content-type: text/html\n")
codHtml.cabHTMLGen()

for paciente in miresultado:
    #salida con el nombre del paciente
    print("<p>El paciente "+paciente[1]+" tiene cita en: </p>")

    #sacar de la bbdd las consultas de cada paciente por id
    miCursor = midb.cursor() #crear cursor
    todasConsultasIDPaciente = "SELECT consulta FROM citas_medicas WHERE id_paciente="+ str(paciente[0])
    miCursor.execute(todasConsultasIDPaciente) 
    resultadoConsultas = miCursor.fetchall() 
    miCursor.close() 

    for consulta in resultadoConsultas:
        print("<p>   "+ consulta[0]+"</p>")

codHtml.finHTMLGen()