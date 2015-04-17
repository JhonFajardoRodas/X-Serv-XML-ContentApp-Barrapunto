from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import ListaDB
from django.views.decorators.csrf import csrf_exempt
from barrapunto import get_bp
import urllib2
 
# Create your views here.

bpOk = ""
@csrf_exempt

def mostrarTodo(request):
    global bpOk
    bpOk = get_bp()
    return HttpResponse("<li><b>TITULARES ACTUALIZADOS de barrapunto.com: </b></li>" + "<li>" + bpOk+ "</li>")

def buscarPersona(request, recurso):

    if request.method == 'GET':
        try:
            
            valor = ListaDB.objects.get(name=recurso)
            salida = valor.age
            return HttpResponse("<html><body>" + str(salida) + "<hr><br>" + bpOk + "</br></hr>" + "</body></html>")
        except ListaDB.DoesNotExist:
            return HttpResponseNotFound("No existe el elmento!")
    elif request.method == 'PUT':
        entryNew = ListaDB(name=recurso, age=request.body)
        entryNew.save()
        salida =  "Almacenado: " + entryNew.name
        return HttpResponse(salida)

