#!C:\Users\Sofía\AppData\Local\Programs\Python\Python311\python.exe
#es un lenguaje interpretado y no compilado

#imprimir
print("Hola Python")
print('Hola Python')

'''
Este es un comentario
con varias lineas
'''

#numeros-> integer (enteros), float (decimales)
#string
#boolean
#listas
#diccionarios
#set
#tuplas

#consultar tipo de dato
print(type('Hola mundo')) #impirme class str (string-> cadena de texto)
print(type (2)) #imprime int
print(type(True)) #imprime bool
print(type(1.5))#imprime float

#VARIABLES Y ALGUNAS FUNCIONES DEL SISTEMA
miVariable = 'hola'
print(len(miVariable)) #saca las letras totales que tiene

#variables en una línea
nombre, apellido = "Sofia", "Villarejo"
print("Me llamo:", nombre, "y mi apellido es:", apellido)

#pedir datos al usuario en consola
"""
name = input("¿Cual es tu nombre? ")
edad = input("¿y tu edad? ")

print(name, edad)
"""

#OPERADORES
print(3+4)
print(3 > 4 or "hola" < "Python")
print( 3 < 4 or (4 > 3 and 4 == 4))
print(not (3 > 4)) #el contrario de 3 mayor que 4 --> 3 > 4 no pues da true

#STRINGS
myString = print('Esto es un string \ncon salto de linea')
myString2 = print('\tEsto es un string con tabulación')

#formateo
nom, apellidoo, age = "sofia", "villarejo", 22
print("Mi nombre es {} {} y mi edad es {}".format(nom, apellidoo, age))
print("Mi nombre es %s %s y mi edad es %d" %(nom, apellidoo, age))
print(f"Mi nombre es {nom} {apellidoo} y mi edad es {age}")

#DESEMPAQUETADO DE CARACTERES
lenguaje = "Python"
a,b,c,d,e,f = lenguaje
print(a,b,d)

#DIVISION DE CARACTERES
lenguaje_slice = lenguaje[1:3] #coge desde la segunda y tercera letra (la priemra letra es la pos 0)
print(lenguaje_slice)

lenguaje_slice = lenguaje[1:]
print(lenguaje_slice)

lenguaje_slice = lenguaje[-2]
print(lenguaje_slice)

lenguaje_slice = lenguaje[::-1]
print(lenguaje_slice) #lo imprime del reves

#funciones tipicas existentes con variables
print(lenguaje.capitalize())
print(lenguaje.upper())
print(lenguaje.count("t"))
print("1".isnumeric())
print(lenguaje.lower())
print(lenguaje.upper().isupper())
print(lenguaje.startswith("Py"))

#########################################################################
#LISTAS --> array, cada elemento que se añade tiene su posición (es como una caja)
#en ellas guardamos datos
miLista = list()
miLista2 = []

print(len(miLista))

miLista = [35, 22, 12, 45]
print(miLista)
print(len(miLista))

miLista2 = [22, 1.23, "Sofia"]
print(type(miLista2))

#acceder a los valores que hay dentro de la lsta
print(miLista2[0])
print(miLista2[-1])
print(miLista2[0])

print(miLista2.count(22)) #cuenta los 22 que hay dentro de la lista, que en este caso, es 1

#asignar variables a los valores de la lista para imprimirlos por el nombre de variable
age, altura, nombree = miLista2
print(nombree)

#junta las dos listas en 1
print(miLista + miLista2)

#añadir valores a una lista
miLista2.append("Villarejo")
print(miLista2)

miLista2.insert(1, "Azul") #insertar en la posicion elegida el valor
miLista2.remove("Azul")#eliminar un valor

#borrar el último elemento añadido a la lista
miLista.pop()
print(miLista)
print(miLista.pop()) #con esto se imprime el valor que se borra
print(miLista)

#limpiar la lista
miLista.clear()
print(miLista)

#cambiar valor de una posicion
miLista2[2] = "Marta" #cambia sofia por marta
listaCopiada = miLista2.copy()
print(listaCopiada)

#darle la vuelta a la lista
listaCopiada.reverse()
print(listaCopiada)

#ordenar una lista numerica de menor a mayor
listaNumerica = [1, 5, 6, 3, 8, 10, 23, 45, 11]
listaNumerica.sort()
print(listaNumerica)

#sublistas
print(miLista2[1:3])

####################################################################
#TUPLAS -->conjunto de valores
#LA DIFERENCIA CON LAS LISTAS ES QUE NO TIENEN OPERACIONES (AÑADIR, BORRAR...)
tupla = tuple()
tupla2 = ()

