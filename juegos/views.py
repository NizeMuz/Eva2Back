from django.shortcuts import render

# Create your views here.

def Inicio(request):
     return render(request,'templatesApp/juegos.html')

def Hellblade(request):
     data = {
          "imagenBandera" : "Hellblade.jpg",
          "nombre": "Nombre: Hellblade",
          "idioma": "Fecha de estreno: 8 de agosto de 2017",
          "lema": "Desarollador: Ninja Theory",
          "continente": "Plataformas: Nintendo Switch, Xbox series X|S",
          "disabled" : "not-active"
          }
     return render(request,'templatesApp/juegos.html', data)


def Doom(request):
     data = {
          "imagenBandera" : "doom.jpg",
          "nombre": "Nombre: Doom",
          "idioma": "Fecha de estreno: 20 de marzo de 2020",
          "lema": "Comer o matar",
          "continente": "Americano",
          "disabled2" : "not-active"
          }
     return render(request,'templatesApp/juegos.html', data)


def Halo(request):
     data = {
          "imagenBandera" : "Halo.jpg",
          "nombre": "Cuba",
          "idioma": "Español",
          "lema": "Patria y vida",
          "continente": "Americano",
          "disabled3" : "not-active"
          }
     return render(request,'templatesApp/juegos.html', data)