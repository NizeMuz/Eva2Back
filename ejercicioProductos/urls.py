"""
URL configuration for ejercicioProductos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import index
from app1.views import electronica
from app1.views import juguetes
from app1.views import ropa
from juegos.views import Hellblade
from juegos.views import Doom
from juegos.views import Halo
from juegos.views import Inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('electronica/', electronica),
    path('juguetes/', juguetes),
    path('ropa/', ropa),
    path('Hellblade/', Hellblade),
    path('Doom/', Doom),
    path('Halo/', Halo),
    path('inicio/', Inicio),
    
    
]
