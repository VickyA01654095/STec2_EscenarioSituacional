from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from json import loads, dumps
import sqlite3

# Create your views here.
from django.http import HttpResponse

def index(request):

  return HttpResponse("Hello Geeks")

def apartarProducto(request):
    mydb = sqlite3.connect("CB_DB.db")
    curr = mydb.cursor()

    query_spaces = '''SELECT name, description FROM spaces '''

    curr.execute(query_spaces)
    
    mydb.commit()
    mydb.close()

    json = dumps({"msg": "producto apartado"})

    return HttpResponse(json, content_type="application/json")