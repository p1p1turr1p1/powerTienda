from django.db import models

# # Create your models here.


class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)


class CategoriaProducto(models.Model):
    id_cat = models.AutoField(db_column='idCategoria', primary_key=True)
    nombre_categoria = models.CharField(max_length=30, blank=False, null=False)


class Talla(models.Model):
    id_talla = models.AutoField(db_column='idTalla', primary_key=True)
    nombre_talla = models.CharField(max_length=30, blank=False, null=False)


def __str__(self):
    return str(self.genero)


class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    id_genero = models.ForeignKey(
        'Genero', on_delete=models.CASCADE, db_column='idGenero')
    telefono = models.CharField(max_length=45)
    email = models.EmailField(
        unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)

    class Meta:
        ordering = ['rut']


class Producto(models.Model):
    id_producto = models.AutoField(db_column='idProducto', primary_key=True)
    nombre = models.CharField(max_length=40)
    id_cat = models.ForeignKey(
        'CategoriaProducto', on_delete=models.CASCADE, db_column='idCategoria')
    id_talla = models.ForeignKey(
        'Talla', on_delete=models.CASCADE, db_column='idTalla')
    precio = models.PositiveBigIntegerField()
    imagen = models.ImageField(upload_to='uploads/')
    precio = models.PositiveBigIntegerField()
    stock = models.PositiveBigIntegerField()