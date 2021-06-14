from django.db import models


class gadgetAttr(models.Model):
    asins = models.CharField(max_length=22)
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    brand = models.CharField(max_length=35)
    dimensions = models.CharField(max_length=60, null=True, blank=True)
    imageurls = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
