from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.nombre)

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.nombre)

class DetallesProducto(models.Model):
    producto = models.OneToOneField('Producto', on_delete=models.CASCADE, primary_key=True)
    dimensiones = models.CharField(max_length=100, blank=True, null=True)
    peso = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Detalles de {self.producto.nombre}"

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='productos')
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)

    def __str__(self):
        return str(self.nombre)