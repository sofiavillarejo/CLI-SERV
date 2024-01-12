#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

print("Content-type: text/plain\n")

import os
from urllib.parse import urlparse, parse_qs

ru= os.environ.get("REQUEST_URI")
parametros = urlparse(ru)

#COGER VARIOS PARAMETROS A LA VEZ Y METERLOS EN LA MISMA LISTA
params = parse_qs(parametros[4])

asig = params.get("asignatura", [])

listaAsig = []
listaAsig.extend(asig)
print(listaAsig)

