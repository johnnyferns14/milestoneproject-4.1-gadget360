from django.db import models
from gadgets.models import gadgetAttr

# Create your models here.

class OrderDetail(models.Model):
    order_number = models.CharField(max_length=30, null=False, editable=False)
    cust_name = models.CharField(max_length=60, null=False, blank=False)
    email_id = models.EmailField(max_length=200, null=False, blank=False)
    contact_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    postcode = models.CharField(max_length=15, null=False, blank=False)
    town_or_city = models.CharField(max_length=30, null=False, blank=False)
    address1 = models.CharField(max_length=100, null=False, blank=False)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    county = models.CharField(max_length=30, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_length=30, null=False, blank=False)
    order_total = models.DecimalField(max_length=30, null=False, blank=False)
    grand_total = models.DecimalField(max_length=30, null=False, blank=False)


class OrderLineItem():
    order = models.ForeignKey(OrderDetail, null=False, blank=False,
                              on_delete=models.CASCADE, related_name='lineitems')
    gadget = models.ForeignKey(gadgetAttr, null=False, blank=False,
                               on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False, editable=False)
