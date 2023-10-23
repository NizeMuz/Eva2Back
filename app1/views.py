from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    data = {
         "nombre": "Inicio"
         }
    return render(request,'templatesApp/index.html', data)

def electronica(request):
     data = {
          "nombre": "Electronica",
          "articulo1": "Mac",
          "articulo2": "Iphone",
          "articulo3": "Xbox Series X|S"
          }
     return render(request,'templatesApp/productos.html', data)

def juguetes(request):
     data = {
         "nombre": "Juguetes",
         "articulo1": "Moto",
         "articulo2": "Cubo rubik",
         "articulo3": "Figura de accion" 
     }
     return render(request,'templatesApp/productos.html', data)

def ropa(request):
     data = {
          "nombre": "Ropa",
          "articulo1": "Pantalones",
          "articulo2": "Chaqueta",
          "articulo3": "Camisa" 
     }
     return render(request,'templatesApp/productos.html', data)