#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
print("Content-type: text/html\n")

def operacionesLista(numeros,operacion):
#     numeros = [1,2,3,4,5]

#     operacion = "suma", "producto"

#     if (operacion == "suma"):
#         # total = 0
#         # for num in numeros:
#         #     total += num
#         # print(f"El resultado de la {operacion} es {total}")

#         total = sum(numeros) #FUNCION QUE REALIZA LA SUMA
#         print(total)

#     if (operacion=="producto"):
#         totalProducto = 0
#         for num in numeros:
#             totalProducto*=num
#         print(f"El resultado del {operacion} es {totalProducto}")

# operacionesLista()

    if len(numeros) == 0:
        return 0
    if operacion != "suma" and operacion != "producto":
        return -1
    if operacion =="suma":
        return sum(numeros)
    if operacion == "producto":
        totalProducto = 1
        for num in numeros:
            totalProducto*=num
        return totalProducto

print(operacionesLista([1,2,3,4,5], "suma"))
print()
print(operacionesLista([1,2,3,4], "producto"))
print()
print(operacionesLista([], "suma"))
print()
print(operacionesLista([], "producto"))
print()
print(operacionesLista([1,2,3,4,5], "division"))

