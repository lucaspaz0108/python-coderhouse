from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader
from datetime import datetime


def vista_saludo(request):
    return HttpResponse("Hola coders!")

def dia_hoy(request, nombre):
    hoy = datetime.now()

    respuesta = f"Hoy es {hoy} - Bienvenido {nombre}"
    return HttpResponse(respuesta)

def anio_nacimiento(request, edad):
    
    edad = int(edad)

    anio_nac = datetime.now().year - edad
    return HttpResponse(f"Naciste en {anio_nac}")

def vista_plantilla(request):
    archivo = open(r"C:\Users\Lucas\Desktop\coder\mi_sitio\mi_sitio\templates\plantilla.html")

    plantilla = Template(archivo.read())
    
    archivo.close()

    #Diccionario con datos para la plantilla
    datos = {"nombre": "Lucas", "fecha": datetime.now(), "apellido": "Paz", "edad": 22}

    contexto = Context(datos)

    documento = plantilla.render(contexto)
    
    return HttpResponse(documento)

def vista_listado_alumnos(request):
    
    archivo = open(r"C:\Users\Lucas\Desktop\coder\mi_sitio\mi_sitio\templates\listado_alumnos.html")

    plantilla = Template(archivo.read())

    archivo.close()
    
    listado_alumnos = ["Lucas paz", "cristian jaimes", "facundo gimenez", "zamudio lautaro", "camila deambrosio"]

    datos = {"tecnologia": "Python", "listado_alumnos": listado_alumnos}

    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)


def vista_listado_alumnos2(request):
    listado_alumnos = ["Lucas paz", "cristian jaimes", "facundo gimenez", "zamudio lautaro", "camila deambrosio"]
    datos = {"tecnologia": "Python", "listado_alumnos": listado_alumnos}
    plantilla = loader.get_template("listado_alumnos.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)




