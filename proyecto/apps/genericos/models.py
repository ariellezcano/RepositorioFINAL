from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Rubro(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class SubRubro(models.Model):
    nombre = models.CharField(max_length=50)
    rubro = models.ForeignKey(Rubro, related_name='mi_rubro', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    