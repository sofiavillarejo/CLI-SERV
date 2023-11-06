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
                </tr>
            '''
            borrado = "<a class='btn btn-danger' href='borrar.py?id=" + str(datosVideojuego[0])+ "'>borrar</a>"
            #recorrer la tupla
            tabla += fila.format(datosVideojuego[0], datosVideojuego[1], datosVideojuego[2], datosVideojuego[3], datosVideojuego[4], datosVideojuego[5], borrado) #id, nombre, empresa, tematica, nº jugadores y año de publicacion

    tabla += "</table>"
    contenidoFin = '''
            </div>
                <div class="col"></div>
            </div>
        '''
    #imprimir todo en html
    print(contenidoIni)
    print(tabla)
    print(contenidoFin)
    finHTML()