#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

import codHtml
#EJERCICIO 1

# a)
# crear código html: tiene que presentar 20 imagenes de coches, del coche1.png al coche20.png
#dentro del div va un img. div con id "contenedorN" y img con alt -> "imagen de coche N"


# b)
#crear codigo html: tiene que representar descripciones de producto que estan en un array
#cada producto en un div con id "productoN" y dentro del div p con la descripcion del producto

######################################################################

print("Content-type: text/html\n")

codHtml.cabHTMLGen()

#a)
for i in range(1,21): #rango del 1 al 20
    print(f"<div id='contenedor{i}'>
          <img src='imagenes/coche{i}.png' alt='imagen de coche {i}'>
        </div>")
    

#b)
descripciones_prod = [
"Descripcion del producto 1: Esta es la descripcion del primer producto",
"Descripcion del producto 2: Aquí se encuentra la descripcion del segundo producto",
"Descripcion del producto 3: Esta es la tercera descripcion de un producto",
"Descripcion del producto 4: Cuarta descripcion de un producto de la lista",
"Descripcion del producto 5: La ultima descripcion corresponde al quinto producto"
]

#!SPLIT()-> divide la cadena con el separador indicado y devuelve una lista con los datos
#!SPLITLINES()-> divide la cadena en cada salto de linea y devuelve una lista

cont = 1
for desc in descripciones_prod:
    descProd = desc.split(":")[1].strip() 
    #separo el cotenido del array por los dos puntos, y lo de la segunda posicion (descripciones)
    #lo guardo en la variable para luego imprimirlo en parrafos
    #el strip es para que no me quite el espacio que hay delante de cada descripcion
    print(f"""<div id="producto{cont}><p>{descProd}</p>""")
    cont+=1 #incremento el contador

codHtml.finHTMLGen()