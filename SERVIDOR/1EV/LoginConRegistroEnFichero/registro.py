#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import os, codigoHtml, json, hashlib
from urllib.parse import urlparse, parse_qs

ru= os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

#fichero con usuarios
fichUsu = "datos/usuarios.json" #fichero json donde se van a guardar los usuarios

"""
validar que nos envian los parametros
que existen
que contienen algo
que cumplen los requisitos, p.e : la passwd sea de mas de 4 caracteres

el objetivo es guardar el nuevo usuario en el fichero de usuarios

abrir  el fichero de usuarios -> JSON

comprobar que el usuaro no existe en la lista de usuarios

si no existe -> se añade y se vuelve a la pag principal

si existe -> ir a la página de error 

formato de la estructura de datos para la lista de usuarios
[["usuario1", "1234", "usu1@miempresa.com"],["usuario2", "3456", "usu2@mitienda.com"]]
"""

#comprobar que vienen todos los parametros
def validarParametros():
    if "nombre" not in param:
        codigoHtml.error("Falta el nombre")
        exit() #sale del python
    if "pass" not in param:
        codigoHtml.error("Falta la contraseña")
        exit()
    if "email" not in param:
        codigoHtml.error("Falta el correo")
        exit()

    #parametros del usuario a registrar
    nom = param["nombre"][0]
    pas = param["pass"][0]
    ema = param["email"][0]

    #comprobar que la variable tiene algo
    #si el parametro nombre está vacio, error
    if nom == "":
        codigoHtml.error("El nombre tiene que tener algo")#el texto que le pasamos es gracias a pasar el parametro texto en el codgioHtml a la funcion error
        exit() #sale del python
    if pas == "" or len(pas)<4:
        codigoHtml.error("Error, la contraseña tiene que ser de minimo 5 caracteres")
        exit()
    if ema == "" or ema.count("@") != 1:
        codigoHtml.error("El email debe contener algo")
        exit()

    #contraseña encriptada
    pasEnc = (hashlib.sha512(str.encode(pas))).hexdigest()
    
    return [nom, pasEnc, ema] #devuelve una lista porque hemos puesro corchetes, sino devolveria una tupla

def comprobarFichero():
    try:
        fich = open(fichUsu, "a")
    except:
        fich = open(fichUsu, "x") #si no existe, creo el fichero vacío
    
    if os.path.getsize(fichUsu) == 0: #si el fich tiene tamaño 0, creo una lista dentro
        fich.write("[]")#le escribimos eso porque sino los datos no se escriben en el fichero, 
        #entonces para no hacerlo manual. escribimos [] y ya se guardan

    fich.close() #cerrar el fichero


usuario = validarParametros()

#comprobar que el fichero eiste, sino crearlo con una lista vacia
comprobarFichero()

#forma abreviada de abrir ficheros
#obtener del fichero los usuarios registrados
with open(fichUsu) as fichero:
    #json.load(usuario, fichero)#escribirlo en formato json
    try:
        listaUsuarios = json.load(fichero)
    except:
        listaUsuarios = []

usuarioNoEncontrado = True
for usu in listaUsuarios:
    if usu[0]==usuario[0] or usu[2]==usuario[2]:
        usuarioNoEncontrado=False

#añadir el nuevo usuario a la lista
if(usuarioNoEncontrado):
    listaUsuarios.append(usuario)
else:
    codigoHtml.error("Usuario repetido")
    exit()

#escribir los usuarios registrados en el fichero 
with open(fichUsu, "wt") as fichero:
    json.dump(listaUsuarios,fichero)

codigoHtml.correcto()