from django.db import models


class gadgetCategory(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class gadgetAttr(models.Model):
    category = models.ForeignKey(gadgetCategory, null=True, blank=True,
                                on_delete=models.SET_NULL)
    asins = models.CharField(max_length=22)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    brand = models.CharField(max_length=50)
    dimensions = models.CharField(max_length=60, null=True, blank=True)
    imageurls = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
