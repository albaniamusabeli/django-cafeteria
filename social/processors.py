## importar los modelos
from .models import Link

def contexto_diccionario(request):
    dicc = {}
    ## obtengo todos los links
    links = Link.objects.all()
    
    ## recorrer los link para ir llenando el dicc
    for i in links:
        dicc[i.key] = i.url ## accede al url de la bbdd Link
    return dicc