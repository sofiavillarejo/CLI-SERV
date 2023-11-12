def error(texto):#le pasamos texto para poder escribir en los if y que saque algun mensaje
    print('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="refresh" content="3; index.html">
            <title>Login con registro en fichero</title>
        </head>
        <body>
          <h1>Error</h1>
        ''')
    print(texto) #le pasamos texto para poder escribir en los if y que saque algun mensaje
    print('''`
        </body>
        </html>
    ''')
    
def correcto():
    print('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="refresh" content="3; index.html">
            <title>Login con registro en fichero</title>
        </head>
        <body>
          <h1>Correcto</h1>
        </body>
        </html>
        ''')
    
def aplicacion(texto, enlace):#le pasamos texto para poder escribir en los if y que saque algun mensaje
    print('''Content-type: text/html\n
          
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Login con registro en fichero</title>
        </head>
        <body>
          <h1>Aceros de Hispania</h1>
          <h3>
    ''')
    print(texto) #le pasamos texto para poder escribir en los if y que saque algun mensaje
    #h3 con el texto "pagina 1" indicado en pagina1.py
    print(''' 
        </h3>
        <a href=" 
    ''')
    print(enlace)
    print('''">Enlace a otra pagina</a>
        <a href="logout.py">Logout</a>
        </body>
        </html>
    ''')
