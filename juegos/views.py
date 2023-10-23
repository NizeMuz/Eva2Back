from django.shortcuts import render

# Create your views here.

def Inicio(request):
     return render(request,'templatesApp/juegos.html')

def Hellblade(request):
     data = {
          "imagenBandera" : "Hellblade.jpg",
          "nombre": "Nombre: Hellblade 2",
          "idioma": "Fecha de estreno: 2024",
          "lema": "Desarollador: Ninja Theory",
          "continente": "Plataformas: Xbox series X|S",
          "disabled" : "not-active"
          }
     return render(request,'templatesApp/juegos.html', data)


def Doom(request):
     data = {
          "imagenBandera" : "doom.jpg",
          "nombre": "Nombre: Doom",
          "idioma": "Fecha de estreno: 20 de marzo de 2020",
          "lema": "Desarollador: id Software,Panic Button",
          "continente": "Plataformas: Nintendo Switch,PlayStation 5,Xbox series X|S",
          "disabled2" : "not-active"
          }
     return render(request,'templatesApp/juegos.html', data)


def Halo(request):
     data = {
          "imagenBandera" : "halo.jpg",
          "nombre": "Nombre: Halo",
          "idioma": "Fecha de estreno: 15 de noviembre de 2021",
          "lema": "Desarollador: 343 Industries",
          "continente": "Plataformas: Xbox series X|S",
          "disabled3" : "not-active"
          }
     return render(request,'templatesApp/juegos.html', data)