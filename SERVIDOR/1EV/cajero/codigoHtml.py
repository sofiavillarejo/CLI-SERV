#codigo para mostrar el principio del html
def cabeceraHtml():
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cajero</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet">
        <!-- Latest compiled JavaScript -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js"></script>
    </head>
    <body>
        <div class="mt-3 text-center">
        <h1 class="display-1">Bienvenido al cajero automatico</h1>
        </div>
    """)

#codigo para cerrar el html
def finHtml():
    print("""
    </body>
    </html>
    """)

#codigo que nos lleva a la página de recarga
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
          <div class="mt-3 text-center">
          <h1 class="display-1">Cuentas</h1>
          </div>
          <h3>Tu operacion se está realizando</h3>
    </body>
    </html>
    """)

#codigo del boton de crearCuenta
def crearCuenta():
    print("""
        <form action="crearCuenta.py" method="get">
        <button type="submit" class="btn btn-info">Crear Cuenta</button>
        </form>
        <hr/>
    """)

#codigo que muestra el numero de cuenta y la cantidad para operar con ella y el boton de operar
def operar():
    print("""
    <form action='operar.py' method="get">
        <label for='nc'>Numero de Cuenta</label> <input type='number' name='numC' id='numC'"/>
          <label for='c'>Cantidad</label> <input type='number' name='c' id='c'"/><br/><br/>
            <select id="operacion" name="operacion" class="btn btn-dark">
                <option value="Ingresar">Ingresar</option>
                <option value="Retirar">Retirar</option>
            </select>
            <button type="submit" class="btn btn-success">Operar</button>
    </form>
    """)

#pagina de recarga cuando estamos operando (ingresando o retirando dinero)
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
          <div class="mt-3 text-center">
          <h1 class="display-1">Operacion</h1>
          </div>
          <h3>Tu operacion se esta realizando</h3>
          
    </body>
    </html>
    """)

#pagina que se muestra si ha habido algún error
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

#pagina para consultar los datos y cantidad de la cuenta, le pasamos los valores que vamos a utilizar
def consultarCuenta(numCuenta, historial):
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Consultar cuenta</title>
    </head>
    <body>
        <h1>Consulta de datos de la cuenta: """+ numCuenta + """</h1>
        <ul>"""+ historial + """</ul>
    </body>
    </html>
    """)

