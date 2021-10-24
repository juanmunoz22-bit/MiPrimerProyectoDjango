from django.shortcuts import render
from .models import Productos

# Create your views here.


def tienda(request):
    #almacenar la lista de productos en una variable
    productos = Productos.objects.all()
    
    return render(request, 'tienda/tienda.html', {'productos': productos})
