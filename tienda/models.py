from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

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
    nombre= models.CharField(max_length=200)
    precio= models.FloatField()
    descripción = models.TextField()
    categoria= models.ForeignKey(Categoria, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)
    digital = models.BooleanField(default=False,null=True, blank=True)
    def __str__(self):
        return self.nombre
    @property
    def imageURL(self):
        try:
            url = self.imagen.url
        except:
            url = ''
        return url  
    
