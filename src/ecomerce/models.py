from django.db import models

# Create your models here.
class ProductModel(models.Model):#heredando de models de django
    title= models.TextField()
    description = models.TextField(default="Sin descripción")
    seller = models.TextField(default="Desconocido")
    color = models.TextField(default="No especificado")
    dimensions = models.FloatField(default=0.0)
    price = models.FloatField()
