from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from .models import Vendedor, Comprador, Producto, Producto_apartado, Mensaje, Chat
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime as dtm
from json import loads, dumps
import sqlite3

# Create your views here.
from django.http import HttpResponse

def index(request):

  return HttpResponse("Hello Geeks")

@csrf_exempt
def apartarProducto(request):
  body_unicode = request.body.decode('utf-8')
  body = loads(body_unicode)
  user_id = body["user_id"]
  product_id = body["prod_id"]
  tiempo = body["time"]

  user = Comprador.objects.get(pk=user_id)
  prod = Producto.objects.get(pk=product_id)
  
  apartado = Producto_apartado.objects.create(vendedor=prod.vendedor, comprador=user,
  producto=prod,tiempo_apartado=tiempo,precio=prod.precio)

  apartado.save()

  json = dumps({"msg": "producto apartado"})

  return HttpResponse(json, content_type="application/json")