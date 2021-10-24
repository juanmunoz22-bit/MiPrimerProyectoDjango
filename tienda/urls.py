#Crea un archivo urls.py en el directorio tienda
#Este archivo contiene las urls de la tienda


from django.urls import path
from . import views


urlpatterns = [
    path('', views.tienda, name='tienda'),
]