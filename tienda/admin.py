from django.contrib import admin
from .models import Usuario,Genero,Producto,CategoriaProducto,Talla

# # Register your models here.
admin.site.register(Genero)
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(CategoriaProducto)
admin.site.register(Talla)

