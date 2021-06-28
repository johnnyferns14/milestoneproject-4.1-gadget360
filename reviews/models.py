from django.db import models
from django.contrib.auth.models import User
from gadgets.models import gadgetAttr
from django.utils import timezone


class ProductReview(models.Model):
    gadget = models.ForeignKey(gadgetAttr, null=True,
                               blank=True, on_delete=models.CASCADE)
    cust_name = models.ForeignKey(User, null=False,
                                  blank=False, on_delete=models.CASCADE)
    review_title = models.CharField(max_length=150, blank=False)
    review_description = models.TextField(blank=False)
    date_added = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.review_title
