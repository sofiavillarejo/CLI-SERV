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
        <meta http-equiv="refresh" content="2;cajero.py">
        <title>Cajero automático</title>
    </head>
    <body>
          <h1>Cuentas</h1>
          <h3>Tu operacion se está realizando</h3>
    </body>
    </html>
    """)

def crearCuenta():
    print("""
        <form action="crearCuenta.py" method="get">
        <button type="submit">Crear Cuenta</button>
        </form>
        <hr/>
    """)

def consultarCuenta():
    print("""
        <form action="consultarCuenta.py" method="get">
        <button type="submit">Consultar Cuenta</button>
        </form>
    """)

def operar():
    print("""
    <form action='operar.py' method="get">  
        <label for='nc'>Nº Cuenta</label><input type='number' name='numC' id='numC'>
        <label for='c'>Cantidad</label><input type='number' name='c' id='c'>
        <select id="operacion" name="operacion">
          <option value="Ingresar">Ingresar</option>
          <option value="Retirar">Retirar</option>
        </select>
          <button type="submit">Operar</button>
    </form>
    """)

def ingRet():
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="refresh" content="2;cajero.py">
        <title>Cajero automático</title>
    </head>
    <body>
          <h1>Operación</h1>
          <h3>Tu operacion se está realizando</h3>
    </body>
    </html>
    """)
    def error():
        print("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="refresh" content="2;cajero.py">
            <title>Oh,oh</title>
        </head>
        <body>
          <h1>Algo ha salido mal, inténtelo de nuevo</h1>
        </body>
        </html>
        """)

