# importamos del archivo persona, la clase Persona
from persona import Persona

class Alumno(Persona):
    def __init__(self, nom, apell, ed, clo):
        Persona.__init__(self,nom, apell, ed)
        self.ciclo = clo

    def __str__(self):
        return f"{self.nombre} {self.apellidos}, {self.edad}, {self.ciclo}"
    
    def nomCiclo(self):
        return "Esta estudiando " + self.ciclo