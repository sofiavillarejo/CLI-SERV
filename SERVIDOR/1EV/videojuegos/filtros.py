#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

from BDvideojuegos import BDVideojuegos
import HtmlVideojuegos, formVideojuegos
print("Content-Type: text/html\n")
#crear BBDD
bd = BDVideojuegos() 

#llamar a la funcion de salida
HtmlVideojuegos.salidaPrincipal(bd.juegosConFiltro(formVideojuegos.CrearFiltros())) 

#cerrar BBDD
bd.cerrarBD()