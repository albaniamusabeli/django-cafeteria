from django.shortcuts import render
from .models import Service


# Create your views here.

def services(request):

    ## obtener todos los objetos de la base de datos
    servicios = Service.objects.all()

    ## los servicios que estan en la BBDD se guardan en el diccionario contexto
    ## que contiene la listaServicios que se MOSTRARA EN HTML!!!!
    contexto = {
        "listaServicios": servicios
    }

    return render(request, 'services/services.html', contexto)