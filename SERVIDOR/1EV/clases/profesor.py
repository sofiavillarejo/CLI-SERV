from persona import Persona

class Profesor(Persona):
    def __init__(self, nom, apell, ed):
        Persona.__init__(self, nom, apell, ed)
        self.asignaturas = [] #lista de asignaturas

    def __str__(self):
        return f"{self.nombre} {self.apellidos}, {self.edad}, profesor."
    
    def listaModulos(self):
        return self.asignaturas
    
    def addAsignaturas(self, nombreAsig):
        self.asignaturas.append(nombreAsig)