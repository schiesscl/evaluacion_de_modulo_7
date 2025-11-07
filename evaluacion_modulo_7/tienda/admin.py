from django.contrib import admin
from .models import Categoria, Etiqueta, DetallesProducto, Producto

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Etiqueta)
admin.site.register(DetallesProducto)
admin.site.register(Producto)