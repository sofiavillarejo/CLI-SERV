#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

from BDvideojuegos import BDVideojuegos
import json, formVideojuegos
print("Content-Type: text/html\n")
#crear BBDD
bd = BDVideojuegos() 

#llamar a la funcion de salida
miResultado = bd.juegosConFiltro(formVideojuegos.CrearFiltros())

print(json.dumps(miResultado))

#cerrar BBDD
bd.cerrarBD()