tupla = (22, 1.70, "Sofia", "Villarejo")
print(type(tupla))
print(tupla[0])
print(tupla.count(22))
print(tupla.index(1.70)) #indica la posicion del elemento en la tupla
tupla2 = ("hola", "adios")
sumaTupla = tupla + tupla2
print(sumaTupla)
print(sumaTupla[1:4])

#cambiar de tupla a lista
tupla = list(tupla)
print(type(tupla))
tupla.insert(4, "nuevo valor")
print(tupla)

#vuelvo a asignarle el valor de tupla, y aparece tambien el nuevo valor
tupla = tuple(tupla)
print(type(tupla))

#del tupla #con eso se borra la tupla y la variable
#print(tupla)
""""
no se pueden reasignar valores
tupla[1] = 1.80
print(tupla)

LAS TUPLAS SON CONJUNTOS DE VALORES CERRADOS --> NO SE PUEDEN CAMBIAR
"""
################################################
#SETS
miSet = set()
miSet2 = {} 

print(type(miSet2)) #asi inicialmente es un diccionario
miSet2 = {22, 1.70, "Sofia"}
print(type(miSet2)) #aqui ya es un set
print(len(miSet2))

#es una estructura no ordenada y NO ADMITE REPETICIONES
miSet2.add("Villarejo")#al añadir algo, se mete en el hueco que quiere
print(miSet2)
miSet2.add("Villarejo")#NO AÑADE ESTE ELEMENTO DOS VECES PORQUE YA ESTÁ 1
print(miSet2)

#tampoco se puede acceder a los elementos porque realmente no sabemos su posicion
#porque es aleatoria
print("Sofia" in miSet2) #comprobar si lo que buscas esta en el set
miSet2.remove(22) #borrar elemento
print(miSet2)
miSet2.clear() #vaciar lista
print(len(miSet2))

#borrar set
"""
del miSet2
print(miSet2)
"""
#cambiar set a lista
miSet = {12, 23, 54}
miListaSet = list(miSet)
print(type(miListaSet))

#unir dos sets en uno mismo .union()
miSet2 = {"hola", 22,34}
nuevoSet = miSet.union(miSet2)
print(nuevoSet)
#añadir contenido con union()
print(nuevoSet.union({"que tal", "genial"}))

#el difference() quita los elementos del set que haya en el segundo que añadas
print(nuevoSet.difference(miSet)) #se restan los valores que haya en miSet

#################################################
#DICCIONARIOS
diccionario = dict()
diccionario2 = {}
#relacion clave-valor
diccionario2 = {"Nombre":"Sofia", "Apellido":"Moure", "Edad":22, 1:"Java"}
diccionario = {
    "Nombre":"Sofia", 
    "Apellido":"Moure", 
    "Edad":22, 
    "Lenguajes": {"Java", "Python"}
}
print(len(diccionario2))
print(diccionario2["Nombre"])#clave para acceder al elemento que se guarda dentro (Sofia)
diccionario2["Nombre"] = "Pancracia" #reasignar valor 
print(diccionario2) #el nuevo valor de la clave Nombre es Pancracia

del diccionario2["Apellido"]
print(diccionario2)

print("Sofia" in diccionario)#da falso porque se busca por clave y le estamos pasando el valor
print("Apellido" in diccionario) #true

print(diccionario2.items()) #cada una de las claves + valor
print(diccionario2.keys()) #claves
print(diccionario2.values()) #valores 

#fromkeys() crea un diccionario nuevo sin valores -> no es funcional
nuevoDic = diccionario2.fromkeys(("Nombre", 1, "Piso"))
print(nuevoDic)

#conventir el diccionario en otro (aunque en los demas solo imprime las claves)
print(diccionario)
print(list(diccionario.values()))#con esto imprimiria los valores en vez de las claves
print(tuple(diccionario))
print(set(diccionario))

##########################################################
#CONDICIONALES
#deciden si algo de nuestro codigo se ejecuta o no


miCondicion = False
if miCondicion == True: #al poner que: si miCondicion es = True, pues no se ejecuta porque la hemos declarado como False 
    print("Se ejecuta la condicion")
print("la condicion se continúa")


multi = 5*2
if multi <=20:
    print(multi)
else:
    print("la multiplicacion es superior a 20")
print("la ejecucion continua")

num1 = 20
num2 = 15
if num1 <=30 and num2 >=10:
    print("Ambos cumplen las condiciones")
else:
    print("ninguno cumple las condiciones")

if num1 <=13 or num2 >=20:
    print("al menos uno cumple las condiciones")
elif num1 == 20: #imprime esto porque la condicion de arriba no se cumple
    print("Si, el  numero 1 es igual a 20")
else:
    print("ninguno cumple las condiciones")

