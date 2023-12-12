from django.contrib import admin
from .models import Piso, Cliente
# Register your models here.

#en principal en pisos (servidor) te saca en tabla todos los datos que indiques
class PisoAdmin(admin.ModelAdmin):
    list_display = ("numReferencia","poblacion", "direccion", "precio", "fechaAlta", "fechaModificacion")
    #filtrar por campos
    list_filter = ("poblacion", "cp")
    search_fields = ("poblacion", )

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre","apellidos", "email", "telefono")
    #filtrar por campos
    list_filter = ("nombre",)
    search_fields = ("nombre", )

admin.site.register(Piso, PisoAdmin) #aqui le digo la tabla que va a manejar el usuario
admin.site.register(Cliente, ClienteAdmin)