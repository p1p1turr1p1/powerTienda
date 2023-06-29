from django.db import models
from datetime import datetime
# # Create your models here.

class Talla(models.Model):
    nombre= models.CharField(max_length=50)
    
def __str__(self):
    return self.nombre

class Categoria(models.Model):
    nombre= models.CharField(max_length=50)

def __str__(self):
    return self.nombre

class Producto(models.Model):
    nombre= models.CharField(max_length=50)
    precio= models.IntegerField()
    descripción = models.TextField()
    talla= models.ForeignKey(Talla, on_delete=models.PROTECT)
    categoria= models.ForeignKey(Categoria, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to='productos', null=True)

def __str__(self):
    return self.nombrecda