from django.db import models
from datetime import date
# Create your models here.

class Currency(models.Model):
    Date =  models.DateField()
    Dollar = models.DecimalField(max_digits=9,decimal_places=4)
    Pound = models.DecimalField(max_digits=9,decimal_places=4)
    Euro = models.DecimalField(max_digits=9,decimal_places=4)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Currencies"
