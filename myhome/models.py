from django.db import models

# Create your models here.
class productInfo(models.Model):
    product_title = models.CharField(max_length=50)
    product_descripton = models.TextField()
    product_brand = models.CharField(max_length=30, default='nobrand')
    product_category = models.CharField(default='abc', max_length=20)
    product_quantity = models.IntegerField(null=False)
    product_image = models.CharField(max_length=100)
    product_price = models.IntegerField(null=False)
