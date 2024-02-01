#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

import codHtml

#generar informacion desde colecciones de diccionario a tablas

preciosProductosID = {
    "CA132":99.2,
    "CB231":55.7,
    "CA332":101.0,
    "CD5632":65.2,
    "CB838":48.1
}

productosYprecios = {
    "ProductoX":45.5,
    "ProductoY":32.0,
    "ProductoZ":18.7,
    "ProductoW":55.3,
    "ProductoV":29.8
}

print("Content-type:text/html\n")

######2 FORMAS DISTINTAS DE ACCEDER A LOS DATOS##################################
codHtml.cabHTMLGen()
total = 0
print("<table border='1px solid black'>")
print(f"<tr><td>producto</td><td>precio</td></tr>")
for prod, precio in preciosProductosID.items(): 
    print(f"<tr><td>{prod}</td><td>{precio}</td></tr>")
    total += precio
print(f"<tr><td>TOTAL</td><td>{total.__round__(2)}</td></tr>")

print("</table>")
#########################################################################
total = 0
print("<table border='1px solid black'>")
print(f"<tr><td>producto</td><td>precio</td></tr>")
for prod in productosYprecios: #obtengo lista de claves
    precio = productosYprecios.get(prod) #con las claves accedo a los precios
    print(f"<tr><td>{prod}</td><td>{precio}</td></tr>")
    total += precio
print(f"<tr><td>TOTAL</td><td>{total.__round__(2)}</td></tr>")

print("</table>")

codHtml.finHTMLGen()