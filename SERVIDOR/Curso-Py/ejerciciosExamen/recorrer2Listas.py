#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe

fich1 = open("fichero2.txt")
fich2 = open("precios2.txt")

listaProd = fich1.readlines()
listaPrec = fich2.readlines()

fich1.close()
fich2.close()

print("Content-type: text/html\n")

print("""<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Mostrar contenido cookie</title>
                </head>
                <body>
    """)

print("<table border='1px'>")
print("<tr><th>Productos</th><th>Precio</th></tr>")

#recorrer dos listas
for prod, prec in zip (listaProd, listaPrec):
        print("<tr>")
        print(f"<td>{prod}</td><td>{prec}</td>")
        print("</tr>")
print("</table>")

print("""
    </body>
    </html>
""")