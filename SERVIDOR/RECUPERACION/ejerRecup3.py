#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

#para mostrar la pagina en html
print("Content-type: text/html\n")

#diccionario que contiene los id de cada producto y cada producto esta en una tupla con dos valores
inventarioProductos = {
    "PRD001": ("Laptop", 1200.00),
    "PRD002": ("Smartphone", 800.00),
    "PRD003": ("Tablet", 400.00),
    "PRD004": ("Monitor", 300.00),
    "PRD005": ("Teclado", 50.00)
}

#imprimir cabecera HTML
print("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Ejercicio 3</title>
        </head>
        <body>
""")
#creamos variable total para calcular el precio del total de productos
total = 0
#creamos la tabla
print("<table border='1px solid black'>")
#imprimimos titulos de cabecera
print(f"<tr><th>Identificador</th><th>Producto</th><th>Precio</th></tr>")
#recorremos el diccionario
for id, producto in inventarioProductos.items(): 
    #imprimir filas y celdas de la tabla pasandole el primer y segundo valor de la tupla
    print(f"<tr><td>{id}</td><td>{producto[0]}</td><td>{producto[1]}</td></tr>")
    #calculamos el total de los precios de los productos metiendolo en la variable total 
    # y sumamos cada precio de cada producto
    total += producto[1]

#imprimir ultima fila de la tabla con el total de productos y lo redondeamos a 2 decimales
print(f"<tr><th>--></th><th>TOTAL</th><th>{total.__round__(2)}</th></tr>")
#cerramos la tabla
print("</table>")
#imprimir fin de HTML
print("""
        </body>
        </html>
""")