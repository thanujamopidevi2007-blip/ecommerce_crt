from django.db import models

# Create your models here.
from django.db import models
from django.db.models import AutoField


# Create your models here.
class ProductModel(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    quantity=models.IntegerField()

class Cart(models.Model):
    cart_id=AutoField(primary_key=True)
    product_id=models.IntegerField()
    p_price=models.FloatField()
