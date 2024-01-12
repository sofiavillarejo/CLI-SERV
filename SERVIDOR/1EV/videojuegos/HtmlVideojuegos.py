def cabeceraHTML():
    cab = '''
    <!DOCTYPE html>
    <html>  
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Videojuegos Antiguos</title>

        <!-- Latest compiled and minified CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet">
        <!-- Latest compiled JavaScript -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js"></script>
    </head>
    <body>
'''
    print(cab)

def cabeceraHTMLRedireccionPrincipal():
    cab = '''
    <!DOCTYPE html>
    <html>  
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Videojuegos Antiguos</title>

        <!-- Latest compiled and minified CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet">
        <!-- Latest compiled JavaScript -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js"></script>
        <meta http-equiv="refresh" content="5;principal.py">
    </head>
    <body>
'''
    print(cab)

def finHTML():
    fin = ("""
    </body>
    </html
""")
    
    print(fin)

def salidaPrincipal(listaVideojuegos):#listaVideojuegos se lo pasamos en principal con bd.todoslosvidejuegos() y se le puede dar el nombre que queramos aqui
    cabeceraHTML()
    contenidoIni = '''
        <div class="row mt-3">
            <div class="col-3">
                <h3>Filtro</h3>
                <a class="m-3 btn btn-secondary" href="principal.py">Ver todos</a>
                 <form action="filtros.py"  class="m-3">
                    <div>
                        <label for="empresa" class="form-label">Empresa</label>
                        <input type="text" class="form-control" name="empresa">
                    </div>
                    <div>
                        <label for="tematica" class="form-label">Tematica</label>
                        <input type="text" class="form-control" name="tematica">
                    </div>
                    <div>
                        <label for="jugadores" class="form-label"> numero de jugadores</label>
                        <input type="text" class="form-control" name="jugadores">
                    </div>
                     <div>
                        <label for="anioInicial" class="form-label">Desde el año</label>
                        <input type="text" class="form-control" name="anioInicial">
                    </div>
                     <div>
                        <label for="anioFinal" class="form-label">Hasta el año</label>
                        <input type="text" class="form-control" name="anioFinal">
                    </div>
                        <button class="mt-3 btn btn-secondary">Filtrar</button>
                </form>
            </div>
            <div class="col-6 bg-secondary text-light text-center">      
                <h1 class="display-5">Videojuegos Antiguos</h1>
        '''
    
    tabla = '''<table class="table table-striped" >
            <thead>
            <tr>
                <th>ID</th>
                <th>Nombre</th>
                <th>Empresa</th>
                <th>Tematica</th>
                <th>Numero de jugadores</th>
                <th>Año de publicacion</th>
                <th></th>
                <th></th>
            </tr>
            </thead>
        '''
    #recorrer la lista de todos los videojuegos para imprimirlos en forma de tabla
    for datosVideojuego in listaVideojuegos:
            fila = '''<tbody>
                <tr>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                </tr>
            '''
            borrado = "<a class='btn btn-danger' href='borrar.py?id=" + str(datosVideojuego[0])+ "'>borrar</a>"
            modificar = "<a class='btn btn-danger' href='modificarFormulario.py?id=" + str(datosVideojuego[0])+ "'>modificar</a>"
            #recorrer la tupla
            tabla += fila.format(datosVideojuego[0], datosVideojuego[1], datosVideojuego[2], datosVideojuego[3], datosVideojuego[4], datosVideojuego[5], borrado, modificar) #id, nombre, empresa, tematica, nº jugadores y año de publicacion

    tabla += "</table>"
    contenidoFin = '''
            </div>
                <div class="col-3">
                    <a class="btn btn-secondary" href="insertarFormulario.py">Insertar</a>
                </div>
            </div>
        '''
    #imprimir todo en html
    print(contenidoIni)
    print(tabla)
    print(contenidoFin)
    finHTML()

def error(msgError):
    cabeceraHTMLRedireccionPrincipal()
    print("""
        <div class="row mt-3">
            <div class="col-3"></div>
                <div class="col-6">
                    <h3 class="display-3">
    """)
    print(msgError)
    print("""
                    </h3>
                </div>
            </div>
            <div class="col-3"></div>
        </div>
    """)
    finHTML()

def formularioInsertar():
    cabeceraHTML()
    contenidoFormulario = """<div class="row mt-3">

                        <div class="col-3"></div>
                        <div class="col-6 bg-secondary text-light text-center">                              
                            <h3 class="display-3">Datos del juego</h3>
                            <form action="insertar.py"  class="m-3">
                                <div>
                                    <label for="nombre" class="form-label">nombre</label>
                                    <input type="text" class="form-control" name="nombre">
                                </div>                              
                                <div>
                                    <label for="empresa" class="form-label">Empresa</label>
                                    <input type="text" class="form-control" name="empresa">
                                </div>
                                <div>
                                    <label for="tematica" class="form-label">Tematica</label>
                                    <input type="text" class="form-control" name="tematica">
                                </div>
                                <div>
                                    <label for="nJug" class="form-label">Número de jugadores</label>
                                    <input type="text" class="form-control" name="nJug">
                                </div>                                                            
                                <div>
                                    <label for="anio" class="form-label">Año publicación</label>
                                    <input type="text" class="form-control" name="anio">
                                </div>                                                                                                                    
                                <button class="mt-3 btn btn-secondary">Enviar</button>
                            </form>

                        </div>
                        <div class="col-3"></div>
                    """
    print(contenidoFormulario)
    finHTML()

def formularioModificar(datos): #datos es la tupla que contiene todos
    cabeceraHTML()
    contenidoFormulario = f"""<div class="row mt-3">

                        <div class="col-3"></div>
                        <div class="col-6 bg-secondary text-light text-center">                              
                            <h3 class="display-3">Datos del juego</h3>
                            <form action="modificar.py"  class="m-3">
                                    <input type="hidden"s name="id" value="{datos[0]}">    
                                <div>
                                    <label for="nombre" class="form-label">nombre</label>
                                    <input type="text" class="form-control" name="nombre" value="{datos[1]}">
                                </div>                              
                                <div>
                                    <label for="empresa" class="form-label">Empresa</label>
                                    <input type="text" class="form-control" name="empresa" value="{datos[2]}">
                                </div>
                                <div>
                                    <label for="tematica" class="form-label">Tematica</label>
                                    <input type="text" class="form-control" name="tematica" value="{datos[3]}">
                                </div>
                                <div>
                                    <label for="nJug" class="form-label">Número de jugadores</label>
                                    <input type="text" class="form-control" name="nJug" value="{datos[4]}">
                                </div>                                                            
                                <div>
                                    <label for="anio" class="form-label">Año publicación</label>
                                    <input type="text" class="form-control" name="anio" value="{datos[5]}">
                                </div>                                                                                                                    
                                <button class="mt-3 btn btn-secondary">Enviar</button>
                            </form>

                        </div>
                        <div class="col-3"></div>
                    """
    print(contenidoFormulario)
    finHTML()
