#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

print("Content-type: text/plain\n")

import os
from urllib.parse import urlparse, parse_qs

ru= os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

name = param["nombre"][0]

print(f"Tu nombre es {name.upper()} y tiene {len(name)} letras")

for letras in name:
    print(letras)

#imprimir sin una parte de la cadena
telf = "+34-675302254"
print(telf[4:])#se imprime a partir del 4
print(telf[::-1])#imprimirlo del reves
