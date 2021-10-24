from django.contrib import admin
from .models import CategoriaProductos, Productos
# Register your models here.

class CategoriaProductosAdmin(admin.ModelAdmin):
    
    readonly_fields = ('created', 'updated')


class ProductosAdmin(admin.ModelAdmin):

    readonly_fields = ('created', 'updated')

admin.site.register(CategoriaProductos, CategoriaProductosAdmin)

admin.site.register(Productos, ProductosAdmin)