cadenaTexto = ""
if not cadenaTexto:
    print("Cadena de texto vacía")
if cadenaTexto == "":
    print("correcto")

###############################################
#BUCLES
    #WHILE
cond = 1
while cond <10:
    print(cond)
    cond += 2 #cond = cond + 1 incrementa cada vez 2 el valor
    #se imprime hasta que sea menor que 10 -> 9
else: #es opcional
    print("ya se ha cumplido la condicion y ya no se cumple")
print("el bucle se ha cumplido y continúa la ejecución")

condicion = 2
while condicion <16:
    print(condicion)
    condicion += 2
    if condicion == 14: #cuando el valor suma 14, se imprime este print pero luego continua la suma hasta 16
        print("la condicion ya ha llegado a 14")

numm = 2
while numm <20:
    print(numm)
    numm += 2
    if numm == 14: #cuando el valor suma 14, se imprime este print pero luego continua la suma hasta 16
        print(numm)
        break #cuando la suma llegue a 14, se para la ejecucion del bucle

print()

    #FOR -> imprime estructuras iterables (que almacenan mas de un valor)
listaa = [10, 20, 30, 40]
for numeros in listaa: #recorre la lista
    print(numeros)

for valores in diccionario.items():
    print(valores)
else:
    print("el bucle for para diccionario ha terminado")

for valores in diccionario:
    print(valores)
    if valores == "Edad": #si recorriendo el diccionario se encuentra la clave edad, se detiene
        break
else: #al poner el break, esta parte tampoco se ejecutaría
    print("el bucle for para diccionario ha terminado")

for valores in diccionario:
    print(valores)
    if valores == "Edad": #si recorriendo el diccionario se encuentra la clave edad, se detiene
        continue
else: #al poner el continue, se sigue ejecutando todo aunque encuentre "Edad"
    print("el bucle for para diccionario ha terminado")

###############################################
#FUNCIONES

def miFunc():
    print("Esto es una funcion")
miFunc() #con esto llamas a la funcion y se ejecutaria

def sumDosValores(num1, num2):
    print(num1 + num2)
sumDosValores(5,7)

def valoresReturn(num1, num2):
    return num1 + num2
resultado = valoresReturn(10,5) #para que lo imprima hay que almacenar el return en alguna varibale
print(resultado)

def imprimirNom(nombre, ape, alias = "sin alias"):
    print(f"{nombre} {ape} {alias}")
imprimirNom("Sofia", "Villarejo", alias ="Sofi")#cambiamos aqui el valor del alias

##########################################
#EXCEPCIONES
numero1 = 5
numero2 = 1
numero3 = "1"

try: #ejecuta este codigo
    print(numero1+numero2)
    print("No hay errores")
except: #si hay algun error, se ejecuta este
    print("Se ha producido un error")
else: #no hay errores? se ejecuta este tambien
    print("La ejecución continúa correctamente")
finally: #se ejecuta siempre
    print("Se han sumado los numeros con éxito")

#########################################
#MANEJO DE FICHEROS
#######
#.TXT
#r -> escritura, w+-> leer y escribir

import os

fiche = open("ficheros/fich.txt" , "w+") #creamos variable del fichero y le asignaos que se abra con la ruta y el nombre que tiene + modo lectura
#print(fich.read()) #imprimimos el fichero mientras le leemos
#print(fich.read(4)) #imprime solo 4 caracteres
#print(fich.readlines()) #lo imprime como una lista
#leer cada una de las lineas
for linea in fiche.readlines(): 
    print(linea)
#escribir en el ficheero con un salto de linea(sino lo escribe de seguido)
fiche.write("\nHola mi nombre es Sofia")
print(fiche.readline())

#cuando terminamos con el fichero, cerrarlo siempre
fiche.close()

#eliminar el fichero
#os.remove("ficheros/fich.txt") #si despues de borrarle ejecuto el codigo anterior, se vuelve a crear

########
#.JSON
import json

fichJson = open("ficheros/fichJson.json" , "w+")

json_texto = {
"nombre":"Sofia",
"ape":"Villarejo",
"edad":"22",
"web":"sofia.com"
}
#añadir texto al fichero json dump(variable con el nuevo texto, fichero al que se lo añadimos)
json.dump(json_texto, fichJson)

fichJson.close()

with open("ficheros/fichJson.json") as fichJson2:
    for linea in fichJson2.readlines():
        print(linea)

#leer fichero y trasnformarlo a un diccionario
fichJson = open("ficheros/fichJson.json")
#load()-> cambia de json a diccionario
jsonDicc = json.load(fichJson)
print(jsonDicc)
print(type(jsonDicc))
print(jsonDicc["ape"])#acceder con la clave al valor que tiene

