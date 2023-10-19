def cabeceraHtml():
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cajero</title>
    </head>
    <body>
        <h1>Bienvenido al cajero automatico</h1>
    """)
    
def finHtml():
    print("""
    </body>
    </html>
    """)

def htmlRecarga():
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="refresh" content="1;cajero.py">
        <title>Cajero automático</title>
    </head>
    <body>
          <h1>Cuentas</h1>
          <h3>Tu cuenta se está creando</h3>
    </body>
    </html>
    """)

def crearCuenta():
    print("""
        <form action="crearCuenta.py" method="get">
        <button type="submit">Crear Cuenta</button>
        </form>
    """)
