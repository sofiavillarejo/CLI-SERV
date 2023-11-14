#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

#.py que genera un contenido HTML con un titulo y un h1. Seguidamente se crea una funcion que contiene las operaciones
#a realizar. Se utiliza un bucle para recorrer la lista de numeros a sumar

print("Content-type: text/html\n")

print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>HTML</title>
    </head>
    <body>
        <h1>Operaciones</h1>

""")
#funcion con las operaciones
def operacionesLista():
    numeros = [1,2,3,4,5,6,7,8,9,10]
    operacion = "suma", "producto"
    if operacion =="suma":
        for num in numeros:
            num+=num
        print(num)
    else:
        print("-1")

    if operacion =="producto":
        for num in numeros:
            num*=num
        print(num)
    else:
        print("-1")

print(operacionesLista)

print("""
    </body>
    </html>
""")