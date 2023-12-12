from django.db import models

# Create your models here.
class Piso(models.Model):
    #crear los campos del modelo: un campo corresponde con una columna de la tabla "principal_piso"
    numReferencia = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=100)
    poblacion = models.CharField(max_length=80)
    cp = models.CharField(max_length=20)
    precio = models.FloatField()
    metroscuadrados = models.IntegerField()
    numHabitaciones = models.IntegerField()
    planta = models.IntegerField()
    banios = models.IntegerField()
    ascensor = models.BooleanField()
    garaje = models.BooleanField()
    terraza = models.BooleanField()
    descCorta = models.CharField(max_length=200)
    comentario = models.TextField()
    correoContacto = models.EmailField()
    fechaAlta = models.DateField(auto_now_add=True, verbose_name="Fecha de alta") #esto es el nombre que va a aparecer de titulo de tabla, se añade asi para que pueda haber espacios
    fechaModificacion = models.DateField(auto_now=True, verbose_name="Fecha de modificacion")

    def __str__(self):
        #esto es lo que sale cuando entras en la administracion de la tabla en el servidor
        return self.numReferencia + "(" + self.poblacion + ")"    
    class Meta:
        #si esto no se pone, se ordena por id por defecto, pero al poner esto nos lo ordena por poblacion y por codigo postal
        ordering = ["poblacion","cp"]

##TRAS CREAR EL FICHERO, HAY QUE AÑADIR LA MIGRACION PARA QUE SE CREE TODOs EN LA BASE DE DATOS

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.IntegerField()

    def __srt__(self):
        return self.nombre + " " + self.apellidos + " " + self.telefono
    class Meta:
        #si esto no se pone, se ordena por id por defecto, pero al poner esto nos lo ordena por poblacion y por codigo postal
        ordering = ["nombre"]