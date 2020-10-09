from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    product_id = models.CharField(max_length=200)
    namecat = models.CharField(max_length=200)
    partnumber = models.CharField(max_length=200)
    productname = models.CharField(max_length=200)
    product_price = models.IntegerField()
    detail = models.CharField(max_length=200)
    longdesc = models.TextField(max_length=200)
    link = models.URLField()
    img = models.URLField()



    def __str__(self):
        return self.productname


