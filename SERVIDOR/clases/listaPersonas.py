#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

from persona import Persona
from alumno import Alumno
from profesor import Profesor

per1 = Persona("Juan", "Rodriguez Garcia", 33)
print("Content-type: text/plain\n")

print(per1.nombreCompleto())
print(per1) #def str

per1.nombre = "Pepe" #cambiar valor
per2 = Persona("Ana", "Lopez Garcia", 43)

if(per2.viva):
    print(f"{per2.nombre} {per2.edad}")
else:
    print("esta muerto")

alu1 = Alumno("Jose", "Garcia Garcia", 18, "DAW")
print(alu1)
print(alu1.nomCiclo())

prof1 = Profesor("Alberto", "Turienzo", 50)
prof1.addAsignaturas("Servidor")
prof1.addAsignaturas("Cliente")
print(prof1)
 #bucle para imprimir todas las asignaturas
for asig in prof1.listaModulos():
    print(asig)