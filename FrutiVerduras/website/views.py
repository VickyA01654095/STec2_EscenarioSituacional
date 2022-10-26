from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime as dtm
from json import loads, dumps
import sqlite3

# Create your views here.
from django.http import HttpResponse

def index(request):

  return render(request, 'home.html')

def ofertas(request):

  return render(request, 'ofertas.html')

def contact(request):

  return render(request, 'contact.html')

def carrito(request):
  mydb = sqlite3.connect("FrutasVerduras.db")
  curr = mydb.cursor()

  productsQry = '''SELECT producto.nombre,  vendedor.nombre_comercio, producto.precio
                  FROM producto_apartado INNER JOIN  vendedor, producto
                  ON  producto_apartado.producto_id = producto.id 
									AND producto_apartado.vendedor_id = vendedor.id
									WHERE producto_apartado.comprador_id = 3'''

  productsQry = curr.execute(productsQry)

  list_products = []

  for x in productsQry:
    list_products.append([x[0], x[1], x[2]])
    print(x[0], x[1], x[2])
  
  mydb.commit()
  mydb.close()

  return render(request, 'carrito.html', {'reservas': list_products})

def getProductos(request):
  mydb = sqlite3.connect("FrutasVerduras.db")
  curr = mydb.cursor()

  productsQry = '''SELECT nombre, precio, id FROM producto'''
  productsQry = curr.execute(productsQry)

  list_products = []

  for x in productsQry:
    list_products.append([x[0], x[1], x[2]])
  
  mydb.commit()
  mydb.close()

  return render(request, 'htmltest.html', {'products': list_products})


def apartarProducto(request):
  user_id = 3
  product_id = request.GET.get('prod_id')
  tiempo = "01:00"
  date = dtm.now()

  mydb = sqlite3.connect("FrutasVerduras.db")
  curr = mydb.cursor()

  product_info = '''SELECT vendedor_id, precio FROM producto WHERE id=?'''
  product_info = curr.execute(product_info, (product_id,)).fetchall()

  insertQry = '''INSERT INTO producto_apartado (vendedor_id,comprador_id,producto_id,tiempo_apartado,precio,created_at)
        VALUES (?, ?, ?, ?, ?, ?);'''
  insertQry = curr.execute(insertQry, (product_info[0][0],user_id,product_id,tiempo,product_info[0][1],date)).fetchall()

  mydb.commit()
  mydb.close()

  return redirect('productos')

