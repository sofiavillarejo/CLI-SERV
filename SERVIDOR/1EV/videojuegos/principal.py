#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

"""
BDvideojuegos.py -> clase para conectar a base de datos (MODELO)
FormVideojuegos.py -> clase para tratar los datos del formulario (CONTROLADOR SECUNDARIO)
principal.py -> codigo principal
HtmlVideojuegos.py -> clase para salida de HTML (VISTA)
APIVideojuegos-> clase para la api de videojuegos (CONTROLADOR PRINCIPAL QUE SE APOYA EN FormVideojuegos.py)
"""
from BDvideojuegos import BDVideojuegos
import HtmlVideojuegos
print("Content-Type: text/html\n")
#crear BBDD
bd = BDVideojuegos() #creamos variable que contiene la clase BDVideojuegos.py

#pido todos los videojuegos a la base de datos
#print(str(bd.todosLosVideojuegos()))

#llamar a la funcion de salida
HtmlVideojuegos.salidaPrincipal(bd.todosLosVideojuegos()) #devuelve la lista de todos los videojuegos de la BBDD
#esto en htmlvideojuegos.py es listaVideojuegos

#cerrar BBDD
bd.cerrarBD()