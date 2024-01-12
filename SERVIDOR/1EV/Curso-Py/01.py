#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe
######ESTRUCTURA REPETITIVA##############
#BUCLE WHILE
print("Content-type: text/html\n")

año = 2001
while año <= 2010:
    print(f"Informe del año: {año} <br/>")
    año += 1
else:
    print("el bucle ha terminado")

#RANGE
#es como ir incrementando un contador, pero esto lo hace directamente
#la variable cont se incrementa sola del 1 al 14 en este caso
for cont in range (1,15): #para una variable cont en un rango de 1 al 14, imprime parrafos
    print(f"<p>Este es el parrafo {cont}.</p>")

print()
############LISTAS################
#MÉTODOS DE LISTAS
# .append(valor) -> añadir un elemento al final de la lista
#.extend(nombre_lista) -> añadir otra lista nuerva al final de nuestra lista inicial
#.copy -> copiar una lista
#.insert(pos, valor) -> elegir la posicion y el valor que añadimos a la lista
#.remove(valor_aBorrar) -> borrar directamente el primer elemento que encuentre que coincida con el valor que quieres borrar (pop nos devuelve el valor que se borra)
#.sort() -> ordena la lista
#.clear -> vaciar lista
#.count(valor) -> cuenta las veces que aparece el valor indicado en la lista
#.index(valor,start) -> devuelve el primer indice (posicion) donde se encuentra el valor (a partir de la posicion x -> start)
#.pop -> devuelve el ultimo elemento y lo borra de la lista (se puede elegior la posicion -> pop(2))
#.reverse() -> imprimir la lista al reves

#ejemplos->

miLista = [1,3,2,5,6,7,34,21,1]
lista2 = ["hola", "adios"]
miLista.append(88)
miLista.extend(lista2)
lista3 = miLista.copy()
miLista.insert(2, 189)
miLista.remove(189)
lista2.sort()
lista3.clear()
print(miLista.count(1))
print(miLista.index(1,4))
print(miLista.pop())#adios
print(miLista.reverse())

print(miLista)
print(lista2)
print(lista3)

print()
#######TUPLAS################
#no se pueden modificar las tuplas, solo se pueden almacenar valores
#MÉTODOS DE TUPLAS
#.count(valor) -> cuenta las veces que aparece el valor indicado en la tupla
#.index(valor,start) -> devuelve el primer indice (posicion) donde se encuentra el valor (a partir de la posicion x -> start)

tupla = 1,2,3,1
a, b, c,d = tupla
print(a,b,c,d)

for num in tupla:
    print(num)

print(tupla.count(1))#contar
print(tupla.index(2))#posicion del numero 2 en la tupla

print()

#######RANGOS##########
#se usa para crear bucles for de secuencia de numeros

rango = range(10,20,2)#rango del 10 al 19 de 2 en 2

for i in rango:
    print(i)

print("El rango empieza por: " + str(rango.start))
print("El rango termina por: " + str(rango.stop))
print("El intervalo del rango es de " + str(rango.step) + " en " + str(rango.step))