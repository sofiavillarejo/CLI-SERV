#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

import http.cookies, os
import funcionesHtml

numTeclados=0
numMonitores=0
numRatones=0

print("Content-type: text/html\n")
cookie = http.cookies.SimpleCookie()

if os.environ.get("HTTP_COOKIE") != None:
    cookie.load(os.environ.get("HTTP_COOKIE"))
    if "teclados" in cookie:
        numTeclados = cookie["teclados"].value
    if "monitores" in cookie:
        numMonitores = cookie["monitores"].value
    if "ratones" in cookie:
        numRatones = cookie["ratones"].value

funcionesHtml.cabeceraHtml()

print("<p>numero de teclados: "+numTeclados+"<br />numero de monitores: "+numMonitores+ "<br />numero de teclados: "+numTeclados+ "</p>")

funcionesHtml.finHtml()