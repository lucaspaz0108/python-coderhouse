from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from desafio_clase_18.models import Familiares

# Create your views here.



    
def listado_Familiares(request):
    listaFamiliares = Familiares.objects.all()
    datos = {"listaFamiliares": listaFamiliares,}
    plantilla = loader.get_template("Template.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)

    #cadena_respuesta = " "
    #for familiar in familia:
        #cadena_respuesta += familiar.nombre + " " + str(familiar.edad) + " " + str(familiar.fecha_nacimiento) + " "
    
    
    



 