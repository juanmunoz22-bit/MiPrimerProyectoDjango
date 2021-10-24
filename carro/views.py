from django.shortcuts import render

from .carro import Carro

from tienda.models import Productos

from django.shortcuts import redirect

# Create your views here.

def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id=producto_id)
    carro.agregar(producto)
    return redirect('tienda')


def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id=producto_id)
    carro.eliminar(producto)
    return redirect('tienda')


def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id=producto_id)
    carro.restar(producto)
    return redirect('tienda')


def limpiar_carro(request):
    carro = Carro(request)
    carro.vaciar()
    return redirect('tienda')