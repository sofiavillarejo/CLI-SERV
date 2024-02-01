#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe


#abrir ficheros -> open(nombreFichero, modo)
# "r"-> leer, saca un error si el fichero no existe
# "a"-> añadir, crea el fichero si no existe
# "w"-> escribir, crea el fichero si no existe
# "x"-> crear, devuelve un error si el fichero no existe 

# además, se puede especificar si el archivo debe ser manejado como texto o como binario
# "t"-> texto, por defecto
# "b"-> binario

print("Content-type: text/plain\n")

import os

dir = "datos/" #variable directorio
nombreFich = "palabras.dat" #variable del fichero

'''
ABRIR FICH Y ACCEDER A EL
fich = open(dir+nombreFich) 

#contenido = fich.read() #permite leer todo el contenido del fichero

#contenido2 = fich.readline() LEER UNA LINEA

#print(contenido)

LEER E IMPRIMIR EL FICHERO 
#print(fich.read())

#bule for para ir leyendo todo el contenido
#for contenido in fich: MEJOR FORMA PARA RECORRER FICHEROS
#    print(contenido)
#contenido = fich.readline()

#while contenido:
#    print("-"+contenido)
#   contenido = fich.readline()
    #continue --> esta instrucción aqui volvería a ejecutar el while y no llega al else2
    #break tambien existe y se usa para que no se ejecute el else
#else: #se ejecuta como última instrucción del while
 #   print("Fin de fichero")
#cerrar fichero

#para leer lineas
#for linea in fich:
#    print(linea)

#print(fich.readlines(7)) #lee el numero de caracteres que pongas pero completa hasta el final de la linea y lo saca en array

#listaDias = fich.readlines()
#print(listaDias[4])#crea una lista e imprime el 5 elemento dentro

#recorre el array e imprime los dias
#for dia in listaDias:
#    print(dia)

#if 'Lunes\n' in listaDias:
#    print("esta el lunes en el fichero")

listaDias = [dia.strip('\n') for dia in fich.readlines()]#guardo cada una de las lineas que voy leyendo y quito el \n
print(listaDias)#imprimo la lista de dias sin el \n
fich.close()
'''
#errores
'''
try:
    fich = open(dir+nombreFich,"at")#at es para añadir texto: append + text; si pongo una w me escribe y borra todo lo anterior
#si pongo una x me crea el fichero y lo escribe lo que ponga
    fich.write("\ny vuelta a empezar")
    fich.close()
except FileExistsError:
    print("problema al abrir el fichero")
else:
    fich.write("y vuelta a empezar")
finally:
    fich.close()
'''
#para saber el directorio actual de trabajo
#importar el os 
print(os.getcwd())

#para saber si un path es un directorio
print(os.path.isdir(dir))

#para saber si un path es un fichero
print(os.path.isfile(dir))
print(os.path.isfile(dir+nombreFich))

#para cambiar de directorio de trabajo
os.chdir(dir)
print(os.getcwd())
#se pueden abrir los ficheros que hay en el directorio de trabajo sin indicar el path
f = open(nombreFich)
print(f.readlines())
f.close()