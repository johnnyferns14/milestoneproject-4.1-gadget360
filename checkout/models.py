from django.db import models
import uuid
from django.db.models import Sum
from django.conf import settings
from gadgets.models import gadgetAttr


class OrderDetail(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
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
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.order_total = self.lineitems.aggregate(Sum('total_lineitem'))['total_lineitem__sum']

        if self.order_total < settings.FREE_DELIVERY_LIMIT:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_RATE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(OrderDetail, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    gadget = models.ForeignKey(gadgetAttr, null=False, blank=False,
                               on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    total_lineitem = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        self.total_lineitem = self.gadget.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'ASIN: {self.gadget.asins} for order {self.order.order_number}'
