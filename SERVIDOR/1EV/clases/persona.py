class Persona:
    def __init__(self, nom, apell, ed):
        self.nombre = nom
        self.apellidos = apell
        self.edad = ed
        self.viva = True

    def nombreCompleto(self):#siempre llevan un parametro y se puede poner el nombre que queiras, aunque siempre se suele usar self
        return self.nombre+ " " + self.apellidos
    
    def __str__(self):
        return self.nombre + " "+ self.apellidos + ", "+ str(self.edad)

#CLASE PERSONA QUE ES USADA EN TODAS LAS DEMAS COMO MODELO