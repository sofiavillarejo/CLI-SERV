
def cabeceraHtml():
     print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ficheros</title>
    </head>
    <body>
        <div>
        <h1>Ejercicio con ficheros</h1>
        </div>
    """)
     
def finHtml():
    print("""
        </body>
        </html>
    """)

def formulario():
     print("""
    <form action="nuevoDato.py" method="get">
          <label for="salario">Salario:</label>
          <input type="number" name="salario"/><br/>
          <label for="gastos">Gastos:</label>
          <input type="number" name="gastos"/>
          <button>Enviar</button>
    </form>
          """)

def htmlRecarga():
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="refresh" content="3; listaSalarios.py">
        <title>Lista de Salarios</title>
    </head>
    <body>
        <h1>Lista de Salarios</h1>
        <h3>Datos apuntados</h3>
    </body>
    </html>
    """)

#abrir ficheros -> open(nombreFichero, modo)
# "r"-> leer, saca un error si el fichero no existe
# "a"-> añadir, crea el fichero si no existe
# "w"-> escribir, crea el fichero si no existe
# "x"-> crear, devuelve un error si el fichero no existe 

# además, se puede especificar si el archivo debe ser manejado como texto o como binario
# "t"-> texto, por defecto
# "b"-> binario
