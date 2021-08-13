from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.

class TimeModels(models.Model):
    creado = DateTimeField(auto_now_add=True,
                            verbose_name=u'creado',
                            help_text=u'fecha de creacion')
    modificado = models.DateTimeField(auto_now_add=True,
                            verbose_name=u'modificado',
                            help_text=u'fecha de modificacion')

    class Meta():
        abstract = True