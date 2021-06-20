from django.db import models

class review(models.Model):
    reviews_title = models.CharField(max_length=50)
