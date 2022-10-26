from django.shortcuts import render, redirect
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

def test(request):

  return render(request, 'testShowApartados.html')


def showApartados(request):
  ## falta modificar 
  mydb = sqlite3.connect("db.sqlite3")
  curr = mydb.cursor()

  productsQry = '''SELECT Producto.nombre, Producto.precio, Producto.estado_actual 
  FROM Producto INNER JOIN Producto_apartado
  ON Producto_apartado.producto_id = Producto.id WHERE Producto_apartado.comprador_id = 1'''

  productsQry = curr.execute(productsQry)

  list_products = []

  for x in productsQry:
    list_products.append([x[0], x[1], x[2]])
  
  mydb.commit()
  mydb.close()

  return render(request, 'index.html', {'apartados': list_products})

def getProductos(request):
  mydb = sqlite3.connect("db.sqlite3")
  curr = mydb.cursor()

  productsQry = '''SELECT nombre, precio, estado_actual, id FROM Producto'''
  productsQry = curr.execute(productsQry)

  list_products = []

  for x in productsQry:
    list_products.append([x[0], x[1], x[2], x[3]])
  
  mydb.commit()
  mydb.close()

  return render(request, 'index.html', {'products': list_products})


@csrf_exempt
def apartarProducto(request):
  user_id = 1
  product_id = request.POST["prod_id"]
  tiempo = "01:00"

  user = Comprador.objects.get(pk=user_id)
  prod = Producto.objects.get(pk=product_id)
  
  apartado = Producto_apartado.objects.create(vendedor=prod.vendedor, comprador=user,
  producto=prod,tiempo_apartado=tiempo,precio=prod.precio)

  apartado.save()

  json = dumps({"msg": "producto apartado"})

  return redirect('productos')

