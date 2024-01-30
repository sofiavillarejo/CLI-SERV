#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

#.py que genera un contenido HTML con un titulo y un h1. Seguidamente abre el directorio que se encuentra 
#en la misma carpeta y se llama "imagenes"

print("Content-type: text/html\n")

#variables del id del div y alt, que luego se van a ir incrementando en cada imagen
idDiv= "Contenedor {1}"
alt = "imagen coche {1}" 

#apertura del html
print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>HTML</title>
    </head>
    <body>
        <h1>Generar HTML</h1>
""")
#abrimos el directorio imagenes y por cada imagen contenida dentro, se crea un div y se imprime cada imagen
#después, se incrementa tanto el id del div como el alt
with open("imagenes/") as directorio:
    for imagen in directorio:
        print(f"<div id={idDiv}>")
        print(f"<img src={imagen} alt={alt} />")
        idDiv+=1
        alt+=1
        print("</div>")

#fin del html
print("""
    </body>
    </html>
""")