from django.db import models
from apps.core.models import TimeModels
from apps.genericos.models import SubRubro
# Create your models here.

class Producto(TimeModels):
    nombre = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=0)
    subrubro = models.ForeignKey(SubRubro, on_delete=models.SET_NULL, null= True)

    def __str__(self):
        return self.nombre
    