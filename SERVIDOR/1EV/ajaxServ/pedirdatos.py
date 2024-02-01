#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe
import mysql.connector
import sys,json

sys.stderr.write("Dentro del pedirdatos.py--------\n") #esto escribe en el archivo error.log


#consulta a la base de datos
#creamos objeto
midb = mysql.connector.connect( 
    host = "localhost",
    user = "pruebajax",
    password = "pruebajax",
    database = "pruebajax"
)

#cursos para hacer peticiones -> objeto que permite hacer consultas a la BBDD
miCursor = midb.cursor()
#crear consulta
consulta = "SELECT * FROM datos" #seleccionamos todos los campos de la tabla datos

#ejecutamos la consulta
miCursor.execute(consulta) 

#devuelve todas las filas que haya en la tabla y se guardan en la variable // 
miResultado = miCursor.fetchall() 

#traza para ver el objeto miResultado
sys.stderr.write(str(miResultado)+"\n") #devuelve una lista de tuplass

#cerrar cursos y conector
miCursor.close()
midb.close()

#generar salida para el cliente ajax
print("Content-Type: application/json\n") #se va a devolver siempre texto plano, pero lo hemo scambiado a applicaction json para indicar
#que vamos a devolver datos en ese tipo de formato

print(json.dumps(miResultado)) #lo devuelve en json porque asi lo tenemos en js, sino no imprime nada


'''
listaNumeros = [1, 1, 2, 3, 5, 8, 13, 21, "hola", "adios"]

print(json.dumps(listaNumeros))

'''

sys.stderr.write("Fin del pedirdatos.py")
