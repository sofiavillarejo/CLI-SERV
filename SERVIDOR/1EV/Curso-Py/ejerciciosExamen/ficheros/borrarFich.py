#!C:\Users\Sofía\AppData\Local\Programs\Python\Python312\python.exe

import os

print("Content-type: text/plain\n")

fich = open("fichBorrador.txt", "wt")
fich.write("Hola que tal, esto es una prueba")
fich.close()

if os.path.exists("fichBorrador.txt"):
  os.remove("fichBorrador.txt")
else:
  print("The file does not exist")