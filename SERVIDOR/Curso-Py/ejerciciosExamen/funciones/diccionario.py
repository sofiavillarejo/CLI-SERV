#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
print("Content-type: text/plain\n")

def diccionario (frase):
    return {palabra: len(palabra) for palabra in frase.split()}

print(diccionario('Hola que tal estas'))

#FUNCION QUE ME DEVUELVE EL MAYOR DE DOS NUMEROS DE FORMA MANUAL
def numeroMayor (n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

print(numeroMayor(8,2))

#FUNCION QUE ME DEVUELVE EL MAYOR DE LOS TRES NUMEROS CON LA FUNCION MAX
# def mayorTres (n1,n2,n3):
#     return max(n1,n2,n3)
# print(mayorTres(3,23,1))

# print(type(1))
# def esVocal(letra):
#     vocales = ["A", "E", "I", "O", "U"]
#     if letra in vocales:
#         return True
#     if type(letra) == int:
#         print("Lo que has introducido es un numero")
#     if letra != vocales:
#         print("Esta letra no es una vocal")
    

# print(esVocal("A"))
# print(esVocal(2))
# print(esVocal("V"))

#FUNCION QUE DEVUELVE LA PALABRA MAS LARGA DE UNA LISTA
def mas_larga(lista_palabras):
    if not lista_palabras:
        return None  # Devuelve None si la lista está vacía

    palabra_mas_larga = max(lista_palabras, key=len)
    return palabra_mas_larga

# Ejemplo de uso:
lista_palabras_ejemplo = ["gato", "perro", "elefante", "jirafa"]
resultado = mas_larga(lista_palabras_ejemplo)
print(f"La palabra más larga es: {resultado}")

def pares_impares():
    listaNum = [1,2,3,4,5,6]
    esPar = []
    esImpar = []

    for num in listaNum:
        if num%2 ==0:
            esPar.append(num)
        else:
            esImpar.append(num)
    print(esImpar)
    print(esPar)
pares_impares()