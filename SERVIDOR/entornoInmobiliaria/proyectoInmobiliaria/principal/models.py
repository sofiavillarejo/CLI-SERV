from django.db import models

# Create your models here.
#########################################################
#CLASES PARA CONFIGURAR LA INTERFAZ DE ADMINISTRACION

class Piso(models.Model):
    ####SI LOS CAMPOS APARECEN EN NEGRITA, ES QUE SON OBLIGATORIOS DE RELLENAR####

    #crear los campos del modelo: un campo corresponde con una columna de la tabla "principal_piso"
    numReferencia = models.CharField(max_length=20, unique=True)
    #upload_to -> envia el archivo a la carpeta que pogas, en este caso la crea
    imagenPiso = models.ImageField(verbose_name="Imagen de piso", null=True, blank=True, upload_to="imgPisos") #al crear este nuevo campo de tabla una vez creada,
    #no pregunta que valor darle porque le estamos poniendo que puede ser null
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
    #añadmos nuevo campo a la tabla ya existente -> makemigrations y seleccionamos 1, y ponemos True or False segun 
    #el valor que queramos darle -> en este caso, False
    inversor = models.BooleanField()

    def __str__(self):
        return self.nombre + " " + self.apellidos + " " + "(" + str(self.telefono) + ")"
    #añadir filtros -> nombre
    class Meta:
        #si esto no se pone, se ordena por id por defecto, pero al poner esto nos lo ordena por poblacion y por codigo postal
        ordering = ["nombre"]

###SI HACEMOS ALGUN TIPO DE MODIFICACION EN ESTA PAGINA PARA ACTUALIZARLA, TENEMOS QUE HACER EL MAKEMIGRATIONS Y DESPUES, EL MIGRATE#######