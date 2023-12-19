from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Piso, Cliente

# Create your views here.
#ESTA ES LA VISTA QUE SE CARGA EN LA PAGINA SEGUN EJECUTAS EL RUNSERVER
def catalogo(request):
    catalogo = loader.get_template('principal\catalogo.html')
    
    #consulta a la tabla de pisos para sacar todo el contenido
    todosLosPisos = Piso.objects.all()
    contexto = {
        #listado de todos los pisos ahora esta en el template
        'pisos':todosLosPisos,
        # 'pisos': Piso.objects.all() esto es lo mismo que lo anterior pero sin guardarlo en una variable antes
        'clientes': Cliente.objects.all() #traer todos los clientes
    }
    #esto es la redireccion-> es lo mejor para hacer
    return HttpResponse(catalogo.render(contexto, request))

def crearCliente(request):
    ##EN LA WEB, VEZ QUE EN LA BARRA PONGA crearCliente, creará el cliente que hay en el objeto
    #Cliente es una clase heredada de model y al ser una clase, me permite crear objetos con ella
    cli = Cliente(nombre="Pepe", apellidos="Ruiz Ruiz", email="peperuiz@correo.com", telefono="665453621",inversor=False)

    #esto es el insert en base de datos, mete el nuevo contenido en la BBDD
    cli.save()

    #para mostrar el cliente y los demas: hacemos redireccion la rita que se llama catalogo y muestra así, todos los pisos y clientes
    return HttpResponseRedirect(reverse('catalogo')) #reverse busca dentro de las urls alguna que se llame catalogo

def modificarCliente(request):
    #ESTRUCTURA-> BUSCAR, MODIFICAR Y GUARDAR
    cli = Cliente.objects.get(id=1) #busca el cliente con id 1 y cambiamos su movil; get se usa cuando lo que va a devolver es solo un valor
    cli.telefono = "111111111" #cambiar de valor el telefono
    cli.save()

    return HttpResponseRedirect(reverse('catalogo'))

def borrarCliente(request):
    try:
        cli = Cliente.objects.get(id=1) 
        cli.delete()
    except:
        pass
    
    return HttpResponseRedirect(reverse('catalogo'))