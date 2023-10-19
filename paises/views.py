from django.shortcuts import render

# Create your views here.

def Inicio(request):
     return render(request,'templatesApp/paises.html')

def Chile(request):
     data = {
          "imagenBandera" : "chile.png",
          "nombre": "Chile",
          "idioma": "español",
          "lema": "Por la razón o la fuerza",
          "continente": "Americano",
          "disabled" : "not-active"
          }
     return render(request,'templatesApp/paises.html', data)


def Venezuela(request):
     data = {
          "imagenBandera" : "venezuela.png",
          "nombre": "Venezuela",
          "idioma": "Español",
          "lema": "Comer o matar",
          "continente": "Americano",
          "disabled2" : "not-active"
          }
     return render(request,'templatesApp/paises.html', data)


def Cuba(request):
     data = {
          "imagenBandera" : "cuba.png",
          "nombre": "Cuba",
          "idioma": "Español",
          "lema": "Patria y vida",
          "continente": "Americano",
          "disabled3" : "not-active"
          }
     return render(request,'templatesApp/paises.html', data)