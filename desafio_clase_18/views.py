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


    
    
    



 