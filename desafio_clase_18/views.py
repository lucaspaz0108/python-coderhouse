from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from desafio_clase_18.models import Familiares

# Create your views here.



    
def ListadoFamiliares(request):
    familia = Familiares.objects.all()

    cadena_respuesta = " "
    for familiar in familia:
        cadena_respuesta += familiar.nombre + " " + str(familiar.edad) + " " + str(familiar.fecha_nacimiento) + " "
    
    return HttpResponse(cadena_respuesta)
    



 