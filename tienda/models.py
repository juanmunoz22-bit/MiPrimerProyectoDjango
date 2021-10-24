from django.db import models

# Create your models here.

#Crea una clase para el modelo de la categoriaproductos con los siguientes campos: nombre, created(auto_now_add=True), updated(auto_now=True)
class CategoriaProductos(models.Model):
    nombre = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #Crea una clase para el modelo de la productos con los siguientes campos: nombre, precio, stock, descripcion, categoria, created(auto_now_add=True), updated(auto_now=True)
    class Meta:
        verbose_name = 'CategoriaProd'
        verbose_name_plural = 'CategoriasProd'

    def __str__(self):
        return self.nombre

#clase para el modelo de productos con campos nombre, categorias, imagen que se suba a la carpeta tienda, precio, stock que sea un valor boolean que inicie como true, created(auto_now_add=True), updated(auto_now=True)
class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(CategoriaProductos, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='tienda/productos')
    precio = models.FloatField()
    stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #Crea una clase para el modelo de la carrito con los siguientes campos: producto, cantidad, usuario, created(auto_now_add=True), updated(auto_now=True)
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre