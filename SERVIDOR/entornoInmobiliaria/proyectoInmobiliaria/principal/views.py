from django.http import HttpResponse
from django.template import loader
from .models import Piso

# Create your views here.
#ESTA ES LA VISTA QUE SE CARGA EN LA PAGINA SEGUN EJECUTAS EL RUNSERVER
def catalogo(request):
    catalogo = loader.get_template('principal\catalogo.html')
    
    #consulta a la tabla de pisos para sacar todo el contenido
    todosLosPisos = Piso.objects.all()
    contexto = {
        #listado de todos los pisos ahora esta en el template
        'pisos':todosLosPisos
    }
    return HttpResponse(catalogo.render(contexto, request))
