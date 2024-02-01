#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

import codigoHtml
import os,http.cookies

#Comprobar si recibimos la cookie, ya que si la recibios es que el usuario ha entrado bien por el login

if os.environ.get("HTTP_COOKIE") == None:
    codigoHtml.error("No estas logeado en el sistema")
    exit()

cookie = http.cookies.SimpleCookie()
cookie.load(os.environ.get("HTTP_COOKIE"))

if "ID1" in cookie:
    codigoHtml.aplicacion("pagina 1", "pagina2.py")#lo primero es el texto que aparece y lo segundo es el enlace
else:
    codigoHtml.error("No estas logeado en el sistema")
