#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe

def saludar():
    print("Hola")

saludar()

#FUNCIONES CON ARGUMENTOS
def saludarDos(nombre):
    #utilizamos la variable que le hemos pasado por parametro
    print("Hola "+nombre+" que tal?")

#aquí le pasamos el valor que va a tener la variable nombre
saludarDos("Sofia")
saludarDos("Carlos")

#FUNCIONES CON RETORNO
def suma(a,b):
    resultado = a + b
    return resultado
print(suma(10,5))

def sumaDos (a, b):
    return a + b
print(sumaDos(20,5))

def sonIguales (num1, num2):
    return num1 == num2
resultado = sonIguales(3,4) #imprime false
if resultado:
    print("si, ambos son iguales")
else:
    print("No, ambos son distintos")

