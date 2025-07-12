from django.contrib import admin

# Register your models here.

# core/admin.py
from django.contrib import admin
from .models import Cliente, Producto, Carrito, ItemCarrito, Venta, DetalleVenta

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(ItemCarrito)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
