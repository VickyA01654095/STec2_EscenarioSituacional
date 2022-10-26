from django.urls import path, include 

#now import the views.py file into this code

from . import views

urlpatterns=[
  path('', views.index),
  path('apartar', views.apartarProducto, name='apartar'),
  path('categories', views.getProductos, name='productos'),
  path('about', views.ofertas, name='ofertas'),
  path('contact', views.contact, name='contact'),
  
]