#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

# API ->libreria que trabaja con datos
# me interesa que me devuelva una lista de datos
from BDvideojuegos import BDVideojuegos
import json


## generar salida para el cliente ajax
print("Content-Type: application/json\n")


bd = BDVideojuegos()


miresultado = bd.todosLosVideojuegos()


print(json.dumps(miresultado))